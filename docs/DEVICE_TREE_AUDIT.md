# Device-tree audit — beyond2lte

## Confirmed source evidence

Repository: https://github.com/LineageOS/android_kernel_samsung_exynos9820

Branch: `lineage-23.2`

Inspected source revision: `a412cfaf86b980ce35cae96a35f678c8ea551575`

Inspected file:
`arch/arm64/boot/dts/samsung/exynos9820-beyond2lte_eur_open_23.dts`

The file:
- identifies itself as a Samsung Exynos 9820 board device-tree source;
- includes Exynos 9820 sensor-hub and display definitions;
- includes beyond2lte-specific common, fingerprint, GPIO, optics, motor, and PMIC data;
- declares compatible strings for the BEYOND2LTE EUR OPEN 23 board and EXYNOS9820.

This is direct evidence that the kernel source tree contains S10+ / Exynos 9820 board-specific device-tree material. It is **not** proof that the tree boots on every SM-G975F hardware revision or that it can boot a non-Android OS.

## Hardware revision caveat

The inspected file is explicitly for the EUR OPEN 23 hardware revision. The target handset's board revision and matching DTB/DTBO selection still need to be verified. Do not substitute this file blindly for another board revision.

## Next audit tasks

- Identify the exact DTB/DTBO selected by the S10+ build configuration.
- Map the device's installed firmware and hardware revision to the correct device-tree variant.
- Record the relevant panel, touch, storage, power, and peripheral nodes.
- Compare the selected DTB with the actual boot image packaging requirements.

## Reference

https://github.com/LineageOS/android_kernel_samsung_exynos9820/blob/a412cfaf86b980ce35cae96a35f678c8ea551575/arch/arm64/boot/dts/samsung/exynos9820-beyond2lte_eur_open_23.dts
