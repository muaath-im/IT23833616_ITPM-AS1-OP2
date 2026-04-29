from playwright.sync_api import sync_playwright
from pathlib import Path
import argparse
import base64
import time
import sys
import csv
from datetime import datetime


DEFAULT_URL = "https://www.pixelssuite.com/convert-to-png"
DEFAULT_TIMEOUT_MS = 60000
DEFAULT_SLOW_MO_MS = 0
TEST_CASE_ID = "Pos_0036"
FEATURE_NAME = "Image format conversion preview functionality"

PNG_1X1_BASE64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMB/6X9wYQAAAAASUVORK5CYII="
)


def configure_stdout():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    except Exception:
        pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--png", default="sample.png")
    parser.add_argument("--out-dir", default="results")
    parser.add_argument("--csv", default="execution_results.csv")
    parser.add_argument("--headless", action="store_true", default=False)
    parser.add_argument("--append-results", action="store_true", default=False)
    parser.add_argument("--timeout-ms", type=int, default=DEFAULT_TIMEOUT_MS)
    parser.add_argument("--slow-mo-ms", type=int, default=DEFAULT_SLOW_MO_MS)
    return parser.parse_args()


def create_default_png_if_missing(file_path: Path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if not file_path.exists():
        file_path.write_bytes(base64.b64decode(PNG_1X1_BASE64))


def find_file_input(page, timeout_ms: int):
    deadline = time.time() + (timeout_ms / 1000)

    while time.time() < deadline:
        try:
            locator = page.locator('input[type="file"]').first
            if locator.count() > 0:
                return locator
        except Exception:
            pass
        page.wait_for_timeout(300)

    raise RuntimeError("File upload input was not found.")


def check_preview_visible(page):
    script = """
    () => {
        const visible = (el) => !!(el && el.getClientRects && el.getClientRects().length);

        const previewLabels = Array.from(document.querySelectorAll("body *"))
            .filter(el => el.childElementCount === 0)
            .filter(el => (el.textContent || "").trim().toLowerCase().includes("preview"))
            .filter(el => visible(el));

        for (const label of previewLabels) {
            let parent = label;
            for (let i = 0; i < 6 && parent; i++) {
                const media = Array.from(parent.querySelectorAll("img, canvas, svg, video"))
                    .filter(el => visible(el));
                if (media.length > 0) {
                    return true;
                }
                parent = parent.parentElement;
            }
        }

        return false;
    }
    """
    return page.evaluate(script)


def write_result_to_csv(csv_path: Path, row: dict, append_results: bool):
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "test_case_id",
        "feature",
        "url",
        "file_type",
        "file_path",
        "preview_detected",
        "status",
        "screenshot",
        "details",
        "executed_at",
    ]

    mode = "a" if append_results else "w"
    file_exists = csv_path.exists() and append_results

    with csv_path.open(mode, newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "test_case_id": row.get("test_case_id", ""),
            "feature": row.get("feature", ""),
            "url": row.get("url", ""),
            "file_type": row.get("file_type", ""),
            "file_path": row.get("file_path", ""),
            "preview_detected": row.get("preview_detected", ""),
            "status": row.get("status", ""),
            "screenshot": row.get("screenshot", ""),
            "details": row.get("details", ""),
            "executed_at": row.get("executed_at", ""),
        })


def run_test():
    configure_stdout()
    args = parse_args()

    png_path = Path(args.png).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = Path(args.csv).resolve()
    create_default_png_if_missing(png_path)

    result = {
        "test_case_id": TEST_CASE_ID,
        "feature": FEATURE_NAME,
        "url": args.url,
        "file_type": "PNG",
        "file_path": str(Path(args.png)),
        "preview_detected": False,
        "status": "FAIL",
        "screenshot": "",
        "details": "Preview was not detected.",
        "executed_at": datetime.now().isoformat(timespec="seconds"),
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=args.headless,
            slow_mo=args.slow_mo_ms
        )
        page = browser.new_page()
        page.set_default_timeout(args.timeout_ms)

        try:
            page.goto(args.url, wait_until="domcontentloaded")

            try:
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                pass

            file_input = find_file_input(page, args.timeout_ms)
            file_input.set_input_files(str(png_path))

            deadline = time.time() + (args.timeout_ms / 1000)
            preview_found = False

            while time.time() < deadline:
                if check_preview_visible(page):
                    preview_found = True
                    break
                page.wait_for_timeout(500)

            status = "PASS" if preview_found else "FAIL"

            screenshot_path = out_dir / f"preview_{status.lower()}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)

            result = {
                "test_case_id": TEST_CASE_ID,
                "feature": FEATURE_NAME,
                "url": args.url,
                "file_type": "PNG",
                "file_path": str(Path(args.png)),
                "preview_detected": preview_found,
                "status": status,
                "screenshot": str(Path(args.out_dir) / screenshot_path.name),
                "details": (
                    "PNG upload preview was displayed successfully."
                    if preview_found
                    else "PNG upload completed, but preview media was not detected."
                ),
                "executed_at": datetime.now().isoformat(timespec="seconds"),
            }

            print("========== TEST RESULT ==========")
            print(f"PNG file        : {png_path}")
            print(f"Preview detected: {preview_found}")
            print(f"Status          : {status}")
            print(f"Screenshot      : {screenshot_path}")
            print(f"CSV             : {csv_path}")

        except Exception as e:
            error_screenshot = out_dir / "preview_error.png"
            try:
                page.screenshot(path=str(error_screenshot), full_page=True)
            except Exception:
                pass

            result = {
                "test_case_id": TEST_CASE_ID,
                "feature": FEATURE_NAME,
                "url": args.url,
                "file_type": "PNG",
                "file_path": str(Path(args.png)),
                "preview_detected": False,
                "status": "FAIL",
                "screenshot": str(Path(args.out_dir) / error_screenshot.name),
                "details": f"Automation error: {e}",
                "executed_at": datetime.now().isoformat(timespec="seconds"),
            }

            print("========== TEST RESULT ==========")
            print(f"PNG file        : {png_path}")
            print("Preview detected: False")
            print("Status          : FAIL")
            print(f"Screenshot      : {error_screenshot}")
            print(f"CSV             : {csv_path}")
            print(f"Error           : {e}")

        finally:
            browser.close()

    write_result_to_csv(csv_path, result, args.append_results)


if __name__ == "__main__":
    run_test()
