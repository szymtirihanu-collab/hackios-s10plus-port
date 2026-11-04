# HackiOS S10+ — Exynos 9820 Research Port

> **Status: research / kernel-source audit. No bootable HackiOS image or iOS port exists yet.**

Target device: **Samsung Galaxy S10+ SM-G975F (beyond2lte), Exynos 9820, ARM64**.

## Project direction

HackiOS investigates whether selected operating-system concepts and compatible components can be recreated for the S10+. It has two separate engineering tracks:

1. **Apple iOS compatibility research** — study the architectural, kernel, driver, firmware, boot-chain, and userspace requirements of Apple's actual operating system.
2. **S10+ custom-kernel research** — audit and compile device-specific ARM64 kernel sources for the Exynos 9820 as a hardware bring-up foundation.

A custom Samsung/Linux kernel is not an iOS kernel. Apple's XNU kernel and platform stack are not made compatible with Exynos merely by compiling a new kernel. Any native Linux kernel work is a distinct platform track and must be labelled accurately.

## Current target and scope

- Device: Samsung Galaxy S10+ **SM-G975F**
- Codename: **beyond2lte**
- SoC: **Exynos 9820**
- Architecture: **ARM64 / AArch64**
- Kernel baseline under investigation: Samsung Exynos 9820 vendor kernel, with current community-maintained source branches audited separately.
- This project does **not** inherit requirements from the separate Android 16 port project.

## Milestones

- [x] Establish target device and scope.
- [x] Record iOS/kernel feasibility constraints.
- [x] Identify public Exynos 9820 kernel-source candidates.
- [ ] Verify the phone's exact firmware and bootloader state.
- [ ] Select and pin a source tree/commit for compile-only testing.
- [ ] Reproduce a clean kernel build on openSUSE.
- [ ] Compare the compiled kernel's interfaces and hardware support with the iOS/XNU requirements map.
- [ ] Define a realistic, independently bootable HackiOS research environment, if feasible.
- [ ] Only after source, image format, and recovery requirements are verified, plan device-side testing.

## Repository map

- `docs/FEASIBILITY.md` — overall iOS-on-Exynos feasibility.
- `docs/XNU_PORT_GAP.md` — platform components a kernel alone cannot provide.
- `docs/BOOT_CHAIN.md` — Samsung boot-chain research checklist.
- `docs/KERNEL_PLAN.md` — kernel development process.
- `docs/KERNEL_SOURCE_AUDIT.md` — known public source candidates and limitations.
- `docs/DEVICE_NOTES.md` — target-specific facts to verify.
- `sources/README.md` — source selection policy.
- `scripts/host-check.sh` — read-only host environment check.
- `scripts/check-kernel-tree.sh` — read-only source-tree sanity check.

## Device integrity

No unverified image should be flashed and no bootloader or partition-table changes should be attempted as an experiment. Keep a known-good stock firmware package and a recovery path before any device-side test. A successful compile does not prove that an image is bootable.

## Naming

“HackiOS” is an independent research project name. It is not affiliated with Apple and does not contain Apple's iOS firmware or source code.
