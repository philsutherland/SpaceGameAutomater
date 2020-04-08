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

    # Run the automator in a loop
    while True:
        # Make sure to update the dictioanry in the Controller object when changes run planets
        run(browser, 1, 249, 1000000216225)
        run(browser, 3, 200, 1000000201099)
        run(browser, 4, 133, 1000000033163)
        run(browser, 9, 440, 1000000029519)
