from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml
import logging
from zeep import Client, Settings
from conftest import client


def checkText(self, word):
    return client.service.checkText(word)[0]['s']
class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
class Check_write_text:
    with open('addr.yaml') as f:
        wsdl = yaml.safe_load(f)['wsdl']
    settings = Settings(strict=False)
    client = Client(wsdl=wsdl, settings=settings)

    def go_to_site2(self):
        try:
            start_browsing = self.driver.get(self.base_url2)
        except:
            logging.exception("Исключение при открытии сайта")
            start_browsing = None
        return start_browsing

    def checkText(self, word):
        return client.service.checkText(word)[0]['s']








class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Отправка {word} к элементу {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Нажата {element_name} кнопка")
        return True
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"Найден текст {text} в поле {element_name}")
        return text


# ENTER TEXT

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_NEW_POST"], word, description="title post")

    def enter_content_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_POST"], word, description="content post")

    def enter_description_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_NEW_POST"], word, description="description post}")

    def enter_your_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_NAME"], word, description="name")

    def enter_your_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_EMAIL"], word, description="email")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"], word, description="content")



# CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login button")

    def click_save_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save button")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_FIND_CONTACT_US"], description="contact us")

    def click_create_new_post_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST"], description="new post")

    def click_contact_us_end(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact button")



# GET TEXT

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error text")

    def get_hello_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_HELLO_USER"], description="hello text")

    def get_res_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RES_LBl"], description="result text")


    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info("text")
        return text

    def check_text(self, word):
        logging.info("check text fot mistakes")
        text = self.client.service.checkText(word)[0]['s']
        logging.info("right text")
        return text