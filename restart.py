import sys
import os


# This function restarts the program
def restart():
    print("Restarting program")
    os.execlp(sys.executable, os.path.abspath(__file__), *sys.argv)
