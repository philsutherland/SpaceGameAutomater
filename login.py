import selenium
from restart import restart


def login(browser):
    #  Open webpage
    try:
        browser.implicitly_wait(5)
        browser.get("https://uni2.playstarfleetextreme.com/")
    except BaseException as e:
        print("Error: Could not access game website")
        print(f"Specific Error {e}")
        restart()

    # Log into game
    try:
        browser.find_element_by_id(
            "tab-existing_account_sign_in_starfleet").click()
        browser.find_element_by_xpath("//*[@id='remember_me']").click()
        browser.find_element_by_xpath(
            "//*[@id='login']").send_keys("Das Engineer")
        # You can't find the element by its id since there are two id's with the name "password"
        browser.execute_script(
            "document.getElementsByClassName('mainForm')[3].value='pwd4phil'")
        browser.find_element_by_xpath("//*[@id='signInNow']").click()
    except BaseException as e:
        print("Error: A problem occured while trying to login")
        print(f"Specific Error {e}")
        restart()
