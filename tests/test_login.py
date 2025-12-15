import pytest
from config.config import Config
from utils.logger import Logger

class TestLogin:
    
    def test_successful_login_with_valid_credentials(self, login_page):
        """Test Case 1: Verify successful login with valid credentials - PASS"""
        logger = Logger.get_logger(self.__class__.__name__)
        
        logger.info("Starting test: Successful login with valid credentials")
        # Perform login
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        
        # Verify login is successful
        logger.info("Verifying login success")
        assert login_page.is_login_successful(), "Login button should not be visible after successful login"
        
        # Verify success message
        flash_message = login_page.get_flash_message()
        assert "You logged into a secure area!" in flash_message, f"Expected success message, got: {flash_message}"
        logger.info("Test completed successfully")
    
    def test_login_with_invalid_username(self, login_page):
        """Test Case 2: Verify login fails with invalid username - PASS"""
        logger = Logger.get_logger(self.__class__.__name__)
        
        logger.info("Starting test: Login with invalid username")
        # Attempt login with invalid username
        login_page.login("invaliduser", Config.VALID_PASSWORD)
        
        # Verify still on login page
        logger.info("Verifying user remains on login page")
        assert login_page.is_on_login_page(), "Should remain on login page after failed login"
        
        # Verify error message
        flash_message = login_page.get_flash_message()
        assert "Your username is invalid!" in flash_message, f"Expected error message, got: {flash_message}"
        logger.info("Test completed successfully")
    
    def test_login_with_invalid_password(self, login_page):
        """Test Case 3: Verify login fails with invalid password - PASS"""
        logger = Logger.get_logger(self.__class__.__name__)
        
        logger.info("Starting test: Login with invalid password")
        # Attempt login with invalid password
        login_page.login(Config.VALID_USERNAME, "wrongpassword")
        
        # Verify still on login page
        logger.info("Verifying user remains on login page")
        assert login_page.is_on_login_page(), "Should remain on login page after failed login"
        
        # Verify error message
        flash_message = login_page.get_flash_message()
        assert "Your password is invalid!" in flash_message, f"Expected error message, got: {flash_message}"
        logger.info("Test completed successfully")
    
    def test_login_with_empty_credentials(self, login_page):
        """Test Case 4: Verify login fails with empty credentials - FAIL (intentional)"""
        logger = Logger.get_logger(self.__class__.__name__)
        
        logger.info("Starting test: Login with empty credentials (intentional fail)")
        # Attempt login with empty credentials
        login_page.login("", "")
        
        logger.warning("This test is designed to fail intentionally")
        # This assertion will fail intentionally to demonstrate a failed test
        assert login_page.is_login_successful(), "This test is designed to fail - empty credentials should not allow login"