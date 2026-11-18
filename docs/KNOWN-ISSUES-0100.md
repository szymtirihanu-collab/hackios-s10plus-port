# Known issues at checkpoint 0100

This list is limited to issues explicitly documented by the upstream 0100 build/runtime notes.

## 1. SpringBoard / rendering

Runtime findings report:
- 48 invalid image colorspace NULL messages.
- 328 invalid context messages.
- A recurring SpringBoard assertion: `_bs_assert_object != nil`.
- No successful sustained icon/backdrop rendering checkpoint.

The counts cover a particular capture interval and must not be treated as a measured regression rate. The logs do not establish the root cause.

## 2. Native application migration

The upstream findings say the prior 0099 migration attempt was rejected by the native installer because HFS staging was unsupported (MIStagingManager error 166). Zero application bundles were installed.

Build 0100 did not retry migration; the retained receipt belongs to the earlier attempt. Do not clear the receipt or initiate another migration as part of baseline reproduction.

## 3. Cache publisher mismatch

The 0100 findings describe a publisher idempotence issue: the owned helper executable had 34 four-byte words rewritten by the native instruction-cache conversion, while the publisher incorrectly required the existing helper to remain byte-identical.

The upstream 0101 fix for this issue is **out of scope**. Do not copy it into this 0100 baseline.

## 4. Boot-to-UI stall on this user's device

The user reports that their first boot attempt remained at the Apple logo for approximately 10 hours. This is user-reported evidence, not a decoded log or a confirmed 0100 runtime result. The exact installed image/build and device log still need confirmation before attributing the stall to a subsystem.

## Evidence needed next

- Exact image provenance and SHA-256 of the image currently on the device.
- Read-only kernel and userspace logs from the stalled boot.
- Whether the device reboots, remains static, or changes backlight state.
- A mapping from the final recorded boot events to the relevant startup stage.

Do not flash or modify partitions to obtain this evidence.
