# XNU / Apple platform compatibility gap

## Purpose

This document prevents the project from confusing a custom Exynos Linux kernel with an iOS kernel. A real iOS port would need much more than a kernel image.

## Major missing platform pieces

| Layer | Apple platform expectation | S10+ research status |
|---|---|---|
| CPU / architecture | Apple-supported ARM64 platform and boot environment | Exynos 9820 is ARM64, but architecture similarity alone is insufficient |
| Kernel | XNU with Apple-specific configuration and interfaces | Public Exynos kernel sources are Linux-based |
| Boot chain | Apple-specific boot and trust model | Samsung boot firmware and device-specific image formats |
| Device drivers | Apple platform drivers and matching hardware interfaces | Samsung/Exynos Linux drivers; not directly reusable as XNU drivers |
| Firmware / coprocessors | Apple platform firmware and service interfaces | Samsung/Exynos-specific firmware and peripherals |
| Userspace | iOS system frameworks, services, libraries, and signing model | Not available as a compatible Exynos distribution |
| Updates / recovery | Apple-specific restore and update infrastructure | Samsung-specific maintenance and recovery path |

## What can be done in this repository

- Study public ARM64 and XNU architectural documentation at a high level.
- Document differences between XNU and the available Exynos Linux kernel.
- Build and inspect a device-specific Linux kernel as a separate hardware research track.
- Recreate independent, open components where licenses permit.
- Build a clearly labelled experimental OS environment without claiming it is Apple's iOS.

## What a custom kernel can and cannot do

A custom Exynos Linux kernel can potentially improve or alter Linux hardware support for this device. It cannot, by itself:
- turn Linux into XNU;
- provide Apple-specific kernel APIs;
- supply proprietary Apple drivers or firmware;
- satisfy Apple's boot verification and system signing requirements;
- make iOS system frameworks run on Samsung hardware.

## Evidence standard

Do not mark any iOS compatibility milestone complete based only on:
- a successful Linux kernel compilation;
- a booting Linux image;
- an iOS-like user interface;
- an emulator or mock interface.

A milestone must identify the exact Apple component being implemented, its interface, the source/license basis, and a reproducible test proving compatibility.
