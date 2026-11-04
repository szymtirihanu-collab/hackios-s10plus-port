# HackiOS S10+ — Exynos 9820 Research Port

> **Status: research / bring-up planning. No bootable image or iOS port exists yet.**

Target device: **Samsung Galaxy S10+ SM-G975F (beyond2lte), Exynos 9820, ARM64**.

## What this project is

HackiOS is the working project name for investigating whether selected parts of an iOS-like environment can be recreated or studied on the S10+. The project keeps two tracks separate:

1. **Apple iOS feasibility research** — document the architectural, boot-chain, kernel, driver, and licensing barriers to running Apple's actual operating system on non-Apple hardware.
2. **Native S10+ platform bring-up** — investigate a custom ARM64 Linux kernel and device support for the Exynos 9820. This can produce a native booting research OS, but it is **not Apple's iOS**.

A newly compiled Samsung/Exynos Linux kernel does not become an iOS kernel. Kernel interfaces, drivers, boot formats, trust chains, and proprietary userspace components are different.

## Initial milestones

- [x] Establish target device and scope.
- [x] Record feasibility constraints and separate the research tracks.
- [ ] Verify exact bootloader state, firmware/build, and partition layout on the target handset.
- [ ] Audit available Samsung kernel source and device trees for SM-G975F.
- [ ] Compare vendor-kernel support with upstream Linux / postmarketOS work.
- [ ] Build a reproducible ARM64 kernel toolchain environment on openSUSE.
- [ ] Produce a kernel configuration and compile test (not yet a flashable image).
- [ ] Investigate display, USB-C, USB OTG, input, storage, and power-management bring-up.
- [ ] Only after verified boot-chain research, plan a safe test-boot procedure.

## Hardware priorities

The first practical hardware goals are:
1. Internal display and basic touch/input.
2. USB OTG keyboard and mouse.
3. USB-C display output only if the device's hardware path and available drivers support it; do not assume HDMI alt mode is available.
4. Storage, charging, thermals, and suspend/resume.

## Repository map

- `docs/FEASIBILITY.md` — what can and cannot realistically be ported.
- `docs/BOOT_CHAIN.md` — Samsung boot-chain research checklist.
- `docs/KERNEL_PLAN.md` — kernel-source and bring-up plan.
- `docs/DEVICE_NOTES.md` — target-specific facts to verify.
- `scripts/host-check.sh` — read-only host environment check for openSUSE/Linux.

## Safety and device integrity

Do not flash an unverified image, overwrite bootloader partitions, or change partition tables as an experiment. Keep a known-good stock firmware package and a recovery path before any device-side test. This repository currently contains documentation and checks only; it does not contain a working kernel, boot image, or installer.

## Naming

“HackiOS” is an independent research project name. It is not affiliated with Apple and does not contain Apple's iOS firmware or source code.
