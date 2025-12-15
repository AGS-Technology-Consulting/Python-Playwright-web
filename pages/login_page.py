from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    FLASH_MESSAGE = "#flash"
    LOGOUT_BUTTON = "a[href='/logout']"
    
    def __init__(self, page):
        super().__init__(page)
        
    def enter_username(self, username):
        self.logger.info(f"Entering username: {username}")
        self.page.fill(self.USERNAME_INPUT, username)
        
    def enter_password(self, password):
        self.logger.info("Entering password: ********")
        self.page.fill(self.PASSWORD_INPUT, password)
        
    def click_login_button(self):
        self.logger.info("Clicking login button")
        self.page.click(self.LOGIN_BUTTON)
        
    def login(self, username, password):
        self.logger.info(f"Attempting login with username: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        
    def get_flash_message(self):
        message = self.page.locator(self.FLASH_MESSAGE).inner_text()
        self.logger.info(f"Flash message: {message.strip()}")
        return message
    
    def is_login_successful(self):
        is_successful = self.is_element_visible(self.LOGOUT_BUTTON)
        self.logger.info(f"Login successful: {is_successful}")
        return is_successful
    
    def is_on_login_page(self):
        on_login_page = self.is_element_visible(self.LOGIN_BUTTON)
        self.logger.debug(f"On login page: {on_login_page}")
        return on_login_page