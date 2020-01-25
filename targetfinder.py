import selenium
import time
from target import Target


# Search for viable targets within a system
def search_for_targets(browser, ss_system, galaxy):
    # Disable implicit waiting to speed up target search
    browser.implicitly_wait(0)

    target_list = []

    for i in range(15):
        encounter = False
        empty_slot = False

        # Check to see if an encounter exists without breaking the code
        try:
            browser.find_element_by_id(f"planet_{i+1}e")
            encounter = True
        except:
            encounter = False

        # Check to see if planet slot is empty without breaking code
        try:
            if browser.find_element_by_xpath(f"//*[@id='planet_{i+1}']/td[2]/div").get_attribute("class") == "inline_action":
                empty_slot = True
        except:
            empty_slot = False

        try:
            # If planet has an alien encounter, continue
            if encounter:
                # If the planet spot is empty, continue
                if empty_slot:
                    planet_name = browser.find_element_by_xpath(
                        f"//*[@id='planet_{i+1}e']/td[2]/span").text

                    player_name = browser.find_element_by_xpath(
                        f"//*[@id='planet_{i+1}e']/td[4]").text

                    full_name = planet_name + " " + player_name

                    # List of acceptably large enough targets
                    accepted_target_type = ["Large Floating Colony Krug",
                                            "Large Floating Colony Urcath", "Abandoned Colossus Platform Seekers"]

                    # If the selected target is acceptable, add it to the target list
                    if full_name in accepted_target_type:
                        target_list.append(
                            Target(galaxy, ss_system, i+1, abs(249 - ss_system)))
                        print(
                            f"Found target at planet: [{galaxy}:{ss_system}:{i+1}]")
        except BaseException as e:
            print(
                f"Error: Something went wrong while searching for targets in [{galaxy}:{ss_system}:{i+1}]")
            print(f"Specific Error {e}")

    # Reactivate implicit waiting
    browser.implicitly_wait(5)

    return target_list


# Scroll through galaxy
def galaxy_scroller(browser, lower_limit, upper_limit, stride):
    target_list = []

    for i in range(lower_limit, upper_limit, stride):
        time.sleep(2)

        try:
            # Get current SS
            ss_system = int(browser.find_element_by_xpath(
                "//*[@id='solar_system']").get_attribute("value"))

            # Get current galaxy
            galaxy = int(browser.find_element_by_xpath(
                "//*[@id='galaxy']").get_attribute("value"))
        except BaseException as e:
            print(
                f"Error: Something went wrong while trying to get current SS or galaxy")
            print(f"Specific Error {e}")

        # Print the current system that is being searched
        print(f"Searching system: [{galaxy}:{ss_system}:0]")

        # Add viable targets from searched SS to the target list
        target_list.extend(search_for_targets(browser, ss_system, galaxy))

        # Navigate to new SS
        try:
            browser.find_element_by_xpath("//*[@id='solar_system']").clear()
            ss_system = 249 + i
            browser.find_element_by_xpath(
                "//*[@id='solar_system']").send_keys(ss_system)
            browser.find_element_by_xpath(
                "//*[@id='set_coordinates_form']/div[3]/span[1]/a/span").click()
        except BaseException as e:
            print(
                f"Error: Something went wrong while trying to navigate to a new SS")
            print(f"Specific Error {e}")

    return target_list


# Scroll though the SS systems to find targets
def find_targets(browser):
    limit = 20
    target_list = []

    # Go to galaxy page
    try:
        browser.get(
            "https://uni2.playstarfleetextreme.com/galaxy/show?current_planet=1000000216225&galaxy=1&solar_system=249")
    except BaseException as e:
        print(f"Error: Something went wrong while trying to go to the galaxy page")
        print(f"Specific Error {e}")

    # Scroll up through galaxy
    target_list.extend(galaxy_scroller(browser, 1, limit, 1))

    # Reset SS location to one system below home system
    try:
        time.sleep(1)
        browser.get(
            "https://uni2.playstarfleetextreme.com/galaxy/show?current_planet=1000000216225&galaxy=1&solar_system=249")
    except BaseException as e:
        print(f"Error: Something went wrong while trying to reset SS location")
        print(f"Specific Error {e}")

    # Scroll down through galaxy
    target_list.extend(galaxy_scroller(browser, -1, -limit, -1))

    return target_list
