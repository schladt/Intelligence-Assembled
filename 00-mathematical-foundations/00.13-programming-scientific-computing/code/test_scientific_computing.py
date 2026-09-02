"""Boundary-focused tests for the module 0.13 computing contracts."""

import json
from pathlib import Path
import tempfile
import unittest

import matplotlib
import numpy as np
from numpy.testing import assert_allclose, assert_array_equal

from scientific_computing import (
    ArrayContract,
    ContractError,
    RunningMean,
    affine_batch,
    benchmark,
    broadcast_result_shape,
    environment_snapshot,
    memory_relation,
    save_exploration_plot,
    spawn_generators,
    stable_logsumexp,
)


class ContractTests(unittest.TestCase):
    def test_array_contract_accepts_named_axes_and_rejects_boundaries(self) -> None:
        contract = ArrayContract((None, 3), "f")
        array = contract.validate(np.ones((4, 3), dtype=np.float32), name="features")
        self.assertEqual(array.shape, (4, 3))
        self.assertEqual(array.size, 12)
        self.assertEqual(array.ndim, 2)
        with self.assertRaisesRegex(ContractError, "axis 1"):
            contract.validate(np.ones((4, 2)), name="features")
        with self.assertRaisesRegex(ContractError, "dtype kind"):
            contract.validate(np.ones((4, 3), dtype=np.int16), name="features")
        with self.assertRaisesRegex(ContractError, "finite"):
            contract.validate([[1.0, 2.0, np.nan]], name="features")

    def test_affine_batch_obeys_shape_dtype_and_operation_contracts(self) -> None:
        features = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
        weights = np.array([[2.0, 0.0], [0.0, -1.0]], dtype=np.float64)
        bias = np.array([0.5, 1.0], dtype=np.float64)
        result = affine_batch(features, weights, bias)
        assert_allclose(result, [[2.5, -1.0], [6.5, -3.0]])
        self.assertEqual(result.shape, (2, 2))
        self.assertEqual(result.dtype, np.dtype(np.float64))
        with self.assertRaisesRegex(ContractError, "axis 1"):
            affine_batch(features, np.ones((3, 3)), np.ones(3))

    def test_stable_logsumexp_matches_longdouble_reference(self) -> None:
        values = np.array([[1000.0, 1001.0, 999.0], [-1000.0, -999.0, -1001.0]])
        maximum = np.max(values.astype(np.longdouble), axis=1)
        reference = maximum + np.log(
            np.sum(np.exp(values.astype(np.longdouble) - maximum[:, None]), axis=1)
        )
        assert_allclose(stable_logsumexp(values, axis=1), reference, rtol=1e-14)
        with self.assertRaises(ContractError):
            stable_logsumexp(np.array([]))
        with self.assertRaisesRegex(ContractError, "axis 3"):
            stable_logsumexp(values, axis=3)

    def test_broadcast_validation_follows_trailing_dimensions(self) -> None:
        self.assertEqual(broadcast_result_shape((5, 1, 4), (3, 4)), (5, 3, 4))
        self.assertEqual(broadcast_result_shape((), (2, 3)), (2, 3))
        self.assertEqual(broadcast_result_shape((np.int64(2), 3), (1, 3)), (2, 3))
        with self.assertRaisesRegex(ContractError, "not broadcast-compatible"):
            broadcast_result_shape((2, 3), (2,))
        for invalid in (2.5, True, "2"):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(ContractError, "must be integers"):
                    broadcast_result_shape((invalid, 3))

    def test_basic_indexing_view_and_advanced_indexing_copy(self) -> None:
        source = np.arange(12).reshape(3, 4)
        view = source[:, 1:3]
        copy = source[[0, 2], :]
        self.assertTrue(memory_relation(source, view)["shares_memory"])
        self.assertTrue(memory_relation(source, view)["may_share_memory"])
        self.assertFalse(memory_relation(source, copy)["shares_memory"])
        self.assertFalse(memory_relation(source, copy)["may_share_memory"])
        view[0, 0] = 99
        copy[0, 0] = -1
        self.assertEqual(source[0, 1], 99)
        self.assertEqual(source[0, 0], 0)

    def test_running_mean_consumes_an_iterator_once_and_preserves_state(self) -> None:
        values = (number for number in [2.0, 4.0, 9.0])
        running = RunningMean()
        running.update(values)
        self.assertEqual(list(values), [])
        self.assertEqual((running.count, running.total, running.mean), (3, 15.0, 5.0))
        empty = RunningMean()
        with self.assertRaisesRegex(ContractError, "undefined"):
            _ = empty.mean

    def test_spawned_streams_reproduce_by_position_without_being_clones(self) -> None:
        first = spawn_generators(20260901, 3)
        second = spawn_generators(20260901, 3)
        first_draws = [generator.integers(0, 2**31, size=8) for generator in first]
        second_draws = [generator.integers(0, 2**31, size=8) for generator in second]
        for left, right in zip(first_draws, second_draws):
            assert_array_equal(left, right)
        self.assertFalse(np.array_equal(first_draws[0], first_draws[1]))

    def test_benchmark_records_setup_without_fragile_speed_assertions(self) -> None:
        calls = 0

        def operation() -> None:
            nonlocal calls
            calls += 1

        result = benchmark(operation, label="counter", number=3, repeat=4, warmup=2)
        self.assertEqual(calls, 14)
        self.assertEqual((result.number, result.repeat, result.warmup), (3, 4, 2))
        self.assertEqual(len(result.seconds), 4)
        self.assertTrue(all(observation >= 0.0 for observation in result.seconds))
        self.assertTrue(result.machine)
        self.assertEqual(json.loads(result.to_json())["label"], "counter")

    def test_environment_snapshot_records_process_and_versions(self) -> None:
        snapshot = environment_snapshot()
        self.assertEqual(snapshot["numpy_version"], np.__version__)
        self.assertEqual(snapshot["matplotlib_version"], matplotlib.__version__)
        self.assertTrue(snapshot["python_executable"].endswith(".venv/bin/python"))
        json.dumps(snapshot)

    def test_plot_is_written_only_to_temporary_storage(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "plot.png"
            returned = save_exploration_plot(
                np.arange(5.0), np.arange(5.0) ** 2, target,
                x_unit="s", y_unit="m",
            )
            self.assertEqual(returned, target)
            self.assertGreater(target.stat().st_size, 1_000)
            self.assertEqual(target.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
        self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()