from utilities import ConfigReader
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
#from selenium.webdriver.chrome.options import Options as ChromeOptions

"""
 #     options = ChromeOptions()
    #     if headless:
    #         options.add_argument("--headless")
    #     context.driver = webdriver.Chrome(options=options)
"""
def before_scenario(context, scenario):
    # Reading configurations from behave.ini
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    print(browser_name)
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    # context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context,step):
   if step.status == 'failed':
       allure.attach(context.driver.get_screenshot_as_png()
                       ,name="failed_screenshot"
                       ,attachment_type=AttachmentType.PNG)