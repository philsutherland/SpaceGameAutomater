from selenium import webdriver
# from target import Target
import selenium
from time import sleep
from threading import Thread
import threading
import sys


# This class holds the static variables
class Controller:
    zeus_fleet_active = False
    heph_active = False


# Changes the status of the zeus fleet once it returns from an attack
def change_zeus_fleet_status(thread_name, delay):
    print("Thread: " + thread_name)
    print(delay)
    sleep(delay)
    Controller.zeus_fleet_active = False

    # End thread
    print("Ending zeus thread")
    sys.exit()


# If this is the first file called, run
if __name__ == "__main__":
    print("Go Selenium!")

    # Start webdriver
    try:
        browser = webdriver.Chrome()

    except:
        print("Error: Selenium Webdriver could not be started")

    login(browser)

    while True:
        if Controller.zeus_fleet_active == False:
            # Find target
            print("Find target")
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
