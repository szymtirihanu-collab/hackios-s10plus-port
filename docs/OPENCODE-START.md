# OpenCode next tasks — 0100 only

Read `AGENTS.md`, `docs/BASELINE-0100.md`, `docs/SOURCE-AUDIT-STATUS.md`, and `docs/BUILD-PIPELINE.md` first.

## Priority

1. Inspect public upstream documentation and source metadata without importing code yet.
2. Verify the 0100 checkpoint's exact Git object and ancestry. Do not use 0101 or later.
3. Record license notices and source provenance in a concise audit report.
4. Run host-only tests and the toolchain probe. Do not install packages or alter the host.
5. Identify documented build-system requirements, but do not invent commands or image formats.
6. Make small, reviewable changes and add host tests for them.

## Report format

For every task, distinguish:
- verified from repository/Git metadata;
- stated by upstream documentation;
- tested locally;
- not yet checked.

Do not report a bootable output, device test, or successful port unless that result is actually observed and recorded. Device installation and destructive device actions are outside this task.
