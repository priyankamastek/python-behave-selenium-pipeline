from utilities import ConfigReader
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
import os

"""
 #     options = ChromeOptions()
    #     if headless:
    #         options.add_argument("--headless")
    #     context.driver = webdriver.Chrome(options=options)
"""
def before_all(context):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # ✅ Download driver ONCE per build
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)

    url = ConfigReader.read_configuration("basic info", "url")
    context.driver.get(url)


def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()

                       

""" 
  def before_scenario(context, scenario):
    # Reading configurations from behave.ini
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    print(browser_name)
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument('--headless')
        # Optional: other arguments for robustness
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage') # Useful for Docker/Jenkins environments
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))
       
 
    # context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
"""
                


def after_step(context,step):
  if step.status in ['failed', 'error'] and hasattr(context, "driver"):
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=AttachmentType.PNG
       )

