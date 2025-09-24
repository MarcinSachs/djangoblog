import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.get(url="http://127.0.0.1:8000/admin")


def element_is_clicked():
    try:
        # Użycie WebDriverWait, aby poczekać na pojawienie się elementu
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#id_username'))
        )
        username_field.send_keys("marcin")

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#id_password'))
        )
        password_field.send_keys("ziomal18")

        time.sleep(2)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[type="submit"]'))
        )  # Bardziej precyzyjny selektor CSS
        login_button.click()

    except TimeoutException:
        print("Nie udało się znaleźć elementu w określonym czasie.")


element_is_clicked()
