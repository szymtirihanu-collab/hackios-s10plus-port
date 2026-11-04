# Source inventory

The repositories below are external references. They are not vendored into this repository and their licenses must be reviewed before copying or modifying code.

| Source | Branch / target | Role |
|---|---|---|
| https://github.com/LineageOS/android_kernel_samsung_exynos9820 | `lineage-23.2` | Current community Exynos 9820 Android kernel reference |
| https://github.com/ExtremeXT/android_kernel_samsung_exynos9820 | `2f7b0aa3e501fabeaea679e3d1bde49a1e13be46` | Device-specific Linux kernel comparison and compile-only research |
| https://github.com/oosexgang/hakios-xnu-kernel | `87bf4851bcc9cbb24fd79997820aa3661abe4ea5` | Licensed upstream HakiOS architecture and generic XNU port reference |
| https://github.com/orhunnx/beyond2lte-ios | `9c6bae4dab4345ff537b1fc2c9de90ae01362c4b` | Read-only exact-device XNU/SpringBoard research reference; no license found, do not vendor or copy code |
| https://github.com/ianmacd/beyond2lte | default branch to verify | Historical combined S10 kernel reference |
| https://github.com/LineageOS/lineage_wiki/blob/main/_data/devices/beyond2lte.yml | `main` | Device model, SoC, architecture, and kernel metadata |

## Rules

1. Pin exact commit SHAs before a reproducible build.
2. Keep source trees in separate directories.
3. Record licenses and preserve notices.
4. Never combine Snapdragon and Exynos source/configuration.
5. Do not copy proprietary firmware blobs into this repository without checking redistribution rights.
6. A source repository's Android build instructions do not imply it supports standalone Linux or iOS.
