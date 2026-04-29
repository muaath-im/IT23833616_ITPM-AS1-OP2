# IT3040 Assignment 1 - Option 2 Playwright Automation

## Project Overview

This project automates one preview functionality test for the Pixelssuite website using Python Playwright. The automated scenario verifies that a valid PNG file can be uploaded to the image format conversion page and that an image preview is displayed successfully.

## Tested Website

https://www.pixelssuite.com/

## Automated Feature

Image format conversion preview functionality.

## Prerequisites

- Python 3.11 or 3.12
- Google Chrome or Playwright Chromium
- Internet connection

## Installation Steps

```bash
pip install -U pip
pip install playwright openpyxl
playwright install
```

If Windows does not recognize the `playwright` command, run Playwright through Python instead:

```bash
python -m pip install -U pip
python -m pip install playwright openpyxl
python -m playwright install
```

## Run Command

```bash
python image_preview_test.py --url "https://www.pixelssuite.com/convert-to-png" --slow-mo-ms 2000
```

For a non-visual/headless execution, use:

```bash
python image_preview_test.py --url "https://www.pixelssuite.com/convert-to-png" --slow-mo-ms 2000 --headless
```

## Expected Outputs

- `execution_results.csv` updated with one automation result row
- `results/preview_pass.png` generated when preview is detected
- `results/preview_fail.png` or `results/preview_error.png` generated if the test fails

## Project Structure

```text
test_automation_ui/
|-- image_preview_test.py
|-- sample.png
|-- execution_results.csv
|-- README.md
`-- results/
    `-- preview_pass.png
```

## Automation Scenario

| Field | Description |
|---|---|
| Test Case ID | Pos_0036 |
| Website URL | https://www.pixelssuite.com/convert-to-png |
| Input File | sample.png |
| Expected Result | Uploaded PNG image should be displayed in the preview section. |
| Evidence | Screenshot saved inside the `results` folder. |

## Notes

- The script creates `sample.png` automatically if the file is missing.
- The CSV file is rewritten by default so the assignment output contains one clear result row.
- Use `--append-results` only when multiple historical runs must be retained.
