from selenium import webdriver
import selenium
from time import sleep
from threading import Thread
import threading
import sys
from login import login
from luckydraw import check_for_lucky_draw
from target import Target
from targetfinder import find_targets


# This class holds the static variables
class Controller:
    zeus_fleet_active = False
    heph_active = False
    used_target_list = []


# Changes the status of the zeus fleet once it returns from an attack
def change_zeus_fleet_status(thread_name, delay):
    print("Thread: " + thread_name)
    print(delay)
    sleep(delay)
    Controller.zeus_fleet_active = False

    # End thread
    print("Ending zeus thread")
    sys.exit()


def run(browser):
    # Go to galaxy page
    browser.get(
        "https://uni2.playstarfleetextreme.com/galaxy/show?current_planet=1000000216225&galaxy=1&solar_system=249")

    while True:
        # Lucky draw could pop up at any time so it needs to be checked for in each iteration
        if browser.find_element_by_id("content").get_attribute("class") == "lucky_draw index":
            check_for_lucky_draw(browser)

        if Controller.zeus_fleet_active == False:
            # Find targets
            print("Find targets")
            target_list = []
            target_list.extend(find_targets(browser))

            # Launch at target
            print("Launch at target")

            Controller.zeus_fleet_active = True

            try:
                # Create new thread to change zeus fleet status back to False once fleet returns
                zeus_thread = Thread(target=change_zeus_fleet_status,
                                     args=("Change Zeus Fleet Status", 5,))

                # Start the zeus fleet thread
                zeus_thread.start()
                print("Starting zeus thread")

            except:
                print("Error: Unable to start zeus thread")

        if Controller.heph_active == False:
            # Find debris field
            print("Finding debris field")

            # Move heph to debris field
            print("Moving heph to debris field")

            # Harvest debris field
            print("Harvesting debris field")

            Controller.heph_active = True


# If this is the first file called, run
if __name__ == "__main__":
    print("Go Selenium!")

    # Start webdriver
    try:
        browser = webdriver.Chrome()

    except:
        print("Error: Selenium Webdriver could not be started")
        sys.exit()

    # Initiate the login process
    login(browser)

    # Run the automator
    run(browser)
