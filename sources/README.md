# Source inventory

The repositories below are external references. They are not vendored into this repository and their licenses must be reviewed before copying or modifying code.

| Source | Branch / target | Role |
|---|---|---|
| https://github.com/LineageOS/android_kernel_samsung_exynos9820 | `lineage-23.2` | Current community Exynos 9820 Android kernel reference |
| https://github.com/ExtremeXT/android_kernel_samsung_exynos9820 | `main`, `beyond2lte` build target | Device-specific kernel comparison and build-system study |
| https://github.com/ianmacd/beyond2lte | default branch to verify | Historical combined S10 kernel reference |
| https://github.com/LineageOS/lineage_wiki/blob/main/_data/devices/beyond2lte.yml | `main` | Device model, SoC, architecture, and kernel metadata |

## Rules

1. Pin exact commit SHAs before a reproducible build.
2. Keep source trees in separate directories.
3. Record licenses and preserve notices.
4. Never combine Snapdragon and Exynos source/configuration.
5. Do not copy proprietary firmware blobs into this repository without checking redistribution rights.
6. A source repository's Android build instructions do not imply it supports standalone Linux or iOS.
