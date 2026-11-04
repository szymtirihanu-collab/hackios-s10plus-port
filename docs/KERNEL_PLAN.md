# Exynos 9820 kernel development plan

## Objective

Establish a reproducible ARM64 kernel build environment for the Samsung Galaxy S10+ Exynos variant (SM-G975F / beyond2lte). The initial output is a compile-test artifact only. A successful build is not evidence that it is bootable, and a Linux kernel build is not an iOS port.

## Source strategy

Evaluate these source classes separately:

1. **LineageOS Exynos 9820 kernel** — a maintained community kernel tree whose `lineage-23.2` branch is associated with the S10+ Android 16 device support. Use it as a reference for the current device kernel baseline, not as an iOS kernel.
2. **ExtremeXT Exynos 9820 kernel** — explicitly lists G975F / beyond2lte and documents a device-specific build target. Its build system is Android/vendor-kernel oriented and packages Android kernel output; do not treat its generated package as a HackiOS image.
3. **OEM/Samsung kernel sources** matching the exact firmware generation.
4. **Upstream Linux** support for Exynos 9820 and individual peripherals. Upstream support may differ substantially from the vendor kernel.

Do not mix source trees, defconfigs, device trees, or proprietary modules from different device variants without documenting and validating the differences.

## Build stages

### Stage A — source audit
- Identify the exact source repository, branch, commit, and license.
- Verify that the tree explicitly supports SM-G975F / beyond2lte.
- Record its kernel version, toolchain expectations, defconfig, device-tree files, and required firmware/modules.
- Identify which drivers are built in and which are external modules.
- Confirm whether the tree targets Android vendor interfaces or a standalone Linux userspace.

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

### Stage D — platform interface research
- Compare the Linux kernel's exported interfaces with the XNU and Apple platform requirements documented in `docs/XNU_PORT_GAP.md`.
- Do not assume Linux drivers can be linked into XNU.
- Identify which functionality would require a clean-room implementation or a separate compatibility layer.
- Keep all results labelled as Linux-kernel research unless an actual XNU-compatible implementation is demonstrated.

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

The custom kernel track is for understanding and bringing up Exynos 9820 hardware. It does not create or replace Apple's XNU kernel and does not make iOS userspace compatible with Exynos.
