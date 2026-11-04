# Exynos 9820 XNU port plan

Audit date: 2026-11-04
Target: Samsung Galaxy S10+ SM-G975F (`beyond2lte`, Exynos 9820)
General upstream reference: https://github.com/oosexgang/hakios-xnu-kernel\nExact-device read-only reference: https://github.com/orhunnx/beyond2lte-ios (audited at `9c6bae4dab4345ff537b1fc2c9de90ae01362c4b`; no license found, so its code is not copied)

## Goal

Run the upstream HakiOS Darwin/XNU environment on the Exynos 9820 and, eventually, run the real Darwin 16.5 iOS userspace including SpringBoard. A visual imitation or Android launcher is not a milestone.

The general HakiOS upstream currently documents Qualcomm ARM64 as its phone-port starting point. Its demonstrated device is the POCO X5 Pro 5G (`redwood`, SC7280/SM7325). A separate public repository, `orhunnx/beyond2lte-ios`, already documents an experimental XNU port on this exact S10+ model and reports that SpringBoard has appeared. Its latest recorded checkpoint still has incomplete rendering and a SpringBoard assertion, its runtime claims are maintainer-reported rather than independently reproduced here, and no repository license was found. It is a read-only research reference only; no code is copied.

## Architecture that must be brought up

The upstream boot path is:

1. Device boot firmware / a suitable UEFI or equivalent handoff.
2. HakiOS loader (`xnuloader`) receives the kernel payload, memory map and device-tree data.
3. Patched XNU starts with a minimal platform configuration.
4. SoC and device drivers are enabled incrementally.
5. Darwin userland starts; system services and graphics/input must work before SpringBoard can be considered functional.

The upstream project also has an Apple-free QEMU path (`make qemu-open`). That is useful for validating a build environment and the generic XNU port, but it does not validate Exynos hardware support.

## Hardware port gap

| Subsystem | Exynos 9820 target | Required evidence / work | Current status |
|---|---|---|---|
| SoC profile | Samsung Exynos 9820 | New SoC layer; CPU topology, physical memory map, interrupt controller, timers, power and reset interfaces | Not implemented |
| Boot handoff | Samsung S10+ boot chain | Determine supported non-destructive handoff and UEFI/loader integration; map memory and device tree correctly | Not implemented |
| Interrupts | Exynos interrupt controller / GIC | Confirm GIC version, distributor/redistributor mapping, affinity and interrupt routing | Not audited |
| SMP | Exynos 9820 CPU clusters | PSCI/secondary CPU start path and topology | Not audited |
| Timer | ARM generic timer plus SoC clocking | Verify counter frequency, timer interrupts and timebase | Not audited |
| Memory | S10+ physical RAM and reserved regions | Device-tree memory/reserved-memory parsing and safe kernel layout | Not audited |
| Display | Samsung DSI AMOLED panel / display pipeline | First milestone: loader framebuffer or a minimal display driver; later native display stack | Not implemented |
| Touch/input | Device-specific touchscreen controller | Identify exact controller and I2C/SPI/GPIO/IRQ wiring from the correct device tree | Not audited |
| Storage | UFS | Read-only storage path and firmware access; no writes during bring-up | Not implemented |
| GPU | ARM Mali-G76 MP12 | Separate Mali support; upstream reference's Adreno path is not compatible | Not implemented |
| USB | Exynos/Samsung USB controller | Enumerate USB and support diagnostic/host input where possible | Not audited |
| Power/thermal | Exynos PMU, regulators, thermal sensors | Safe clock/power/thermal visibility before enabling higher-level device features | Not audited |
| Firmware | Samsung-specific firmware and coprocessors | Inventory firmware dependencies from the exact stock device tree and firmware layout | Not audited |

No driver should be marked `works` based only on compiling. It needs a reproducible runtime test on the actual device or a properly scoped emulator.

## Immediate development sequence

### Gate A — reproducible upstream baseline

- Pin an exact upstream HakiOS commit.
- Compare its generic loader/XNU architecture with the exact-device reference's published boot contract and board notes.
- Reproduce upstream static checks and the Apple-free QEMU build on CI or a Linux host.
- Keep all upstream files under their original licenses; do not copy Apple firmware or proprietary iOS system images into this repository.
- Record the exact toolchain, build command, output hashes and test result.

Acceptance: upstream generic XNU/QEMU baseline builds and runs; this is not an Exynos boot.

### Gate B — Exynos device description

- Obtain the exact SM-G975F device tree and identify the board revision and panel/touch variants.
- Compare the Exynos device tree against the upstream loader's required device-tree contract.
- Create a new `exynos9820` SoC layer and `beyond2lte` device profile; do not reuse Qualcomm SC7280 data or Adreno driver code.
- Keep all phone-specific drivers disabled until their addresses, interrupts, clocks, rails and firmware dependencies are verified.

Acceptance: configuration and device-profile checks pass with a documented source for each hardware value. The exact-device reference may inform the gap analysis, but its unlicensed code is not reused.

### Gate C — early XNU boot

- Establish a supported, testable loader-to-kernel handoff.
- Bring up CPU, memory, interrupt controller, timer and serial/log output first.
- Boot a minimal kernel without touching persistent storage.

Acceptance: XNU reaches its early userspace/launchd with a useful boot log and a safe return path.

### Gate D — display and input

- Bring up the internal display path before attempting GPU acceleration.
- Add the touchscreen and physical buttons only after the relevant controller and interrupt data are verified.
- Treat external display over USB-C as optional research; do not assume this model supports video output over USB-C.

Acceptance: a real framebuffer is visible and input events are received on the target device.

### Gate E — Darwin userland and SpringBoard

- Validate required filesystem, process, IPC, launchd, framework and graphics dependencies.
- Use only user-supplied, lawfully obtained system material; keep proprietary images and firmware out of the public repository.
- Confirm SpringBoard and its dependent services actually launch and remain usable.

Acceptance: real SpringBoard process running on the target with working display and touch. A screenshot or UI mock is not sufficient.

## One-month time box

The month is a research sprint, not a delivery guarantee. A credible best-case sequence is to prove the upstream baseline first, then complete the Exynos profile and determine whether early XNU boot is feasible. Display/input and SpringBoard remain dependent on those gates. If early XNU boot is not achieved, the project must report that honestly rather than presenting a Linux kernel or mock UI as iOS.

## Safety and device integrity

- Do not flash unverified artifacts.
- Do not alter the partition table or boot chain as an exploratory step.
- Keep initial work to source audits, reproducible host builds, QEMU tests and read-only device information.
- Any future device test needs a separately reviewed recovery plan and verified model/firmware match.
