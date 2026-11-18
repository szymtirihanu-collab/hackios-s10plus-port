# Baseline lock: upstream build 0100

## Provenance

- Upstream: https://github.com/orhunnx/beyond2lte-ios
- Checkpoint commit: `53abba664c46231ceb6b0a21c0825e154da61309`
- Commit message describes preserving tested progress through 0100 and explicitly says 0101 is built but not installed.
- Upstream README says installed checkpoint is 0100.

**Rule:** this project is based on 0100. Do not import 0101 changes or later commits into the baseline.

## 0100 change

Build 0100 adds root device-tree property `target-type="D94"` alongside model `iPhone17,2`. The upstream build note says this matches the source image's device tree and the existing `D94.Default.plist` / `D94.Touch.plist` resources, allowing UIKit to select the correct event timing profiles.

The upstream build note reports:
- Device-tree regression checks for one root property and NUL-terminated D94 value.
- Capacity, topology and ABI tests passed under ASan/UBSan.
- EFI loader and embedded 4 MiB firmware compiled.
- Packaging verified that the newly built loader was embedded.
- Kernel byte-identical to 0099.

## Installation evidence reported upstream

The upstream note reports a BOOT-only installation from root recovery after product, BOOT alias and capacity verification, a full 57,671,680-byte BOOT backup, and a previous-0099 prefix check. It reports exact readback SHA-256:

`8fa0af6c3d76b56dd62331e1889bff24f8d866c5aa77398940989c8e4d713e05`

It also reports reboot returned successfully. This is upstream-reported evidence, not an independent verification by this repository.

## Runtime evidence reported upstream

The 0100 runtime findings report that SpringBoard and UIKit clients selected:

`/System/Library/EventTimingProfiles/D94.Touch.plist`

They also report no default event timing warning in the decoded boot.

The same runtime findings report 48 `invalid image colorspace: NULL` messages, 328 invalid-context messages, and a SpringBoard assertion:

`Invalid condition not satisfying: _bs_assert_object != nil`

Framebuffer copies reportedly had no sampled unsupported-format/bounds failures.

## Explicit exclusions

Build 0101's publisher comparison fix is excluded. Upstream says it was compiled and tested but not installed. This repository must not silently incorporate it or imply it is part of 0100.
