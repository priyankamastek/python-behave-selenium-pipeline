from behave import *
from selenium.webdriver.common.by import By
from datetime import datetime

@given(u'I navigate to Register Page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Register").click()

@when(u'I enter below details into mandatory fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("John")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Mathew")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    new_email = "johnmathew"+time_stamp+"@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(new_email)
    context.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")

@when(u'I select Privacy Policy option')
def step_impl(context):
    context.driver.find_element(By.NAME, "agree").click()


@when(u'I click on Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@then(u'Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(expected_text)

