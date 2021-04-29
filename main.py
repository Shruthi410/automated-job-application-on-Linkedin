from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2506796570&f_AL=true&geoId=115702354&keywords=python%20developer&location=Chennai%2C%20Tamil%20Nadu%2C%20India")

EMAIL = "LINKEDIN EMAIL"
PASSWORD = "LINKEDIN PASSWORD"
PHONE = "YOUR PHONE NUMBER"

signin_button = driver.find_element_by_link_text("Sign in")
signin_button.click()

time.sleep(5)
email = driver.find_element_by_id("username")
email.send_keys(EMAIL)

password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    listing.click()

    try:
        time.sleep(5)
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone_number_input = driver.find_element_by_class_name("fb-single-line-text__input")
        phone_number_input.send_keys(PHONE)

        submit_application = driver.find_element_by_css_selector("footer button")

        if submit_application.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("complex application, skipped")
            continue
        else:
            submit_application.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("no application button, skipped")
        continue

time.sleep(5)
driver.quit()
