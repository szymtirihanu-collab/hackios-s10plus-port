# HackiOS S10+ — Exynos 9820 Research Port

> **Status: research / kernel-source audit. No bootable HackiOS image or iOS port exists yet.**

Target device: **Samsung Galaxy S10+ SM-G975F (beyond2lte), Exynos 9820, ARM64**.

## Project direction

The intended end goal is Apple's actual Darwin/iOS environment on the S10+, including the real SpringBoard and its required system services—not an Android launcher, visual imitation, or Linux-based substitute.

The project has two distinct engineering tracks:

1. **XNU / iOS compatibility research** — investigate the upstream HakiOS XNU port, its loader, device profiles, drivers and iOS userspace requirements, then determine what must be implemented for Exynos 9820.
2. **S10+ Linux kernel compile research** — maintain a reproducible Linux kernel build only as a separate source/hardware reference. It is not an iOS kernel and is not a substitute for XNU.

A successful Linux kernel compile does not advance the project to a bootable iOS image. See the [upstream HakiOS audit](docs/UPSTREAM_HAKIOS_AUDIT.md) and [Exynos XNU port plan](docs/EXYNOS_XNU_PORT_PLAN.md) for the current architecture and hardware bring-up gates.

## Current target and scope

- Device: Samsung Galaxy S10+ **SM-G975F**
- Codename: **beyond2lte**
- SoC: **Exynos 9820**
- Architecture: **ARM64 / AArch64**
- Actual iOS track: upstream HakiOS XNU architecture, with a new Exynos device/SoC port required.
- Separate Linux baseline: Samsung Exynos 9820 vendor kernel, for compile and hardware-source research only.
- This project does **not** inherit requirements from the separate Android 16 port project.

## Milestones

- [x] Establish target device and actual-iOS goal.
- [x] Identify and inspect the upstream HakiOS XNU project.
- [x] Document the initial Exynos 9820 versus Qualcomm reference-platform gaps.
- [x] Identify public Exynos 9820 Linux kernel-source candidates for separate hardware research.
- [x] Audit upstream HakiOS build structure, device manifest, loader flow and SoC requirements at source level.
- [x] Pin an upstream HakiOS revision and add CI checks for its source/configuration integrity.
- [ ] Establish whether a viable Exynos-specific UEFI/boot path can be built and tested.
- [ ] Define an Exynos XNU device profile and identify the minimum required drivers.
- [ ] Demonstrate XNU early boot on the target platform.
- [ ] Bring up display and touch, then required iOS userspace services and actual SpringBoard.

A one-month effort is a time-box for research and bring-up, not a promise that SpringBoard will be working by the deadline.

## Repository map

- `docs/UPSTREAM_HAKIOS_AUDIT.md` — pinned upstream project inspection and Exynos gap analysis.
- `docs/EXYNOS_XNU_PORT_PLAN.md` — subsystem-by-subsystem XNU bring-up plan and acceptance gates.
- `docs/BUILD_STATUS.md` — separate Linux kernel compile experiment and CI status.
- `docs/FEASIBILITY.md` — overall iOS-on-Exynos feasibility.
- `docs/XNU_PORT_GAP.md` — platform components a kernel alone cannot provide.
- `docs/BOOT_CHAIN.md` — Samsung boot-chain research checklist.
- `docs/KERNEL_PLAN.md` — Linux kernel research process.
- `docs/KERNEL_SOURCE_AUDIT.md` — known public Exynos source candidates and limitations.
- `docs/DEVICE_NOTES.md` — target-specific facts to verify.
- `docs/DEVICE_TREE_AUDIT.md` — inspected S10+ device-tree evidence.
- `sources/README.md` — source selection policy.
- `scripts/host-check.sh` — read-only host environment check.
- `scripts/check-kernel-tree.sh` — read-only source-tree sanity check.

## Device integrity

No unverified image should be flashed and no bootloader or partition-table changes should be attempted as an experiment. Keep a known-good stock firmware package and a recovery path before any device-side test. A successful compile does not prove that an image is bootable.

## Naming

“HackiOS” is an independent research project name. It is not affiliated with Apple and does not contain Apple's iOS firmware or source code.
