# Upstream provenance check — checkpoint 0100

Checked against public GitHub metadata and file listings on 2026-11-18.

## Snapshot identity

- Repository: https://github.com/orhunnx/beyond2lte-ios
- Checkpoint commit: `53abba664c46231ceb6b0a21c0825e154da61309`
- Tree: `c6846becb7d9e66567090cbc4d44113898b39970`
- Parent: `1e77ae3afa690e2ae0bb8b2af3bdf9152406c83d`
- Checkpoint commit message states 0100 and explicitly notes 0101 was built but not installed.
- The immediately following commit `9c6bae4dab4345ff537b1fc2c9de90ae01362c4b` has parent 0100 and is the 0101-related work. It is excluded from this project.

The commit metadata confirms this parent relationship. Both commits are unsigned; GitHub reports verification as false. This is provenance metadata, not proof that the author or reported device results are independently authenticated.

## Repository/license status

GitHub repository metadata reports no declared license. The 0100 root listing does not include a LICENSE file. **Do not copy/vendor upstream code until licensing permission or a compatible license is established.** This repo currently contains no upstream implementation source.

## Current scope and limits

- 0100 metadata is identified by commit and tree hashes above.
- The source snapshot has not been downloaded, built, or independently reviewed here.
- Upstream README and commit messages are author claims; they are not independent device verification.
- 0101 and later commits are excluded.
- This document records Git metadata only. It is not a boot/build guide and does not authorize device modifications.

## Follow-up audit

- [x] Identify exact 0100 commit SHA and tree.
- [x] Verify 0101-related commit is a direct child of 0100.
- [x] Note unsigned commits.
- [x] Check repository license metadata and root listing.
- [ ] Establish lawful source reuse terms.
- [ ] Independent reviewer assesses the upstream claims.
