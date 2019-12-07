from selenium import webdriver
import selenium
import time

heph_fleet_busy = False
zeus_fleet_busy = False

print("Go Selenium go!")


browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.get("https://uni2.playstarfleetextreme.com/")


# Log into game
browser.find_element_by_id("tab-existing_account_sign_in_starfleet").click()
browser.find_element_by_xpath("//*[@id='remember_me']").click()
browser.find_element_by_xpath("//*[@id='login']").send_keys("Das Engineer")

# You can't find the element by its id since there are two id's with the name "password"
browser.execute_script("document.getElementsByClassName('mainForm')[3].value='pwd4phil'")
browser.find_element_by_xpath("//*[@id='signInNow']").click()

# Search for viable targets
def search_for_targets():



if not zeus_fleet_busy:
    # Go to galaxy page
    browser.find_element_by_xpath("//*[@id='user_planets']/div/div[2]/div/div[2]/a[1]").click()
    browser.find_element_by_xpath("//*[@id='galaxy_nav']").click()

    # Scroll up through galaxy
    for i in range(20):
        time.sleep(1)
        SS_system = int(browser.find_element_by_xpath("//*[@id='solar_system']").get_attribute("value"))
        browser.find_element_by_xpath("//*[@id='solar_system']").clear()
        print(f"SS: {SS_system}")
        SS_system += 1
        browser.find_element_by_xpath("//*[@id='solar_system']").send_keys(SS_system)
        browser.find_element_by_xpath("//*[@id='set_coordinates_form']/div[3]/span[1]/a/span").click()

    # Reset SS location to home
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='solar_system']").clear()
    browser.find_element_by_xpath("//*[@id='solar_system']").send_keys("249")

    # Scroll down through galaxy
    for i in range(20):
        time.sleep(1)
        SS_system = int(browser.find_element_by_xpath("//*[@id='solar_system']").get_attribute("value"))
        browser.find_element_by_xpath("//*[@id='solar_system']").clear()
        print(f"SS: {SS_system}")
        SS_system -= 1
        browser.find_element_by_xpath("//*[@id='solar_system']").send_keys(SS_system)
        browser.find_element_by_xpath("//*[@id='set_coordinates_form']/div[3]/span[1]/a/span").click()


class Target:
    def __init__(self, galaxy, system, planet):
        self.galaxy = galaxy
        self.system = system
        self.planet = planet


