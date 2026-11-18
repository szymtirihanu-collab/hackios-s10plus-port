# OpenCode instructions — HackiOS S10+ (0100 only)

## Scope
- Target: Samsung SM-G975F / beyond2lte / Exynos 9820, ARM64.
- Baseline: upstream checkpoint 0100 only.
- Never import 0101 or later commits, fixes, or artifacts.
- Treat the current repository as a documentation/scaffolding project until upstream source provenance and licensing are verified.

## Workflow
1. Read README.md and docs/BASELINE-0100.md, docs/KNOWN-ISSUES-0100.md, docs/WORKPLAN.md.
2. Verify upstream repository, exact 0100 source commit/tree, and license before fetching/copying code.
3. Do not guess build inputs, partition layouts, image offsets, device-tree values, boot formats, signing requirements, or filenames. Confirm each from source or device-specific documentation and cite it in notes.
4. Start with host-only inspection and reproducible tests. Make the smallest change, add a test, run it, and report exact results.
5. Never claim an image is bootable or device-tested unless evidence exists.
6. Keep generated images, firmware, dumps, private logs, and identifiers out of Git; use build/ (ignored) and artifact manifests with hashes.

## Device boundary
- Do not run device flashing, partition writes, formatting, repartitioning, bootloader unlock, or recovery commands.
- Do not add scripts that perform device writes or automate flashing.
- Build and validation scripts must be host-only and non-destructive.
- Ask the owner to have a knowledgeable adult review device-side testing and recovery plans.

## Deliverables
- Maintain source provenance, toolchain/version record, build log, test results, artifact sizes and SHA-256 hashes.
- Build outputs are untrusted until validated and reviewed.
- If the actual upstream source or build system is unavailable, stop and document the blocker instead of inventing a boot image.
