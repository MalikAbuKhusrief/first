# This is a simple Python script 
import os
import sys
import platform
from pathlib import Path

# this is the first function
def run_windows_audit():
    print("=========================================")
    print("Running Windows Audit...")
    print("=========================================") 

    # 1. Detect Operating System
    os_name = platform.system() 
    print(f"Detected Operating System: {os_name}")
    print(f"Detected OS Version: {platform.version()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Detected OS Release: {platform.release()}")

# Run statement to check if the script is being run directly    
if __name__ == "__main__":
    run_windows_audit()
t6t