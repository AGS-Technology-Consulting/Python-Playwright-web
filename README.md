# Playwright Automation Framework

A robust Python-based automation testing framework using Playwright with Page Object Model (POM) design pattern.

## 🚀 Features

- **Page Object Model (POM)** - Maintainable and reusable code structure
- **Comprehensive Logging** - Detailed logs in both console and file
- **HTML Reports** - Beautiful test execution reports
- **Allure Reports** - Beautiful, interactive test execution reports
- **CI/CD Ready** - GitHub Actions and Jenkins support
- **Configurable** - Easy configuration management
- **Cross-browser Testing** - Chromium, Firefox, WebKit support

## 📁 Project Structure

```
playwright-automation/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml    # GitHub Actions workflow
├── pages/
│   ├── __init__.py
│   ├── base_page.py                # Base page with common methods
│   └── login_page.py               # Login page object
├── tests/
│   ├── __init__.py
│   ├── conftest.py                 # Pytest fixtures and hooks
│   └── test_login.py               # Login test cases
├── config/
│   ├── __init__.py
│   └── config.py                   # Configuration settings
├── utils/
│   ├── __init__.py
│   └── logger.py                   # Logging utility
├── logs/
│   └── automation.log              # Test execution logs
├── reports/
│   └── report.html                 # HTML test reports
├── Jenkinsfile                     # Jenkins pipeline configuration
├── README.md                       # This file
├── requirements.txt                # Python dependencies
└── pytest.ini                      # Pytest configuration
```

## 🛠️ Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 📦 Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd playwright-automation
```

2. **Create virtual environment:**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
playwright install
```

## ▶️ Running Tests

### Run all tests:
```bash
pytest tests/test_login.py
```

### Run specific test:
```bash
pytest tests/test_login.py::TestLogin::test_successful_login_with_valid_credentials
```

### Run with HTML report:
```bash
pytest tests/test_login.py --html=reports/report.html --self-contained-html
```

### Run in headed mode (see browser):
```bash
# Change HEADLESS = False in config/config.py
pytest tests/test_login.py
```

### Run with verbose output:
```bash
pytest tests/test_login.py -v -s
```

### Run specific marker:
```bash
pytest tests/test_login.py -m smoke
```

### Running Tests with Allure
```bash
1. pytest --alluredir=reports/allure-results
2. allure serve reports/allure-results
```

## 📊 Test Cases

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| test_successful_login_with_valid_credentials | Login with valid username and password | PASS ✅ |
| test_login_with_invalid_username | Login with invalid username | PASS ✅ |
| test_login_with_invalid_password | Login with valid username but invalid password | PASS ✅ |
| test_login_with_empty_credentials | Login with empty credentials | FAIL ❌ (Intentional) |

## 📝 Logging

Logs are generated in two formats:

1. **Console Output** - Real-time logs during test execution
2. **File Logging** - Detailed logs saved to `logs/automation.log`

### Log Levels:
- DEBUG - Detailed information for debugging
- INFO - General information about test execution
- WARNING - Warning messages
- ERROR - Error messages
- CRITICAL - Critical issues

### Configure Logging:
Edit `config/config.py`:
```python
LOG_LEVEL = "INFO"      # Change to DEBUG for more details
CONSOLE_LOG = True      # Set to False to disable console logs
LOG_FILE = "logs/automation.log"
```

## ⚙️ Configuration

Edit `config/config.py` to customize:

```python
class Config:
    BASE_URL = "https://the-internet.herokuapp.com/login"
    VALID_USERNAME = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"
    TIMEOUT = 30000
    HEADLESS = False        # Set to True for CI/CD
    LOG_LEVEL = "INFO"
    CONSOLE_LOG = True
```

## 🔄 CI/CD Integration

### GitHub Actions

The framework includes a GitHub Actions workflow that:
- Runs on push and pull requests
- Executes tests on Ubuntu
- Generates HTML reports
- Archives test artifacts

Workflow file: `.github/workflows/playwright-tests.yml`

### Jenkins

The framework includes a Jenkinsfile that:
- Runs tests in a Docker container
- Generates and archives HTML reports
- Publishes HTML reports in Jenkins UI
- Archives logs

Pipeline file: `Jenkinsfile`

To use in Jenkins:
1. Create a new Pipeline job
2. Point to your repository
3. Jenkins will automatically detect the Jenkinsfile

## 🧪 Adding New Tests

1. **Create a new page object** in `pages/` directory:
```python
from pages.base_page import BasePage

class NewPage(BasePage):
    # Define locators
    ELEMENT = "#element-id"
    
    def interact_with_element(self):
        self.page.click(self.ELEMENT)
```

2. **Create test file** in `tests/` directory:
```python
import pytest
from utils.logger import Logger

class TestNewFeature:
    def test_something(self, browser_context):
        logger = Logger.get_logger(self.__class__.__name__)
        logger.info("Test started")
        # Your test code here
```

## 📚 Best Practices

1. **Page Object Model** - Keep page objects separate from test logic
2. **Logging** - Log important actions and verifications
3. **Assertions** - Use descriptive assertion messages
4. **Fixtures** - Reuse fixtures for common setup/teardown
5. **Independent Tests** - Each test should be independent
6. **Clear Naming** - Use descriptive names for tests and methods

## 🐛 Troubleshooting

### Issue: Browser not found
```bash
playwright install
```

### Issue: Import errors
```bash
pip install -r requirements.txt
```

### Issue: Permission denied (Linux/Mac)
```bash
chmod +x venv/bin/activate
```

### Issue: Tests failing randomly
- Increase timeout in `config/config.py`
- Check network connectivity
- Verify test data

## 📄 Reports

HTML reports are generated in the `reports/` directory:
- Test execution summary
- Pass/Fail status
- Screenshots (if configured)
- Execution time
- Error details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

For questions or support, please open an issue in the repository.

## 📜 License

This project is licensed under the MIT License.

---

**Happy Testing! 🎉**
