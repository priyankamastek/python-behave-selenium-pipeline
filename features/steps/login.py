from datetime import datetime
from behave import *
from selenium.webdriver.common.by import By
from features.pages.HomePage import HomePage


@given(u'I navigated to Login page')
def step_impl(context):
    # creating Home Page object
   context.home = HomePage(context.driver)
   context.home.click_on_my_account()
   assert context.home.check_home_page_title("Your Store")
   # Getting login page object from the function call
   context.login = context.home.select_login_option()



@when(u'I enter valid email address as {email} and valid password as {password} into the fields')
def step_impl(context,email,password):
    context.login.enter_email_address(email)
    context.login.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.login.click_on_login_button()

@then(u'I should get logged in')
def step_impl(context):
    warning_message = "Edit your account information"
    assert context.login.display_status_of_warning_message(warning_message)



@when(u'I enter invalid email "{email}" and valid password say "{password}" into the fields')
def step_impl(context,email, password):
    context.login.enter_email_address("john897@gmail.com")
    context.login.enter_password("12345")

@When(u'I enter valid email say "{email}" and invalid password say "{password}" into the fields')
def step_impl(context,email, password):
    context.login.enter_email_address("amotoriapril2023sample@gmail.com")
    context.login.enter_password("1234567890")



@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.login.enter_email_address("")
    context.login.enter_password("")

# Assignment: Refactor this code
@then(u'I should get a proper warning message')
def step_impl(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]") \
     .text.__contains__(expected_warning_message)


