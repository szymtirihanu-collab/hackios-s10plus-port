# Existing beyond2lte XNU project — independent reference audit

Audit date: 2026-11-04
Repository inspected: https://github.com/orhunnx/beyond2lte-ios
Pinned revision: `9c6bae4dab4345ff537b1fc2c9de90ae01362c4b`

## Why this matters

This repository is already specific to Samsung Galaxy S10+ SM-G975F (`beyond2lte`) with Exynos 9820. It is much closer to this project's hardware target than the Qualcomm-only reference device in upstream HakiOS. Its README reports physical-device XNU startup, iOS userspace startup and SpringBoard appearing on the device.

Those are project-maintainer claims and device observations recorded in its own documentation. They have not been independently reproduced by this repository. The project has no GitHub Actions workflows or visible Actions runs at the audited revision, so its documented local test/build results should not be treated as independently verified CI results.

## What the repository reports

- A Samsung S-Boot → BootShim → beyond2lte UEFI → embedded XnuLoader → XNU boot path.
- An XNU board overlay targeting the Exynos 9820.
- A CPU framebuffer path that copies rendered surfaces to the firmware-provided display; GPU acceleration is explicitly not implemented.
- Direct UFS storage support and an HFS root filesystem rather than native iOS APFS.
- ARM64e userspace support that is partial and includes instruction compatibility work because the target does not provide the same hardware features as an Apple SoC.
- A real SpringBoard process/UI has appeared, but the latest recorded checkpoint still has rendering errors and a SpringBoard assertion. Settings opening was reported at checkpoint 0099; checkpoint 0100 verifies a UIKit D94 touch-profile selection, not a complete UI fix.
- Touch is reported as partially working. Application migration is blocked by HFS/APFS assumptions. Mali GPU acceleration is not implemented. Apple services are not a supported goal.

The project therefore provides evidence that a real XNU/iOS-userspace experiment on this exact device may be technically possible. It does **not** demonstrate a complete or stable iOS port, and its latest recorded status is not a fully working SpringBoard experience.

## Build and trust limitations

- The repository has no top-level `LICENSE`, `COPYING` or `NOTICE` file at the audited revision. Do not copy or vendor its code into this project unless the owner clarifies the applicable license and permissions.
- The README and build notes report device-side installation and BOOT readback, but those reports are not independently verifiable from this repository's GitHub Actions because no workflow is present.
- The project describes development-only security compatibility behavior and an altered software product identity. It should not be treated as a production iOS security environment or as an unmodified Apple platform.
- The project has extensive local build artifacts excluded from Git; public source alone does not reproduce every claimed installed checkpoint without the specified external dependencies and local inputs.

## Comparison with upstream HakiOS

| Project | Hardware | What it contributes | Limitation for this target |
|---|---|---|---|
| `oosexgang/hakios-xnu-kernel` | Qualcomm SC7280 reference phone plus QEMU | Shared XNU port, loader, userland tools, documented architecture and CI-style source checks | Its documented phone port is Qualcomm; Exynos 9820 is not a supported device |
| `orhunnx/beyond2lte-ios` | Exact SM-G975F / Exynos 9820 | Existing board overlay, loader/boot-contract research and reported physical XNU + SpringBoard progress | No repository license found; runtime claims are maintainer-reported; latest UI remains incomplete |
| This repository | SM-G975F / Exynos 9820 | Own project coordination, source audits, reproducible build records and independently authored work | No Exynos XNU device profile or validated XNU boot yet |

## Engineering decision

Use the beyond2lte-ios repository as a read-only technical reference while continuing to use the licensed upstream HakiOS source as the general architecture reference. Do not copy its code, patches, build scripts, boot images or device-specific instructions without an explicit license grant. Reproduce claims from source-level evidence and safe host-side tests before considering any device-side work.

The immediate useful target is no longer to invent an Exynos boot architecture from zero. It is to compare the public boot contract, XNU revision, board configuration, display/input interfaces and storage assumptions against the licensed upstream HakiOS design, then implement independently authored, license-clean components with tests.

## Acceptance standard

A SpringBoard milestone requires the real SpringBoard process and its dependent services to start on the target with usable display and touch, with no reliance on an Android launcher or visual mock. A successful kernel compile, a boot logo, or a single SpringBoard screenshot is insufficient to claim a functional port.
