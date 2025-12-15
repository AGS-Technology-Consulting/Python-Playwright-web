import pytest
import os
import allure
from datetime import datetime
from playwright.sync_api import sync_playwright
from config.config import Config
from pages.login_page import LoginPage
from utils.logger import Logger


@pytest.fixture(scope="function")
def browser_context():
    logger = Logger.get_logger("FixtureSetup")
    logger.info("Setting up browser context")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=Config.HEADLESS)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(Config.TIMEOUT)
        
        logger.info("Browser context created successfully")
        yield page
        
        logger.info("Tearing down browser context")
        context.close()
        browser.close()
        logger.info("Browser closed")

@pytest.fixture(scope="function")
def login_page(browser_context):
    logger = Logger.get_logger("FixtureSetup")
    page = browser_context
    login_page = LoginPage(page)
    logger.info(f"Navigating to base URL: {Config.BASE_URL}")
    login_page.navigate_to(Config.BASE_URL)
    return login_page

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call":
        logger = Logger.get_logger("TestExecution")
        test_name = item.nodeid
        
        # Get the page fixture if available
        if "browser_context" in item.funcargs:
            page = item.funcargs["browser_context"]
            
            # Take screenshot on failure
            if rep.failed and Config.SCREENSHOT_ON_FAILURE:
                try:
                    # Create screenshots directory
                    if not os.path.exists(Config.SCREENSHOT_DIR):
                        os.makedirs(Config.SCREENSHOT_DIR)
                    
                    # Generate screenshot filename
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    test_name_clean = test_name.replace("::", "_").replace("/", "_")
                    screenshot_path = f"{Config.SCREENSHOT_DIR}/{test_name_clean}_{timestamp}.png"
                    
                    # Take screenshot
                    page.screenshot(path=screenshot_path, full_page=True)
                    logger.info(f"Screenshot saved: {screenshot_path}")
                    
                    # Attach to Allure report
                    with open(screenshot_path, "rb") as image_file:
                        allure.attach(
                            image_file.read(),
                            name=f"Failure Screenshot - {timestamp}",
                            attachment_type=allure.attachment_type.PNG
                        )
                    
                except Exception as e:
                    logger.error(f"Failed to capture screenshot: {str(e)}")
        
        if rep.passed:
            Logger.log_test_end(test_name, "PASSED ✓")
        elif rep.failed:
            Logger.log_test_end(test_name, "FAILED ✗")
            logger.error(f"Test failed with error: {rep.longreprtext}")
        elif rep.skipped:
            Logger.log_test_end(test_name, "SKIPPED")

def pytest_runtest_setup(item):
    logger = Logger.get_logger("TestExecution")
    Logger.log_test_start(item.nodeid)