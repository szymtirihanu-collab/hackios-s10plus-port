# Kernel source audit — SM-G975F / beyond2lte

This is a source inventory, not an endorsement or a claim that any tree is ready for HackiOS.

## Candidate A — LineageOS Exynos 9820 kernel

- Repository: https://github.com/LineageOS/android_kernel_samsung_exynos9820
- Branch found in repository metadata: `lineage-23.2`
- Device context: LineageOS device metadata lists the S10+ as SM-G975F / beyond2lte, Exynos 9820, ARM64, with kernel 4.14.
- Intended use here: reference the current community device kernel baseline and inspect its configuration, device tree, and driver coverage.

This is still an Android/vendor kernel tree. The Android 16 device support does not mean it can boot Apple's iOS or provide XNU interfaces.

## Candidate B — ExtremeXT Exynos 9820 kernel

- Repository: https://github.com/ExtremeXT/android_kernel_samsung_exynos9820
- Branch: `main`
- Its README explicitly lists G975F / S10+ / beyond2lte as supported.
- Its README documents cloning with submodules and selecting the model with `./build.sh -m beyond2lte`.
- Its build script selects an Exynos 9820 board configuration and an `extreme_beyond2lte_defconfig`.

Intended use here: inspect its S10+-specific configuration and compare it with the LineageOS tree. Do not blindly execute its packaging/flash workflow; this project needs a compile-only, reproducible baseline first.

## Candidate C — legacy combined S10 kernel source

- Repository: https://github.com/ianmacd/beyond2lte
- Description identifies combined kernel sources for G970F, G973F, and G975F.
- Treat as a historical reference unless its branch, toolchain, and firmware compatibility are verified.

## Selection decision

**Not selected yet.** Before choosing a baseline, compare:
- Kernel version and Android common/vendor ABI expectations.
- Exact G975F defconfig and DTB/DTBO inputs.
- Toolchain version and submodule revisions.
- Required vendor modules and firmware.
- Build reproducibility on openSUSE.
- Whether the source is suitable for a standalone Linux userspace (do not assume it is).

## Source references

- LineageOS kernel: https://github.com/LineageOS/android_kernel_samsung_exynos9820
- LineageOS S10+ device metadata: https://github.com/LineageOS/lineage_wiki/blob/main/_data/devices/beyond2lte.yml
- ExtremeXT kernel and build instructions: https://github.com/ExtremeXT/android_kernel_samsung_exynos9820
- Legacy combined kernel: https://github.com/ianmacd/beyond2lte
