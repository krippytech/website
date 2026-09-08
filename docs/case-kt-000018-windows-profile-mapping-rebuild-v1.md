# KT-000018 | Windows User Profile Was Rebuilt from the Correct SID Mapping

## Purpose

Create a public-safe proof-layer case showing a controlled Windows user-profile recovery where the exact SID-to-profile mapping was proven before removing only the affected ProfileList registration.

## Source basis

Sanitized KrippyTech KER: `KrippyTech_KER_Rebuild_Corrupt_Windows_User_Profile.docx`.

The source supports:

- a Windows profile could be corrupt, orphaned, temporary, or shown as Account Unknown
- `Win32_UserProfile` was used to map `LocalPath` to the affected SID
- work proceeded from a separate administrative account while the affected profile was not loaded
- `ProfileImagePath` was verified under `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`
- only the verified affected SID registration was removed
- local profile data had to be protected first if it needed to be retained
- Windows created a clean profile at the next sign-in
- normal desktop/profile loading and the new SID mapping were verified

## Locked lesson

**When a Windows profile appears broken, prove the SID-to-path mapping before deleting anything.**

## Supporting principle

**The profile display name is not the source of truth. SID, LocalPath, and ProfileImagePath are.**

## Investigation path

**Separate admin → Win32_UserProfile → SID + LocalPath → ProfileImagePath → Data protection → Remove affected registration → Clean sign-in → Verify new mapping**

## Status

**Profile Rebuilt / Normal Sign-In Verified**

## Evidence boundary

Do not claim:

- every temporary profile or Account Unknown entry has this same cause
- every profile problem requires ProfileList deletion
- an unresolved display name is enough evidence to delete a SID
- local profile data is safe to remove without first determining what must be retained
- Windows must be reinstalled for this recovery
- unrelated user, administrator, or system profile registrations should be removed

The case may state that the controlled recovery succeeded by proving the affected mapping, removing only that registration, signing the user back in, and verifying the clean profile was created successfully.

## Intent separation

- `/cases/KT-000018/` is proof of the controlled recovery
- `/everyday-it/repair-rebuild-replace-workstation/` remains the broader workstation repair/rebuild/replace decision page
- `/everyday-it/change-safety-rollback/` remains the change-safety methodology
- `/everyday-it/known-good-comparison/` remains comparison methodology
- `/everyday-it/verify-before-close/` remains verification methodology

Do not turn this case into a generic registry tutorial or a downloadable derivative.
