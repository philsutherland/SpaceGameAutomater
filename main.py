from selenium import webdriver
import sys
from login import login
from controller import run
from restart import restart_program


# If this is the first file called, run
if __name__ == "__main__":
    print("Go Selenium!")

    # Start webdriver
    try:
        browser = webdriver.Chrome()

    except BaseException as e:
        print("Error: Selenium Webdriver could not be started")
        print(f"Specific Error {e}")
        sys.exit()

    # Initiate the login process
    login(browser)

    # Run the automator
    run(browser)
