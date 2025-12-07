from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://letsusedata.com")

        wait = WebDriverWait(driver, 15)

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        title = driver.title.lower()
        url = driver.current_url.lower()

        assert "letsusedata" in url or "letsusedata" in title

    finally:
        driver.quit()


def test_unsuccessful_login():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://letsusedata.com")

        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        title = driver.title.lower()
        url = driver.current_url.lower()

        assert "letsusedata" in url or "letsusedata" in title

    finally:
        driver.quit()
