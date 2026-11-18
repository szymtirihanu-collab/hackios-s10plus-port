# Upstream source artifact — checkpoint 0100

## Status

This is a **source provenance descriptor**, not a source-code bundle and not a buildable or flashable artifact. The upstream repository does not declare a repository-level license at the pinned revision (no root LICENSE file is present). Until the copyright holder supplies a license or explicit redistribution permission, this project does not copy or redistribute upstream source files.

## Exact upstream identity

- Repository: https://github.com/orhunnx/beyond2lte-ios
- Checkpoint: `0100`
- Commit: `53abba664c46231ceb6b0a21c0825e154da61309`
- Tree: `c6846becb7d9e66567090cbc4d44113898b39970`
- Parent: `1e77ae3afa690e2ae0bb8b2af3bdf9152406c83d`
- Commit signature: unsigned / not verified
- Snapshot inventory: 493 blob files, 529 total tree entries (GitHub recursive tree response was not truncated)
- Top-level source areas: `common/`, `docs/`, `patches/`, `scripts/`, `tests/`, `tools/`, `uefi/`, `userspace/`, `xnu-overlay/`

## Strict checkpoint boundary

The next upstream commit is checkpoint 0101 (`9c6bae4dab4345ff537b1fc2c9de90ae01362c4b`). It is intentionally excluded. Do not resolve a moving branch name such as `main` when interpreting this artifact; only the immutable 0100 commit above defines the baseline.

## OpenCode instructions

1. Treat this file and `source-artifact-0100.json` as provenance metadata only.
2. Do not claim that upstream source files are present in this repository.
3. Do not import, mirror, patch, build, package, or redistribute upstream code until its applicable license or written permission is verified.
4. Keep all project work host-side and read-only with respect to physical devices. Do not generate device-write or flashing steps.
5. Keep 0101 and all later checkpoints out of the 0100 baseline.

## Verification limits

GitHub metadata confirms the commit, tree, parent and unsigned status. It does not prove the upstream author's runtime claims, code correctness, or hardware compatibility. No source build or device test is represented by this descriptor.
