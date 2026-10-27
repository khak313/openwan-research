# Roadmap

All networking milestones remain planned; dates are intentionally not promised.

- [x] Document scope and distinguish balancing, failover, and aggregation.
- [x] Provide a deterministic analytical baseline and invariant tests.
- [ ] M1: Build an isolated Linux namespace topology with documented cleanup and no host-route changes. Done when another contributor can reproduce reachability and shaping checks.
- [ ] M2: Implement link observations and flow-affinity policies. Done when fault-injection tests cover loss, complete outage, and intermittent recovery.
- [ ] M3: Evaluate endpoint-assisted aggregation. Done when transport version, remote bottleneck checks, and overhead accounting are reproducible.
- [ ] M4: Run the frozen evaluation protocol and publish raw data, analysis, and negative results.
- [ ] M5: Seek independent replication, address peer feedback, and define supported deployment boundaries.
