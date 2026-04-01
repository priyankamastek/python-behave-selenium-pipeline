from utilities import ConfigReader
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import os

"""
 #     options = ChromeOptions()
    #     if headless:
    #         options.add_argument("--headless")
    #     context.driver = webdriver.Chrome(options=options)
"""
def before_all(context):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # ✅ Download driver ONCE per build
    service = Service("C:/WebDriver/chromedriver.exe")
    context.driver = webdriver.Chrome(service=service, options=options)
    url = ConfigReader.read_configuration("basic info", "url")
    context.driver.get(url)


def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()

def after_step(context,step):
  if step.status in ['failed', 'error'] and hasattr(context, "driver"):
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=AttachmentType.PNG
       )

