from selenium import webdriver
import sys
import random
from time import sleep
from threading import Thread
import threading
from luckydraw import check_for_lucky_draw
from target import Target
from targetfinder import find_targets
from targetlauncher import target_launcher
from restart import rerun


# This class holds the static variables and methods associated with running the program
class Controller:
    zeus_fleet_active = False
    heph_active = False
    used_target_list = []


# Changes the status of the zeus fleet once it returns from an attack
def change_zeus_fleet_status(thread_name, delay):
    print("Thread: " + thread_name)

    # Add a random 5 - 10 minutes onto the time between zeus fleet return and launch
    delay += 300 + random.random()*300
    print(f"The delay is: {delay}s")

    # Keep the thread waiting for the duration of the delay
    threading.Event().wait(delay)

    # Make  the zeus fleet active again
    Controller.zeus_fleet_active = False
    print("Zeus fleet now nonactive")

    # End thread
    print("Ending zeus thread")
    sys.exit()


# The method is the main loop that runs the program
def run(browser):
    print("Running script")
    # Go to galaxy page
    try:
        browser.get(
            f"https://uni2.playstarfleetextreme.com/galaxy/show?current_planet=1000000216225&galaxy=1&solar_system=249")
    except BaseException as e:
        print("Error: Unable to initially go to game page")
        print(f"Specific Error {e}")
        rerun(browser)

    while True:
        # Lucky draw could pop up at any time so it needs to be checked for in each iteration
        if browser.find_element_by_id("content").get_attribute("class") == "lucky_draw index":
            check_for_lucky_draw(browser)

        if Controller.zeus_fleet_active == False:
            # Find targets
            print("Finding targets")
            target = None
            target_list = []
            target_list.extend(find_targets(browser))

            # Sort targets based on proximity
            target_list.sort(key=lambda x: x.proximity)

            # Launch at target
            print("\nTargets found:")
            for _target in target_list:
                print(
                    f"Location: {_target.location()} Proximity: {_target.proximity}")

            # Check if target has been hit before
            try:
                for _target in target_list:
                    if not any(x.location() == _target.location() for x in Controller.used_target_list):
                        target = _target
                        break
            except BaseException as e:
                print(
                    f"Error: Something went wrong while checking if the target has been hit before")
                print(f"Specific Error {e}")
                rerun(browser)

            # Launch on target
            print(f"Launching at target: {target.location()}")
            duration = target_launcher(browser, target)

            # Add current target to used target list
            Controller.used_target_list.append(target)

            # Change zeus fleet to active
            Controller.zeus_fleet_active = True
            print("Zeus fleet now active")

            try:
                # Create new thread to change zeus fleet status back to False once fleet returns
                zeus_thread = Thread(target=change_zeus_fleet_status,
                                     args=("Change Zeus Fleet Status", duration,))

                # Start the zeus fleet thread
                zeus_thread.start()
                print("Starting zeus thread")
            except BaseException as e:
                print("Error: Unable to start zeus thread")
                print(f"Specific Error {e}")
                rerun(browser)

        if Controller.heph_active == False:
            # Find debris field
            print("Finding debris field")

            # Move heph to debris field
            print("Moving heph to debris field")

            # Harvest debris field
            print("Harvesting debris field")

            Controller.heph_active = True
