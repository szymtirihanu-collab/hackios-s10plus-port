# Compile status — SM-G975F / beyond2lte

## Current compile target

- Repository: https://github.com/LineageOS/android_kernel_samsung_exynos9820
- Branch audited: `lineage-23.2`
- Pinned source commit: `a412cfaf86b980ce35cae96a35f678c8ea551575`
- Device defconfig: `exynos9820-beyond2lte_defconfig`
- Device-tree reference: `exynos9820-beyond2lte_eur_open_23.dts`
- Host runner: GitHub Actions Ubuntu 22.04
- Build type: compile-only; `Image` and DTBs, if produced

The source is a Linux 4.14 Android/vendor kernel. This is a reproducible hardware-kernel research baseline, not Apple's XNU, not an iOS kernel, and not a bootable HackiOS image.

## Automation

`.github/workflows/kernel-compile.yml` checks out the pinned source revision, configures the G975F-specific defconfig, and attempts to compile the kernel image and device trees. A successful run uploads a short-lived artifact containing the build outputs, config, source/compiler record, and image hash.

The workflow intentionally does not create a flashable ZIP, alter boot images, or write anything to a phone.

## Status

- [x] Select and pin a G975F-specific compile-test source revision.
- [x] Add a CI compile-only workflow.
- [ ] Complete the first CI compile successfully.
- [ ] Review compiler warnings and resulting DTB coverage.
- [ ] Compare Linux driver/interface coverage with the separate XNU feasibility analysis.

A CI failure is useful diagnostic evidence, not proof that the source is unusable. Fixes should be isolated and recorded; do not silently change the pinned source revision.

## Device safety

Do not flash the compile artifact. It has not been validated against the device's boot chain, firmware, partition layout, or recovery procedure. Keep all device-side experiments separate from this compile-only stage.
