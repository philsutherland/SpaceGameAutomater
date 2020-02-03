import sys
import os


# This function restarts the program
def restart_program():
    print("Restarting program")
    os.execlp(sys.executable, os.path.abspath(__file__), *sys.argv)


# This function re-runs the mainscript without restarting the entire script
def rerun(browser):
    print("Rerunning run method")
