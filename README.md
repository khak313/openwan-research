# OpenWAN Research

Reproducible research on using heterogeneous Internet uplinks for availability and aggregate application throughput.

**Status: research proposal and analytical baseline.** This repository does not yet implement a router, bonding tunnel, or production failover service. No hardware measurements, deployments, adoption figures, or performance improvements are claimed.

## Research scope

Multi-WAN raises three distinct questions:

1. How should independent application flows be assigned to links with unequal capacity, latency, loss, and cost?
2. How can failure detection and recovery improve availability without excessive switching or broken sessions?
3. Under what conditions can a cooperating multipath transport or remote aggregation endpoint improve a single transfer?

Per-flow load balancing can distribute concurrent flows. It does not, by itself, add all uplink capacities to a single ordinary TCP connection. Multipath transport and tunnel aggregation require additional endpoint support and incur overhead. These distinctions guide the proposed experiments.

## What is available

- [Research proposal](docs/RESEARCH.md): questions, assumptions, hypotheses, and limits.
- [Architecture](docs/ARCHITECTURE.md): proposed components and implementation boundaries.
- [Evaluation protocol](docs/EVALUATION.md): baselines, measurements, and reproducibility requirements.
- [Roadmap](ROADMAP.md): milestones with evidence-based completion criteria.
- A dependency-free Python baseline for weighted flow allocation and an optimistic transfer-time lower bound.

## Run the baseline

Requires Python 3.10 or newer; no administrator access or network configuration changes are needed.

```sh
python -m unittest discover -s tests -v
python -m openwan.baseline
```

The example uses synthetic capacities of 20 and 10 Mbps. Its JSON output is an arithmetic illustration, not a measured benchmark or a prediction of Internet performance. See the evaluation protocol before interpreting results.

## Participate

Read [CONTRIBUTING.md](CONTRIBUTING.md). Useful contributions include critiques of assumptions, reproducible lab setups, reviewed measurement tools, and anonymized traces with provenance. Please distinguish observed results from hypotheses.

## License and project identity

MIT licensed; see [LICENSE](LICENSE). OpenWAN Research is an independent early-stage project. The name is a working research title and does not imply affiliation with other networking projects or a completed trademark review.

## Technical references

- Ford et al., [RFC 8684: TCP Extensions for Multipath Operation with Multiple Addresses](https://www.rfc-editor.org/rfc/rfc8684), 2020.
- Thaler and Hopps, [RFC 2991: Multipath Issues in Unicast and Multicast Next-Hop Selection](https://www.rfc-editor.org/rfc/rfc2991), 2000.
