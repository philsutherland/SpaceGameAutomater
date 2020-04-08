import selenium
import time
from target import Target
from restart import rerun


# Search for viable targets within a system
def search_for_targets(browser, system, galaxy):

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
                # If the planet spot is empty, continuejg
                if empty_slot:
                    planet_name = browser.find_element_by_xpath(
                        f"//*[@id='planet_{i+1}e']/td[2]/span").text

                    player_name = browser.find_element_by_xpath(
                        f"//*[@id='planet_{i+1}e']/td[4]").text

                    # Convert the color into a single integer value that represents the amount of green
                    color = int(str(browser.find_element_by_xpath(
                        f"//*[@id='planet_{i+1}e']/td[4]").get_attribute("style")).split(", ")[1])

                    full_name = planet_name + " " + player_name

                    # List of acceptably large enough targets
                    accepted_target_type = ["Large Floating Colony Krug",
                                            "Large Floating Colony Urcath", "Abandoned Colossus Platform Seekers"]

                    # If the selected target is acceptable, add it to the target list
                    if full_name in accepted_target_type:
                        target_list.append(
                            Target(galaxy, system, i+1, abs(249 - system), color))
                        print(
                            f"Found target at planet: [{galaxy}:{system}:{i+1}]")
        except BaseException as e:
            print(
                f"Error: Something went wrong while searching for targets in [{galaxy}:{system}:{i+1}]")
            print(f"Specific Error {e}")
            rerun(browser)

    # Reactivate implicit waiting
    browser.implicitly_wait(5)

    return target_list


# Scroll through galaxy
def galaxy_scroller(browser, lower_limit, upper_limit, stride, galaxy, system):
    target_list = []

    for i in range(lower_limit, upper_limit, stride):
        time.sleep(2)

        try:
            # Get current SS
            _system = int(browser.find_element_by_xpath(
                "//*[@id='solar_system']").get_attribute("value"))

            # Get current galaxy
            _galaxy = int(browser.find_element_by_xpath(
                "//*[@id='galaxy']").get_attribute("value"))
        except BaseException as e:
            print(
                f"Error: Something went wrong while trying to get current SS or galaxy")
            print(f"Specific Error {e}")
            rerun(browser)

        # Print the current system that is being searched
        print(f"Searching system: [{_galaxy}:{_system}:0]")

        # Add viable targets from searched SS to the target list
        target_list.extend(search_for_targets(browser, _system, _galaxy))

        # Navigate to new SS
        try:
            browser.find_element_by_xpath("//*[@id='solar_system']").clear()
            _system = system + i
            browser.find_element_by_xpath(
                "//*[@id='solar_system']").send_keys(_system)
            browser.find_element_by_xpath(
                "//*[@id='set_coordinates_form']/div[3]/span[1]/a/span").click()
        except BaseException as e:
            print(
                f"Error: Something went wrong while trying to navigate to a new SS")
            print(f"Specific Error {e}")
            rerun(browser)

    return target_list


# Scroll though the SS systems to find targets
def find_targets(browser, galaxy, system, planet_id, limit):
    target_list = []

    # Go to galaxy page
    try:
        browser.get(
            f"https://uni2.playstarfleetextreme.com/galaxy/show?current_planet={planet_id}&galaxy={galaxy}&solar_system={system}")
    except BaseException as e:
        print(f"Error: Something went wrong while trying to go to the galaxy page")
        print(f"Specific Error {e}")
        rerun(browser)

    # Scroll up through galaxy
    target_list.extend(galaxy_scroller(browser, 1, limit, 1, galaxy, system))

    # Reset SS location to one system below home system
    try:
        time.sleep(1)
        browser.get(
            f"https://uni2.playstarfleetextreme.com/galaxy/show?current_planet={planet_id}&galaxy={galaxy}&solar_system={system}")
    except BaseException as e:
        print(f"Error: Something went wrong while trying to reset SS location")
        print(f"Specific Error {e}")
        rerun(browser)

    # Scroll down through galaxy
    target_list.extend(galaxy_scroller(
        browser, -1, -limit, -1, galaxy, system))

    return target_list
