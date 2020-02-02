import selenium
from restart import restart


def check_for_lucky_draw(browser):
    # Check if lucky draw is activated
    try:
        browser.find_element_by_xpath("//*[@id='roll_button']").click()
        # Need to somehow check if lucky draw has multiple ones
    except BaseException as e:
        print("Error: A problem occured while trying to check for lucky draw")
        print(f"Specific Error {e}")
        restart()
