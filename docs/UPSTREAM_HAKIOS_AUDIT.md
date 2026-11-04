# Upstream HakiOS audit for Galaxy S10+ (beyond2lte)

Audit date: 2026-11-04

## Goal clarified

The target is Apple's real Darwin/iOS environment, including the real SpringBoard process and system frameworks. A launcher, Android skin, Linux desktop, or visual mock-up does not satisfy the goal.

The upstream project inspected is https://github.com/oosexgang/hakios-xnu-kernel. Its README identifies the project as a port of Apple's open-source Darwin XNU kernel (xnu-8796.121.2) to Android hardware, with its own loader, drivers, configuration and userland. It keeps Apple's iOS userspace and device firmware out of the repository; the user supplies legally obtained source-device material.

## What the upstream project actually provides

- An XNU-based kernel port, loader, common drivers, user-space components and build tools.
- A separate UEFI project and per-device repositories.
- A documented porting flow that starts from a device tree, creates a device profile, boots with minimal drivers, then brings up device drivers incrementally.
- A working reference target based on the Qualcomm SC7280 family (POCO X5 Pro / redwood).

The upstream docs/porting/index.md currently describes its starting hardware requirement as an ARM64 Qualcomm SoC with an unlocked bootloader and a UEFI port. Its example driver sequence includes Adreno GPU support and Qualcomm-oriented subsystems.

## Gap against the SM-G975F

| Area | Upstream reference | Galaxy S10+ target | Porting consequence |
|---|---|---|---|
| SoC | Qualcomm SC7280 family | Samsung Exynos 9820 | New SoC support; reference SoC code cannot be assumed compatible |
| GPU | Adreno 642L | ARM Mali-G76 MP12 | Existing Adreno path is not reusable as a Mali driver |
| Boot | HakiOS UEFI / loader path | Samsung device boot chain | A device-specific boot integration must be researched |
| Device profile | redwood profile and device tree | beyond2lte device tree | New device profile and hardware description required |
| Peripherals | Qualcomm reference drivers | Samsung/Exynos peripherals | Each driver needs evidence and device-specific implementation |
| iOS userland | User-supplied compatible iOS firmware content | No validated S10+ compatibility profile | SpringBoard cannot be considered supported until the required services/frameworks run |

ARM64 compatibility alone does not make the platforms interchangeable.

## Immediate engineering direction

1. Keep the existing LineageOS Linux kernel compile workflow labelled Linux compile-only. It is not an iOS kernel build and must not be used as evidence that XNU boots.
2. Treat upstream HakiOS as the architectural reference for the actual iOS track.
3. Audit the upstream build system, device manifest, SoC abstraction, loader interfaces and driver boundaries before creating an Exynos profile.
4. Build a source-backed Exynos gap matrix: boot/UEFI, CPU and interrupt handling, timer, memory, storage, framebuffer/display, touch/input, USB, GPU and required early userspace services.
5. Only claim a milestone after a reproducible test demonstrates that exact component on the target or in an appropriately scoped emulator.

## One-month planning boundary

A month can be used for a serious feasibility and bring-up attempt, but it is not a credible promise of a working iOS port. The first meaningful acceptance gates are: (a) a reproducible HakiOS build with an Exynos-specific configuration, (b) a documented and independently testable boot path, and (c) evidence that XNU reaches its early userspace on the target platform. A functioning SpringBoard is a later gate and depends on the kernel, display/input drivers, iOS userspace and services all working together.

No phone image should be flashed based on a compile result or an unverified configuration.