from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_successful_login():
    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_experimental_option("detach", True) 

    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://letsusedata.com")

    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.presence_of_element_located((By.ID, "edit-name")))
    username.send_keys("username")

    password = driver.find_element(By.ID, "edit-pass")
    password.send_keys("password")

    driver.find_element(By.ID, "edit-submit").click()
