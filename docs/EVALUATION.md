# Prospective evaluation protocol

## 1. Status and objective

No empirical results have been collected. Freeze a versioned experiment configuration before collecting confirmatory data; exploratory runs must be labeled separately.

## 2. Baselines

Compare each individual link, equal flow-count allocation, capacity-weighted flow-count allocation, and an endpoint-assisted multipath implementation identified by version and configuration. Do not compare a single transfer on one baseline with multiple concurrent transfers on another without labeling the workload difference.

## 3. Experimental factors

Start with two emulated links. Proposed capacity pairs: 20/20, 20/10, and 20/2 Mbps. Vary RTT asymmetry, loss, and bottleneck sharing in separate blocks before testing interactions. Include complete outages and intermittent faults. Record effective link shaping settings and actual observed rates. These values are planned inputs, not observations.

## 4. Workloads and metrics

Test one large transfer and batches of concurrent transfers separately. Record payload goodput, total completion time, p50/p95 flow completion time, failed transfers, interruption duration, detection delay, recovery time, route-switch count, bytes sent per link, CPU use, and tunnel overhead. Define failure and recovery timestamps in the configuration. Never infer session continuity solely from reachability probes.

## 5. Repetition and analysis

Use at least 30 independent trials per initial condition as a starting plan; revise sample size based on a documented pilot variance and target precision. Randomize condition order and record seeds. Use the trial as the sampling unit, not each packet. Report effect sizes and confidence intervals with the resampling method, raw per-trial values, and exclusion reasons. If many hypotheses are tested, declare the primary outcome and multiplicity policy in advance.

## 6. Artifact requirements

Each future result must include commit SHA, UTC time, topology, hardware or VM resources, OS/kernel and tool versions, complete configuration, seeds, raw logs, commands, analysis script, and known limitations. Include shared-bottleneck checks and remote endpoint capacity. Publish synthetic outputs separately from measured data. A blank or missing result is preferable to an invented value.

## 7. Acceptance gates

Arithmetic tests establish only baseline invariants. A networking milestone requires independently rerunnable lab instructions and logs. Any production-readiness statement requires separate operational and security review. No numerical performance target is currently claimed as achieved.
