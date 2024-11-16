import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

# os.popen(r'chrome --remote-debugging-port=9222 --user-data-dir="C:\Users\ammar\Desktop\Newfolder"')

# Function to download image
def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)

def close_pop_up(driver):w
    try:
        # Wait until the pop-up is present
        wait = WebDriverWait(driver, 10)
        pop_up_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div')))
        
        # Click the close button on the pop-up
        close_button = pop_up_element.find_element(By.XPATH, 'your_close_button_xpath_here')
        close_button.click()
        print("Pop-up closed successfully!")
    except Exception as e:
        print(f"An error occurred while closing the pop-up: {e}")



# Function to scrape social media post
def scrape_post(post_url):
    # Set up the WebDriver (assuming Chrome)
    driver = webdriver.Chrome()
    # option = webdriver.ChromeOptions()
    # option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe", options=option)

    try:
        # Navigate to the post URL
        driver.get(post_url)
        time.sleep(2)  # Wait for the page to load

        # Extract post content (example for Instagram)
        # post_content = driver.find_element(By.CSS_SELECTOR, 'div.C4VMK > span').text
        time.sleep(2)  # Wait for the page to load

        # Extract image URL (example for Instagram)
        print("Waiting to detect images...")
        close_pop_up(driver)

        wait = WebDriverWait(driver, 10)
        post_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, '__aagv')))
        print("Post div found!")
        # Find the image tag within this div
        image_element = post_div.find_element(By.TAG_NAME, 'img')
        print("Image element found!")

        image_url = image_element.get_attribute('src')
        time.sleep(2)  # Wait for the page to load

        # Save the image
        image_path = os.path.join(os.getcwd(), 'post_image.jpg')
        download_image(image_url, image_path)
        time.sleep(2)  # Wait for the page to load

        # print(f"Post content: {post_content}")
        print(f"Image saved at: {image_path}")
    except Exception as e:
        print("Error occured")
        print(e)
    finally:
        # driver.quit()
        print("finished")

# User provides the URL
# post_url = input("Enter the URL of the social media post: ")
post_url = "https://www.instagram.com/p/C-dRbDBpNqV/?igsh=NWNueHVyMTl4cjM5"
post_url = "https://www.instagram.com/p/C-r_nfVusMu/?igsh=MTk1Y3h0eDVnbm9qOA=="
scrape_post(post_url)