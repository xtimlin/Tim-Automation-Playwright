import pytest, webbrowser, os
from pytest_html import extras


def pytest_sessionfinish():
    report_path = os.path.abspath("reports/report.html")
    if os.path.exists(report_path):
        webbrowser.open_new_tab(f"file://{report_path}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if not page:
            for k, v in item.funcargs.items():
                if isinstance(v, dict) and "page" in v:
                    page = v["page"]
                    break

        if page:
            os.makedirs("reports", exist_ok=True)
            screenshot_path = os.path.join("reports", f"{item.name}.png")
            page.screenshot(path=screenshot_path, full_page=True)
            extra = getattr(report, "extra", [])
            extra.append(extras.image(screenshot_path))
            report.extra = extra
