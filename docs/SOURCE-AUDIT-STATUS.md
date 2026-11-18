# Upstream source audit status (0100 only)

## What is known

- The upstream project is publicly visible at https://github.com/orhunnx/beyond2lte-ios.
- Its README describes a Samsung beyond2lte / Exynos 9820 XNU port and says checkpoint 0100 is the current installed checkpoint.
- The public README contains a large historical development log. It is upstream-authored documentation, not independently verified device evidence.
- This repository does not yet contain upstream source code. The target configuration still marks source import and license verification as false.

## Audit rules

Before any source is imported, record:

1. Exact upstream repository URL and commit SHA.
2. Exact 0100 commit/tree identity and whether it is an ancestor of the selected source revision.
3. License files and per-file notices for every candidate source file.
4. A file inventory and hashes for the reviewed snapshot.
5. Any excluded changes that are newer than 0100. Never include 0101 or later.
6. A reviewer-readable report separating upstream claims, source inspection, host tests, and device observations.

## Current state

- [ ] Exact 0100 commit ancestry verified from Git objects.
- [ ] Source snapshot inventoried and hashed.
- [ ] License review completed.
- [ ] Build system discovered from source (not guessed).
- [ ] Build dependencies recorded.
- [ ] Independent review completed.

Until these checks are complete, this project remains scaffolding and must not claim to produce a bootable image.
