# HackiOS S10+ — Build 0100 baseline

Research port for the Samsung Galaxy S10+ (SM-G975F, beyond2lte, Exynos 9820).

## Scope lock

**This repository starts from upstream checkpoint 0100 only.** Build 0101 and all later changes are out of scope and must not be merged, copied, or treated as part of this baseline.

Upstream reference: [orhunnx/beyond2lte-ios](https://github.com/orhunnx/beyond2lte-ios), source checkpoint commit `53abba664c46231ceb6b0a21c0825e154da61309`. That commit explicitly records 0100 as installed and 0101 as built but not installed.

## Verified 0100 facts

- The boot chain is Samsung S-Boot → BootShim → beyond2lte UEFI → embedded XnuLoader → XNU.
- The device has previously booted XNU and iOS userspace; SpringBoard UI has appeared on earlier checkpoints.
- Eight CPU cores have passed timer and cross-CPU interrupt checks.
- Build 0100 adds root device-tree `target-type="D94"`, matching existing UIKit D94 timing-profile resources.
- The 0100 runtime log confirms `D94.Touch.plist` selection.
- Rendering remains broken: NULL colorspace/context errors and a SpringBoard assertion are recorded.
- Native application migration remains blocked by HFS staging rejection (error 166); zero app bundles were installed in the recorded attempt.

These facts do **not** prove that this repository has been built or booted on a device. It is a research baseline.

## First engineering objective

Reproduce and inspect the exact 0100 source/build artifacts, then isolate the earliest reproducible failure after the Apple logo using read-only logs and host-side tests. Do not change multiple subsystems at once.

## Safety and device boundary

- No flashing, partition formatting, repartitioning, or destructive device operation is part of automated work.
- Preserve a known-good BOOT backup and recovery path before any separately approved device test.
- Do not claim a fix without a reproducible test and device evidence.
- Keep generated binaries, firmware, IPSWs, private logs, and device-specific identifiers out of Git.

## Repository layout

- `docs/BASELINE-0100.md`: exact checkpoint scope and provenance.
- `docs/KNOWN-ISSUES-0100.md`: evidence-backed open issues.
- `docs/WORKPLAN.md`: staged investigation plan.

## Licensing and upstream

Review the upstream repository's license and attribution requirements before copying source files. This initial commit records the baseline and does not yet vendor upstream implementation code.
