# IT3040 Assignment 1 - Option 2: Functional and Usability Testing of Pixelssuite Website

## 1. Title

IT3040 Assignment 1 - Option 2: Functional and Usability Testing of Pixelssuite Website

## 2. Project Overview

This project evaluates the functional correctness and usability of the Pixelssuite website. The testing work focuses on user-facing website features that support document conversion, PDF editing, image editing, image conversion, meme generation, and color selection.

The project contains 36 total test scenarios. Thirty-five scenarios are documented as manual test cases in the Excel workbook, and one positive preview scenario is automated using Python Playwright.

## 3. Objectives

1. Verify whether selected Pixelssuite features behave according to expected user actions.
2. Evaluate whether the user interface is clear, consistent, and easy to use.
3. Prepare manual test cases using positive and negative test design.
4. Automate one preview functionality scenario using a valid PNG image.
5. Record automation evidence using a CSV result file and screenshot.

## 4. Scope

Included testing activities:

- Functional testing
- Usability testing
- Manual test case design
- One Playwright automation test

Excluded testing activities:

- Backend API testing
- Performance testing
- Scalability testing
- Security testing

## 5. Website Features Under Test

1. Document conversion
2. PDF editing
3. Image resizing
4. Cropping
5. Compression
6. Image format conversion
7. Meme generation
8. Color picker
9. Image rotation
10. Image flipping

## 6. Test Scenario Distribution

| Feature | Manual Scenarios | Automated Scenarios | Total |
|---|---:|---:|---:|
| Document conversion | 4 | 0 | 4 |
| PDF editing | 4 | 0 | 4 |
| Image resizing | 4 | 0 | 4 |
| Cropping | 3 | 0 | 3 |
| Compression | 3 | 0 | 3 |
| Image format conversion | 4 | 1 | 5 |
| Meme generation | 4 | 0 | 4 |
| Color picker | 3 | 0 | 3 |
| Image rotation | 3 | 0 | 3 |
| Image flipping | 3 | 0 | 3 |
| **Total** | **35** | **1** | **36** |

## 7. Manual Test Case Design

Manual test cases are stored in `Manual_Test_Cases_IT23833616.xlsx`. The workbook uses the required assignment columns:

- TC ID
- Application Feature Tested
- Input
- Expected Output
- Actual Output
- Status
- Assumption for Expected Output

Positive test case IDs start with `Pos`, and negative test case IDs start with `Neg`.

## 8. Automation Test Design

The automated scenario uses Python Playwright to test image format conversion preview functionality.

| Field | Value |
|---|---|
| Test Case ID | Pos_0036 |
| Feature | Image format conversion preview functionality |
| URL | https://www.pixelssuite.com/convert-to-png |
| Input | `sample.png` |
| Expected Output | The uploaded PNG image is displayed in the preview section. |
| Evidence | `results/preview_pass.png` |

## 9. Implementation Steps

1. Created a structured assignment folder using the registration number `IT23833616`.
2. Prepared 35 manual test cases in Excel format.
3. Implemented one Python Playwright automation test.
4. Added a PNG input image for automation.
5. Executed the automation test against the Pixelssuite website.
6. Generated `execution_results.csv` and screenshot evidence.
7. Prepared a README file with setup and execution instructions.

## 10. Testing and Verification

The automation test was executed against `https://www.pixelssuite.com/convert-to-png`. The script uploaded `sample.png`, detected the preview area, wrote the result to `execution_results.csv`, and saved screenshot evidence in the `results` folder.

The manual workbook was checked to confirm:

- 35 manual test cases are included.
- All 10 required features are covered.
- Each feature has positive and negative scenarios.
- Expected outputs and assumptions are clear.
- Status values are recorded in the workbook.

## 11. Website Issues Identified

The following issues are related to the live Pixelssuite website behavior and are recorded as usability or functional findings:

| Issue | Affected Area | Impact |
|---|---|---|
| PDF-to-Word and Word-to-PDF pages display image-format support text such as PNG, JPG, and WEBP. | Document conversion | Users may be confused about the correct input type even though the file input accepts PDF or Word files. |
| Unsupported file uploads do not always show a clear validation message. | Upload-based tools | Users may not understand why an invalid file was not processed. |
| PDF editor feedback for invalid input can remain unclear or show a generic working state. | PDF editing | Users may not know whether the file is invalid or still processing. |

These issues are outside the automation project code because they belong to the external website under test. They are documented in the manual test cases and treated as usability findings.

## 12. Constraints and Limitations

1. The project is limited to the Pixelssuite website.
2. Only functional testing, usability testing, manual testing, and one automation test are included.
3. Backend API, performance, scalability, and security testing are outside scope.
4. Only one scenario is automated.
5. The automated scenario uses a PNG image and checks preview functionality.
6. The public GitHub repository link is provided in the separate repository link text file.

## 13. Final Folder Structure

```text
IT23833616/
|-- Manual_Test_Cases_IT23833616.xlsx
|-- execution_results_IT23833616.csv
|-- GitHub_Repository_Link_IT23833616.txt
|-- Project_Report_IT23833616.md
`-- test_automation_ui/
    |-- image_preview_test.py
    |-- sample.png
    |-- execution_results.csv
    |-- README.md
    |-- requirements.txt
    `-- results/
        `-- preview_pass.png
```

## 14. README.md Content

The README includes:

- Project overview
- Tested website URL
- Automated feature
- Prerequisites
- Installation steps
- Run command
- Expected outputs
- Project structure

## 15. Final Submission Checklist

| Item | Status |
|---|---|
| Manual Excel file includes 35 test cases | Completed |
| Automation test script is included | Completed |
| PNG input file is included | Completed |
| CSV execution result is included | Completed |
| Screenshot evidence is included | Completed |
| README is included | Completed |
| GitHub repository link placeholder is included | Completed |
| Final ZIP folder is prepared | Completed |

## Note for Submission

The final folder and files have been renamed using registration number `IT23833616`.
