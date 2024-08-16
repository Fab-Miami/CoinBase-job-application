import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# -----------------------------------------------------------------------------------------
# Read the README.md file for instructions on how to use this script
# -----------------------------------------------------------------------------------------
# Fill in the following details before running the script
FIRST_NAME = 'your_first_name'
LAST_NAME = 'your_last_name'
EMAIL = 'your@email.com'
PHONE = 'your_phone_number'
LINKEDIN_PROFILE = 'https://www.linkedin.com/in/blahblahblah/'
RESUME_PATH = os.path.abspath('/Users/....etc') # for PC, change the /Users/ to C:/Users/...
COVER_LETTER_PATH = os.path.abspath('/Users/....etc') 
COINBASE_PRODUCT_EXPERIENCE = "Yes, + some blah blah..."
GENDER = 'Male'
ETHNIC_BACKGROUND = 'whichever-you-identify-to'
JOB_HEARD_FROM = 'Career Page' # or 'LinkedIn' or ....
# -----------------------------------------------------------------------------------------
URL_LIST_FILE = 'url_list.txt' # make sure the file is in the same directory as the script
# -----------------------------------------------------------------------------------------


def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

# Function to fill out text fields and check
def fill_and_check(label_text, value, is_partial_match=False):
    global driver
    try:
        # Modify the XPath to use starts-with if is_partial_match is True
        if is_partial_match:
            xpath = f"//label[starts-with(text(), '{label_text}')]/following-sibling::div//input"
        else:
            xpath = f"//label[contains(text(), '{label_text}')]/following-sibling::div//input"
        
        element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(value)
        assert element.get_attribute('value') == value
    except Exception as e:
        print(f"Failed to fill and check the field with label '{label_text}': {e}")

# Function to extract the Job ID from the URL
def extract_job_id(url):
    return url.rstrip('/').split('/')[-1]

# Reading the URL list and filtering out commented lines
def read_url_list(filename):
    with open(filename, 'r') as file:
        urls = [line.strip() for line in file if line.strip() and not line.strip().startswith('#')]
    return urls

# Function to process the form
def process_form(url):
    global driver
    job_id = extract_job_id(url)
    driver.get(url)
    
    try:
        # Wait for the first iframe to be available and switch to it
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
        iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]  # Select the first iframe
        driver.switch_to.frame(iframe)

        # Fill in text fields and check using label texts
        fill_and_check('First Name', FIRST_NAME)
        fill_and_check('Last Name', LAST_NAME)
        fill_and_check('Email', EMAIL)
        fill_and_check('Phone', PHONE, is_partial_match=True)
        fill_and_check('Linkedin', LINKEDIN_PROFILE)

        # Upload resume
        try:
            resume_element = driver.find_element(By.ID, 'resume')
            resume_element.send_keys(RESUME_PATH)
        except Exception as e:
            print(f"Resume upload failed: {e}")

        # Upload cover letter (optional)
        try:
            cover_letter_element = driver.find_element(By.ID, 'cover_letter')
            cover_letter_element.send_keys(COVER_LETTER_PATH)
        except Exception as e:
            print(f"Cover letter upload failed: {e}")

        # Select "Yes" for the question about work authorization
        try:
            yes_radio_button = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Are you legally authorized to work')]/following-sibling::div//input[@value='1']"))
            )
            driver.execute_script("arguments[0].click();", yes_radio_button)
        except Exception as e:
            print(f"Work authorization radio button not found: {e}")

        # Select "No" for the question about visa sponsorship
        try:
            no_radio_button = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Will you now or in the future require sponsorship')]/following-sibling::div//input[@value='0']"))
            )
            driver.execute_script("arguments[0].click();", no_radio_button)
        except Exception as e:
            print(f"Visa sponsorship radio button not found: {e}")

        # Locate the textarea for the question about using Coinbase products (TEXT ANSWER)
        try:
            coinbase_products_label = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Have you ever used any Coinbase products?')]"))
            )
            coinbase_products_textarea = coinbase_products_label.find_element(By.XPATH, "//following-sibling::div//textarea")
            coinbase_products_textarea.send_keys(COINBASE_PRODUCT_EXPERIENCE)
        except Exception as e:
            print(f"Coinbase products textarea not found: {e}")

        # Select Have you ever used any Coinbase products (RADIO BUTTON)
        try:
            user_label = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Have you ever used any Coinbase products')]/following-sibling::div//input[@value='1']"))
            )
            driver.execute_script("arguments[0].click();", user_label)
        except Exception as e:
            print(f"Coinbase products radio button not found: {e}")

        # Select "Yes" for "Are you at least 18 years of age?"
        try:
            age_label = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Are you at least 18 years of age')]/following-sibling::div//input[@value='1']"))
            )
            driver.execute_script("arguments[0].click();", age_label)
        except Exception as e:
            print(f"Age confirmation radio button not found: {e}")

        # Select Do you have the direct years of product management experience
        try:
            experience_label = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Do you have the direct years of product management experience')]/following-sibling::div//input[@value='1']"))
            )
            driver.execute_script("arguments[0].click();", experience_label)
        except Exception as e:
            print(f"Product management experience radio button not found: {e}")

        # Select "No" for "Have you previously been employed by Coinbase in any capacity?"
        try:
            employment_label = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Have you previously been employed by Coinbase')]/following-sibling::div//input[@value='0']"))
            )
            driver.execute_script("arguments[0].click();", employment_label)
        except Exception as e:
            print(f"Previous employment radio button not found: {e}")

        # Select "LinkedIn" from the dropdown for "How did you hear about this job?"
        try:
            dropdown_label = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'How did you hear about this job')]"))
            )
            dropdown = dropdown_label.find_element(By.XPATH, "//following-sibling::div//select")
            select = Select(dropdown)
            select.select_by_visible_text(JOB_HEARD_FROM)
        except Exception as e:
            print(f"Dropdown for 'How did you hear about this job?' not found: {e}")

        # Check the "Confirmed" checkbox for Global Data Privacy Notice using JavaScript
        try:
            privacy_label = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Please confirm receipt of the above linked Global')]"))
            )
            confirmed_checkbox = driver.find_element(By.XPATH, "//label[contains(text(), 'Please confirm receipt of the above linked Global')]/following-sibling::div//input[@type='radio']")
            driver.execute_script("arguments[0].click();", confirmed_checkbox)
        except Exception as e:
            print(f"Global Data Privacy Notice checkbox not found: {e}")

        # Select "Male" for "What is your gender?"
        try:
            gender_select = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[starts-with(@id, 'demographics_')]")))[0]  # first dropdown
            Select(gender_select).select_by_visible_text(GENDER)
        except Exception as e:
            print(f"Gender selection dropdown not found: {e}")


        # Select the option that starts with "White" for "How would you describe your racial/ethnic background?"
        ethnic_dropdown = WebDriverWait(driver, 1).until(EC.presence_of_all_elements_located((By.XPATH, "//*[starts-with(@id, 'demographics_')]")))[1]  # second dropdown

        for option in Select(ethnic_dropdown).options:
            if option.text.startswith(ETHNIC_BACKGROUND):
                Select(ethnic_dropdown).select_by_visible_text(option.text)
                break

    except Exception as e:
        print(f"An error occurred while processing the form for Job ID {job_id}: {e}")

    # Wait for user confirmation before submitting the form
    input("Form is filled out. Review the form, and press Enter to submit or close the browser window to cancel.")

    # Click the submit button if it exists and make sure form is submitted
    try:
        submit_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='apply_button' or @type='submit' or @name='commit']")
            )
        )
        driver.execute_script("arguments[0].click();", submit_button)
        print(f"Submit Button Clicked for Job ID {job_id}")

        WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.ID, "submit_job")))

        time.sleep(2)

        print(f"Form submission confirmed for Job ID {job_id}. Proceeding to the next page...")
        mark_url_as_processed(url)

    except Exception as e:
        print(f"Submit button not found or could not be clicked for Job ID {job_id}: {e}")


# Function to read the URL list and check for duplicate Job IDs
# Function to read the URL list and check for duplicate Job IDs
def read_and_validate_urls(filename):
    job_ids = {}
    duplicates = []

    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()

            # Skip empty lines
            if not stripped_line:
                continue

            # Extract the Job ID from the URL or commented URL
            job_id = stripped_line.rstrip('/').split('/')[-1]

            if job_id in job_ids:
                duplicates.append(job_id)
            job_ids[job_id] = stripped_line.startswith('#')

    # If there are any duplicates, prompt the user and stop the script
    if duplicates:
        print(f"\033[91mDuplicate Job IDs found (whether commented or not): {', '.join(duplicates)}\033[0m")
        print("\033[91mPlease resolve the duplicates and try again.\033[0m")
        return None

    # Return a list of URLs to process (only active, non-commented lines)
    return [line.strip() for line in open(filename, 'r') if line.strip() and not line.strip().startswith('#')]

# Mark URL as processed by adding a comment character at the beginning of the line
def mark_url_as_processed(url):
    with open(URL_LIST_FILE, 'r') as file:
        lines = file.readlines()

    with open(URL_LIST_FILE, 'w') as file:
        for line in lines:
            if line.strip() == url.strip():
                file.write(f"# {line}")
            else:
                file.write(line)

# ====================================================================================

# Main function to execute the script
def main():
    global driver
    driver = setup_driver()

    # Ask the user for mode selection with a numerical choice
    print("Select mode:")
    print("1. One by one URL mode")
    print("2. URL list mode")
    mode = input("Enter your choice (1 or 2): ").strip()

    if mode == "1":
        while True:
            url = input("Enter the webpage URL: ")
            if url.lower() == "exit":
                print("Exiting script.")
                break
            process_form(url)

    elif mode == "2":
        urls = read_and_validate_urls(URL_LIST_FILE)
        if urls is None:
            return  # Stop script execution if there are duplicate Job IDs

        for url in urls:
            process_form(url)

        print("All URLs processed. Job applications are complete.")

    else:
        print("Invalid choice. Exiting script.")

if __name__ == "__main__":
    main()
