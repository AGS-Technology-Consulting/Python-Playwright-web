class Config:
    BASE_URL = "https://the-internet.herokuapp.com/login"
    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"
    TIMEOUT = 30000
    HEADLESS = False

    # Logging configuration
    LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    LOG_FILE = "logs/automation.log"
    CONSOLE_LOG = True

    SCREENSHOT_ON_FAILURE = True
    SCREENSHOT_DIR = "screenshots"