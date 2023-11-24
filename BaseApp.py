from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from zeep import Client, Settings

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"
        self.base_url2 = "https://speller.yandex.net/services/spellservice?WSDL"



    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                           message=f"Невозможно найти элемент по локатору {locator}")
        except:
            logging.exception("Найден элемент исключения ")
            element = None
        return element


    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        logging.error(f"Свойства {property} не найдены в элементе {locator}")
        return None
    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Исключение при открытии сайта")
            start_browsing = None
        return start_browsing


    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Исключение с ошибкой")
            return None
