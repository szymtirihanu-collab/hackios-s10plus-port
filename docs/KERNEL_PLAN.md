# Exynos 9820 kernel development plan

## Objective

Establish a reproducible ARM64 kernel build environment for the Samsung Galaxy S10+ Exynos variant (SM-G975F / beyond2lte). The initial output is a compile-test artifact only. A successful build is not evidence that it is bootable.

## Source strategy

Evaluate these source classes separately:

1. **Samsung/OEM kernel source** matching the exact SM-G975F firmware generation. This is usually the most relevant starting point for existing vendor hardware support.
2. **Community device trees and kernel trees** for beyond2lte. Record the exact branch, commit, target variant, Android/Linux base, and known limitations.
3. **Upstream Linux** support for Exynos 9820 and individual peripherals. Upstream support may be incomplete compared with the vendor kernel.

Do not mix source trees, defconfigs, device trees, or proprietary modules from different device variants without documenting and validating the differences.

## Build stages

### Stage A — source audit
- Identify the exact source repository and license.
- Verify that the tree explicitly supports SM-G975F / beyond2lte.
- Record its kernel version, toolchain expectations, defconfig, device-tree files, and required firmware/modules.
- Identify which drivers are built in and which are external modules.

### Stage B — reproducible host setup
- Record openSUSE release, architecture, compiler versions, and required packages.
- Use an ARM64 cross-compiler appropriate to the selected source tree.
- Keep build outputs outside the source tree where possible.
- Save the exact build command and environment metadata.

### Stage C — compile-only validation
- Generate the documented defconfig.
- Run the kernel configuration and build.
- Preserve compiler output and configuration.
- Check that expected kernel and DTB artifacts were produced.
- Do not call these artifacts flashable until their image packaging and device boot requirements are verified.

### Stage D — hardware bring-up investigation
Priority order:
1. Display panel and display controller.
2. Touchscreen and input devices.
3. USB host / OTG and keyboard/mouse.
4. Internal storage and filesystem.
5. Charging, battery, thermal sensors, and power management.
6. Audio, cameras, radios, suspend/resume.
7. USB-C external display, only if the exact hardware route is supported.

## Required build record

Every build should record:
- Source URL and commit SHA.
- Kernel version and config/defconfig.
- Cross-compiler name and version.
- Host OS and package versions.
- Build command.
- Build result and artifact hashes.
- Warnings/errors and known unsupported hardware.

## Important distinction

This is a Linux kernel development track. It does not create or replace Apple's XNU kernel and does not make iOS userspace compatible with Exynos.
