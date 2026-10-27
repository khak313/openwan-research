"""Deterministic arithmetic baselines; not a network simulator."""
from fractions import Fraction
import json
import math


def _capacities(values):
    values = tuple(values)
    if not values or any(isinstance(v, bool) or not isinstance(v, (int, float))
                         or not math.isfinite(v) or v < 0 for v in values):
        raise ValueError("capacities must be finite nonnegative numbers in Mbps")
    weights = tuple(Fraction(str(v)) for v in values)
    if not sum(weights):
        raise ValueError("at least one capacity must be positive")
    return weights


def allocate_flows(count, capacities):
    """Allocate equal-sized independent flows by largest remainders."""
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("count must be a nonnegative integer")
    weights = _capacities(capacities)
    shares = [count * w / sum(weights) for w in weights]
    result = [int(s) for s in shares]
    order = sorted(range(len(weights)), key=lambda i: (-(shares[i] - result[i]), i))
    for i in order[:count - sum(result)]:
        result[i] += 1
    return result


def ideal_transfer_seconds(size_bytes, capacities):
    """Optimistic bound with independent links and zero overhead (decimal Mbps)."""
    if isinstance(size_bytes, bool) or not isinstance(size_bytes, int) or size_bytes < 0:
        raise ValueError("size_bytes must be a nonnegative integer")
    return float(Fraction(size_bytes * 8, 1_000_000) / sum(_capacities(capacities)))


if __name__ == "__main__":
    print(json.dumps({"kind": "synthetic arithmetic illustration",
                      "capacities_mbps": [20, 10], "flows": allocate_flows(12, [20, 10]),
                      "payload_bytes": 30_000_000,
                      "ideal_lower_bound_seconds": ideal_transfer_seconds(30_000_000, [20, 10])}, indent=2))
