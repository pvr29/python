import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helium import *


# Default Chrome options
default_options = ["--disable-extensions", "--disable-user-media-security=true",
                   "--allow-file-access-from-files",

                   "--use-fake-device-for-media-stream",
                   "--use-fake-ui-for-media-stream", "--disable-popup-blocking",

                   "--disable-infobars", "--enable-usermedia-screen-capturing",

                   "--disable-dev-shm-usage",
                   "--no-sandbox",
                   "--auto-select-desktop-capture-source=Screen 1",

                   "--disable-blink-features=AutomationControlled"]
# Headless Chrome options
headless_options = ["--headless", "--use-system-clipboard", "--window-size=1920x1080"]


# Function to set browser options based on type (headless or regular)
def browser_options(chrome_type):
    webdriver_options = webdriver.ChromeOptions()
    notification_opt = {"profile.default_content_setting_values.notifications": 1}
    webdriver_options.add_experimental_option("prefs", notification_opt)
    if chrome_type == "headless":
        var = default_options + headless_options
    else:
        var = default_options
    for d_o in var:
        webdriver_options.add_argument(d_o)
    return webdriver_options


# Function to initialize the WebDriver instance
def get_webdriver_instance(browser=None):
    base_url = "https://accounts.teachmint.com/"

    # Create Chrome options
    options = browser_options(browser)
    options.add_experimental_option("detach", True)

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(base_url)
    set_driver(driver)
    return driver


# Function to enter phone number and OTP
def enter_phone_number_otp(driver, creds):
    # Enter phone number
    driver.find_element(By.NAME, "username").send_keys(creds[0])
    driver.find_element(By.ID, "send-otp-btn-id").click()
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loader")))
    time.sleep(1)

    # Enter OTP
    for i, otp_digit in enumerate(creds[1]):
        otp_input = driver.find_element(By.XPATH, f"//input[@data-group-idx='{i}']")
        otp_input.send_keys(otp_digit)
        time.sleep(1)  # Add a slight delay after entering each OTP digit

    # Submit OTP
    driver.find_element(By.ID, "submit-otp-btn-id").click()
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".loader")))
    time.sleep(2)

# Main login function
def login(admin_credentials=None, account_name="@Automation-2"):
    # If admin_credentials is None, use default credentials
    if admin_credentials is None:
        admin_credentials = ["0000020232", "120992", "@Automation-2"]

    driver = get_webdriver_instance()

    # Enter phone number and OTP
    enter_phone_number_otp(driver, admin_credentials)

    # Wait until login is successful
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{account_name}']")))
    time.sleep(1)

    # Click on the account
    driver.find_element(By.XPATH, f"//div[text()='{account_name}']").click()
    time.sleep(1)

    return driver



# Main function
def main():
    # Perform login
    driver = login()

    # Quit the driver
    driver.quit()


if __name__ == "__main__":
    print("Starting the login process...")
    main()
    print("Login process completed.")
