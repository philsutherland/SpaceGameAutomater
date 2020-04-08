import sys
import os
import time


# This function restarts the program
def restart_program():
    print("Restarting program")

    # Pause to prevent endless loop refreshes
    time.sleep(2000)

    os.execlp(sys.executable, os.path.abspath(__file__), *sys.argv)


# This function re-runs the mainscript without restarting the entire script
def rerun(browser):
    print("Rerunning run method")

    # Pause to prevent endless loop refreshes
    time.sleep(2000)

    # Rerun program
    # Temp code to restart vs rerun
    os.execlp(sys.executable, os.path.abspath(__file__), *sys.argv)
