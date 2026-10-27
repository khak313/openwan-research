import unittest
from openwan.baseline import allocate_flows, ideal_transfer_seconds


class BaselineTests(unittest.TestCase):
    def test_weighted_counts(self):
        self.assertEqual(allocate_flows(12, [20, 10]), [8, 4])

    def test_deterministic_ties(self):
        self.assertEqual(allocate_flows(2, [1, 1, 1]), [1, 1, 0])

    def test_zero_capacity(self):
        self.assertEqual(allocate_flows(5, [0, 2, 0]), [0, 5, 0])

    def test_invariants(self):
        for weights in ([1, 3, 7], [0, 0.1, 0.2], [1e308, 1e308]):
            for count in range(100):
                result = allocate_flows(count, weights)
                self.assertEqual(sum(result), count)
                self.assertTrue(all(v >= 0 for v in result))
                for value, weight in zip(result, weights):
                    if weight == 0:
                        self.assertEqual(value, 0)

    def test_invalid_capacities(self):
        for values in ([], [0], [-1], [float('nan')], [float('inf')], [True], ['20']):
            with self.subTest(values=values):
                with self.assertRaises(ValueError):
                    allocate_flows(2, values)
                with self.assertRaises(ValueError):
                    ideal_transfer_seconds(10, values)

    def test_invalid_counts_and_sizes(self):
        for value in (-1, 1.5, True, '1'):
            with self.assertRaises(ValueError):
                allocate_flows(value, [1])
            with self.assertRaises(ValueError):
                ideal_transfer_seconds(value, [1])

    def test_units_and_monotonicity(self):
        self.assertEqual(ideal_transfer_seconds(30_000_000, [20, 10]), 8)
        self.assertEqual(ideal_transfer_seconds(0, [1]), 0)
        self.assertLess(ideal_transfer_seconds(100, [1, 2]), ideal_transfer_seconds(100, [1]))

    def test_empty_workload(self):
        self.assertEqual(allocate_flows(0, [1, 2]), [0, 0])


if __name__ == '__main__':
    unittest.main()
