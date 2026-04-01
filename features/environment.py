from utilities import ConfigReader
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
#from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
import os

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
    os.environ["MOZ_HEADLESS"] = "1"   # ✅ REQUIRED for Jenkins
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        options = Options()
    # ✅ Recommended for Jenkins
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        context.driver = webdriver.Firefox(options=options)
  
    # context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context,step):
   if step.status == 'failed':
       allure.attach(context.driver.get_screenshot_as_png()
                       ,name="failed_screenshot"
                       ,attachment_type=AttachmentType.PNG)
