# Proposed architecture

## Boundary

The implemented Python module is an offline analytical utility. All networking components below are proposed and unimplemented.

## Components and data flow

1. Link observer: collect timestamped reachability, delay, loss, and capacity estimates with explicit probe targets and timeouts.
2. Policy engine: select links for new flows using health, weight, cost, and flow requirements.
3. Routing adapter: apply Linux policy routes in an isolated testbed; preserve flow affinity where feasible.
4. Optional aggregation adapter: communicate with a cooperating remote endpoint using an identified transport; account for encapsulation and resequencing overhead.
5. Measurement collector: record application completion times, link counters, policy decisions, and failure timestamps using a consistent clock.

## Design constraints

- Health state should include unknown, healthy, degraded, and unavailable rather than infer Internet health from carrier alone.
- Existing sessions may fail after a public source address changes. Session preservation is not guaranteed by rerouting.
- Remote aggregation adds operational cost and a trust boundary; transport authentication and encryption require review before deployment.
- Probe traffic, retry limits, route rollback, and resource use must be bounded.
- Never modify the host default route automatically in the initial experimental tooling.

## Initial baseline contract

`allocate_flows(count, capacities)` returns nonnegative integer counts summing to count, proportional to capacities using largest remainders. Equal remainders favor earlier input links. Zero-capacity links receive no flows. This is a count allocation for equal-sized independent flows; it is not a packet scheduler or a capacity estimator.

`ideal_transfer_seconds(size_bytes, capacities)` returns an optimistic arithmetic lower bound for ideal striping over independent links. Capacities are Mbps, using decimal units. It does not simulate a network.
