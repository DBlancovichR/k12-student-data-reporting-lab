# Vendor Import and Export SOP

## Purpose

This SOP documents a basic workflow for exchanging student data with third-party education platforms.

## Scope

This applies to CSV imports, CSV exports, reporting extracts, and vendor file review.

## Export Procedure

1. Confirm the vendor file layout.
2. Generate the required extract from the student information system.
3. Validate required fields.
4. Remove duplicate records.
5. Confirm student IDs match the expected format.
6. Save the export file using a standard naming convention.
7. Transfer the file using the approved method.
8. Document transfer date, owner, and destination.

## Import Procedure

1. Receive file from approved vendor source.
2. Confirm file name, format, and expected columns.
3. Scan for missing required fields.
4. Validate student IDs against SIS records.
5. Load into test or staging workflow when available.
6. Review errors.
7. Document corrections.
8. Import final approved file.

## Common Issues

| Issue | Cause | Action |
|---|---|---|
| Import rejected | Missing required field | Correct source file and re-import |
| Duplicate student ID | SIS/vendor mismatch | Verify record ownership |
| Invalid grade level | Bad source value | Correct SIS value |
| Missing program status | Incomplete program record | Confirm program participation |

## Documentation Requirement

Every failed import/export should have a support ticket documenting the issue, investigation, root cause, and resolution.
