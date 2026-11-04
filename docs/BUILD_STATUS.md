# Compile status — SM-G975F / beyond2lte

## Purpose

This is a separate Linux hardware-source experiment. It is not the actual iOS/XNU port and a successful build does not mean HakiOS can boot.

## Current compile target

- Repository: https://github.com/ExtremeXT/android_kernel_samsung_exynos9820
- Pinned source commit: `2f7b0aa3e501fabeaea679e3d1bde49a1e13be46`
- Device defconfig: `extreme_beyond2lte_defconfig`
- Compiler: repository submodule `toolchain/clang-r416183b`
- Additional required submodule: `KernelSU` (the kernel tree's `drivers/kernelsu` symlink points into it)
- Host runner: GitHub Actions Ubuntu 22.04
- Build type: compile-only; `Image` and DTBs, if produced

## First CI result

Run 4 failed during Kconfig setup, before compilation. The exact error was:

`drivers/Kconfig:243: can't open file "drivers/kernelsu/Kconfig"`

The workflow had initialized the Clang toolchain submodule but omitted the KernelSU submodule. This was a CI checkout defect, not a compiler error and not evidence that the kernel itself cannot compile.

## Fix applied

Commit `8bb4564ac13ef69f41e011c51a506db0702ed9fe` changes the checkout step to initialize all pinned submodules recursively and explicitly checks that `drivers/kernelsu/Kconfig` resolves. The follow-up workflow run is tracked on the repository Actions page; the compile is not marked successful until the run finishes and produces outputs.

## Automation and outputs

`.github/workflows/kernel-compile.yml` verifies the source SHA, configures the device defconfig, and attempts to compile `Image` and DTBs. On success it uploads the build record, kernel config, image, DTBs and checksum as a short-lived artifact.

The workflow does not create a flashable package, alter a boot image, or write anything to a phone.

## Status

- [x] Pin a G975F-specific Linux kernel source revision.
- [x] Add a CI compile-only workflow.
- [x] Diagnose and fix the missing KernelSU submodule checkout.
- [ ] Complete a CI compile successfully.
- [ ] Review compiler warnings and resulting DTB coverage.

## Device integrity

Do not flash this compile artifact. It has not been validated against the device's boot chain, firmware, partition layout, or recovery procedure. Keep device-side work separate from this compile-only stage.
