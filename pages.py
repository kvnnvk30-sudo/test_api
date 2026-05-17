from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReqresPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://reqres.in"
        # Используем более надежный селектор по тексту внутри списка
        self.register_button = (By.XPATH, "//li[@data-id='register-successful']")

    def open(self):
        self.driver.get(self.url)

    def click_register_api(self):
        wait = WebDriverWait(self.driver, 10)
        # Исправлено название метода на presence_of_element_located
        element = wait.until(EC.presence_of_element_located(self.register_button))

        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()