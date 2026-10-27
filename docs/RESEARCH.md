# Research proposal

## Abstract

OpenWAN Research proposes a controlled evaluation of heterogeneous multi-WAN connectivity. The study separates independent-flow distribution, failure recovery, and single-transfer aggregation. The initial artifact provides an analytical baseline and a prospective methodology. Empirical validation remains future work.

## 1. Problem statement

Multiple access links provide distinct capacities and failure modes. Their combined advertised bandwidth is not necessarily available to one application connection. Scheduling, congestion control, shared bottlenecks, address translation, remote endpoint capacity, and path asymmetry may limit useful performance.

## 2. Research questions

- RQ1: When does capacity-weighted flow placement reduce completion time relative to equal flow counts?
- RQ2: How do probe interval, failure threshold, and recovery hysteresis affect interruption and route oscillation?
- RQ3: When does endpoint-assisted aggregation outperform the fastest single link after accounting for tunnel overhead, reordering, and remote bottlenecks?

## 3. Assumptions and notation

Link i has available capacity c_i(t), round-trip delay r_i(t), loss probability p_i(t), and optional usage cost k_i. Capacity observations are estimates rather than guaranteed service rates. Failures may be correlated. A remote endpoint, when used, must be reachable through each tested uplink and have measured spare capacity.

For payload B bits, the idealized lower bound T >= B / sum(c_i) assumes independent links, perfect striping, no overhead, and no downstream bottleneck. For an unmodified single-path transfer, the analogous optimistic bound is B / max(c_i). Neither expression models congestion control or constitutes a performance result.

## 4. Hypotheses to test

| ID | Hypothesis | Evidence that would challenge it |
| --- | --- | --- |
| H1 | Capacity-weighted placement improves batch completion for many similarly sized flows on stable unequal links. | No improvement, or worse tail latency, against equal allocation under the same workload. |
| H2 | Recovery hysteresis reduces route oscillation during intermittent faults. | Equal or higher switch count without a useful availability improvement. |
| H3 | Aggregation gains shrink as path delay asymmetry or common bottlenecks increase. | Stable gains despite controlled increases in these constraints. |

These are proposed hypotheses, not conclusions. Flow-size skew, estimation error, and application behavior may reverse H1.

## 5. Method

Begin with deterministic baseline tests. Develop an isolated Linux network-namespace testbed, then compare single-link, equal allocation, capacity-weighted allocation, and an explicitly identified endpoint-assisted transport. Introduce controlled capacity, delay, loss, outage, and recovery conditions. Follow the preregistered protocol in EVALUATION.md and publish negative as well as positive outcomes.

## 6. Validity and ethics

Synthetic models cannot establish real-world throughput or resilience. Emulation may omit cellular variability, ISP shaping, shared infrastructure, and middlebox behavior. Test only networks and endpoints under participant control. Redact public addresses and credentials; do not publish payload captures or third-party traffic without permission.

## 7. Current evidence

Only arithmetic and allocation unit tests are included. There are no completed networking experiments, field deployments, independent replications, or adoption measurements. The questions and architecture here are a proposed starting point; unavailable earlier discussion has not been reconstructed as fact.

## References

1. Ford, A., Raiciu, C., Handley, M., Bonaventure, O., and Paasch, C. RFC 8684 (2020). https://www.rfc-editor.org/rfc/rfc8684
2. Thaler, D., and Hopps, C. RFC 2991 (2000). https://www.rfc-editor.org/rfc/rfc2991
