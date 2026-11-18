# Work plan — 0100 only

## Phase 0: establish provenance (current)

- [x] Record upstream checkpoint commit and 0100 scope.
- [x] Record 0100's documented device-tree change and runtime result.
- [x] Explicitly exclude 0101 and later.
- [ ] Obtain the exact 0100 source tree/artifact provenance and license.
- [ ] Compare this user's installed image hash with the upstream 0100 hash, if available.

## Phase 1: reproduce on the host

- [ ] Identify the exact upstream commit/tree that corresponds to the 0100 source baseline.
- [ ] Fetch source only after confirming licensing and repository layout.
- [ ] Reproduce documented host tests without a connected phone.
- [ ] Record toolchain versions, commands, outputs, and artifact hashes.

## Phase 2: diagnose the stalled boot

- [ ] Collect existing logs read-only.
- [ ] Identify the last successful boot stage.
- [ ] Correlate kernel, launchd, dyld, backboardd, and SpringBoard events where present.
- [ ] Form one falsifiable hypothesis at a time.

## Phase 3: fix only a demonstrated 0100 defect

- [ ] Make the smallest isolated patch.
- [ ] Add a regression test before changing behavior.
- [ ] Run relevant tests and sanitizer checks.
- [ ] Keep the unmodified 0100 baseline reproducible.

## Device boundary

No automatic flashing, partition writes, formatting, or destructive recovery actions. Any future device test must be separately approved by the device owner after backup and recovery readiness are verified.
