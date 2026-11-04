# Samsung S10+ boot-chain research

Target: SM-G975F / beyond2lte / Exynos 9820.

This document is a checklist, not a flashing guide. Exact behavior depends on the handset's bootloader revision, firmware, lock state, and regional variant.

## Information to collect

- Exact model string from Settings and download mode.
- Current Android build number and baseband/bootloader revision.
- Whether OEM unlocking is available and the current bootloader lock state.
- Whether the device has a custom recovery already installed.
- Partition map and image format information from trusted device-specific sources.
- The exact stock firmware package matching the device and bootloader revision.

Do not publish serial numbers, IMEIs, account identifiers, or other device-unique secrets in this repository.

## Questions to answer from reliable sources

1. Which boot stages are used on this Exynos S10+ variant?
2. Which image formats and headers are expected at each relevant stage?
3. Which partitions are verified, and what does the device's current lock state permit?
4. Is there a documented and recoverable route for testing a non-stock kernel?
5. Which recovery method remains available if a test image fails?

## Guardrails

- Never assume instructions for the Snapdragon S10+ apply to the Exynos SM-G975F.
- Never assume instructions for another Exynos model or S10 variant apply unchanged.
- Do not flash bootloader, partition-table, modem, or other critical firmware components as an experiment.
- Do not test an image until its source, target variant, format, and recovery path have been independently checked.
