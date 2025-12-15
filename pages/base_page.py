from utils.logger import Logger

class BasePage:
    def __init__(self, page):
        self.page = page
        self.logger = Logger.get_logger(self.__class__.__name__)
        
    def navigate_to(self, url):
        self.logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)
        self.logger.debug(f"Successfully navigated to: {url}")
        
    def get_page_title(self):
        title = self.page.title()
        self.logger.debug(f"Page title: {title}")
        return title
    
    def is_element_visible(self, selector):
        is_visible = self.page.locator(selector).is_visible()
        self.logger.debug(f"Element '{selector}' visible: {is_visible}")
        return is_visible
    
    def wait_for_element(self, selector, timeout=30000):
        self.logger.debug(f"Waiting for element: {selector}")
        self.page.wait_for_selector(selector, timeout=timeout)
        self.logger.debug(f"Element appeared: {selector}")