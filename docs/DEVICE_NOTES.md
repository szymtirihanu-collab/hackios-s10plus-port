# Target device notes

## Confirmed project target

| Field | Value |
|---|---|
| Device | Samsung Galaxy S10+ |
| Model | SM-G975F |
| Device codename | beyond2lte |
| SoC | Samsung Exynos 9820 |
| CPU architecture | ARM64 / AArch64 |

## Must be verified on the actual handset

- Exact Android firmware and bootloader revision.
- Bootloader unlock status.
- Available recovery options.
- Panel/touch hardware revision.
- USB-C display capabilities on this exact model.
- Current partition layout and image packaging requirements.

## First-use goals

- Internal display.
- USB OTG keyboard and mouse.
- Basic boot diagnostics and serial/log capture if supported.
- External display over USB-C is a research item, not a guaranteed feature.

## Variant warning

The S10+ family includes different SoCs and regional models. This repository targets the Exynos SM-G975F only. Snapdragon models and other S10 variants are out of scope unless explicitly added and separately validated.
