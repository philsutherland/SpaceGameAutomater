import selenium
import time
from target import Target
from restart import rerun


# Launch on target
def target_launcher(browser, target, galaxy, system, planet_id):
    time.sleep(2)

    try:
        # Go to solar system
        browser.get(
            f"https://uni2.playstarfleetextreme.com/galaxy/show?current_planet={planet_id}&galaxy={galaxy}&solar_system={target.system}")

        time.sleep(2)
    except BaseException as e:
        print(
            f"Error: Something went wrong while trying to go to galaxy page to launch on target")
        print(f"Specific Error {e}")
        rerun(browser)

    try:
        # Click the attack button
        browser.find_element_by_xpath(
            f"//*[@id='select_fleet_link_attack_{target.planet}e']").click()

        # Pause for 2 seconds to make sure attack window loads
        time.sleep(2)

        # Select all zeus ships
        browser.find_element_by_xpath(
            "//*[@id='assign_fleet_form']/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/input").click()

        time.sleep(2)

        # Record attack duration
        travel_time = str(browser.find_element_by_xpath(
            "//*[@id='task_duration']").text)
        travel_time = travel_time.split(":")
        duration = (int(travel_time[0])*3600 +
                    int(travel_time[1])*60 + int(travel_time[2])) * 2

        print(f"Duration is: {duration}s")

        # Launch attack
        browser.find_element_by_xpath("//*[@id='assign_button']").click()
        print(f"Zeus fleet launched at: {target.location()}")

        # Pause to let attack process
        time.sleep(2)
        
    except BaseException as e:
        print(
            f"Error: Something went wrong while trying to launch on {target.location()}")
        print(f"Specific Error {e}")
        rerun(browser)

    return duration
