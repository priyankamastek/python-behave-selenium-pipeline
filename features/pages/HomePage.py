from selenium.webdriver.common.by import By

from .BasePage import BasePage
from .LoginPage import LoginPage
from .SearchPage import SearchPage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    #find_element(BY.XPATH, "//span[text()='My Account']"
    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"

    def click_on_my_account(self):
        #self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        #self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        login_page = LoginPage(self.driver)
        return login_page

    def check_home_page_title(self, expected_title_text):
        return self.driver.title.__eq__(expected_title_text)

    # SearchPage
    def enter_product_into_search_box_field(self, product_text):
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_text)

    def click_on_search_button(self):
        #self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)