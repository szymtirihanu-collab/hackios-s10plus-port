# Build pipeline scaffolding

This repository is **not yet a boot-image build**. These host-side files are scaffolding for OpenCode while source provenance, upstream license, and the exact 0100 build system remain to be verified.

## Host-only commands

- `make preflight`: verify config and basic host tools.
- `make prepare`: create ignored workspace folders.
- `make test`: run local config tests.
- `make validate`: check a manifest once real artifacts exist.

## Artifact policy

Every produced artifact must be accompanied by:
- exact source commit and baseline (0100),
- build command and toolchain versions,
- file size and SHA-256,
- test evidence and known limitations.

Never label a placeholder or untested artifact as bootable. No device flashing, partition writes, formatting, or repartitioning are automated in this repository.
