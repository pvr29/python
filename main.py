import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome driver with detached option
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open Teachmint website
driver.get("https://accounts.teachmint.com/")
time.sleep(2)

# Enter username
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys('0000020232')

# Click to request OTP
driver.find_element(By.ID, "send-otp-btn-id").click()
time.sleep(3)

# Enter OTP
otp_input = driver.find_element(By.XPATH, '//*[@id="mobile-number-body"]/div/div[2]/div[1]/input[1]')
otp_input.send_keys('120992')
time.sleep(1)

# Login after entering OTP
driver.find_element(By.ID, "submit-otp-btn-id").click()
time.sleep(1)

# Skip password creation
driver.find_element(By.XPATH, "//span[@onclick='onSkipPassCreationClick()']").click()
time.sleep(3)

# Select Automation account
driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div[1]/div/div[1]/div[3]/div[2]').click()
time.sleep(10)

# Go to certificate section
driver.get("https://www.teachmint.com/institute/dashboard/certificate-templates/student/")
time.sleep(5)

# Select School Leaving certificate
# Find all the cards with class "krayon__PlainCard-module__FWclP"
cards = driver.find_elements(By.CLASS_NAME, "krayon__PlainCard-module__FWclP")

# Loop through each card to find the "School Leaving Certificate" card
for card in cards:
    # Find the card details by class name
    card_details = card.find_element(By.CLASS_NAME, "Cards_cardDetails__WsZ-E")
    # Find the heading (certificate name) within the card details
    heading = card_details.find_element(By.CLASS_NAME, "krayon__Heading-module__2pnHW")
    # Check if the heading text matches "School leaving certificate"
    if heading.text.strip() == "School leaving certificate":
        # If found, click on the card
        card.click()
        # Break out of the loop since we found the desired card
        break

time.sleep(5)

# Click on Generate button
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[3]/div[2]/div[2]/button[2]/div').click()
time.sleep(5)

# Search and select student (Sam)
search_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/div/input')
search_input.send_keys("Sam")
time.sleep(2)

# Click on Generate button to generate the certificate
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div/table/tbody/tr/td[4]/button/div').click()
time.sleep(2)

# Insert Remarks
remarks_input = driver.find_element(By.XPATH, '//*[@id="fillDetails"]/div[1]/div[2]/div[28]/div[2]/div/input')
remarks_input.send_keys('Test Automation')
time.sleep(2)

# Click on Generate to complete the process
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div/div/footer/div/button/div').click()
time.sleep(8)

# Download the generated certificate
driver.find_element(By.XPATH, '//*[@id="download"]/div').click()
time.sleep(5)

# Validate the history of certificates
driver.get('https://www.teachmint.com/institute/dashboard/certificate-templates/student/generated-list')

# Close the browser
# driver.quit()