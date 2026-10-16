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

    # 2. Get Desktop directory path dynamically
    desktop_path = Path.home()
    print(f"Desktop Path: {desktop_path}")

    
    # 3. List files on the Desktop
    print("\n--- Files on Home Directory ---")
    files = list(desktop_path.iterdir())
    if not files:
        print("No files found on Home Directory.")

    else:
        for item in files:
            file_type = "DIR" if item.is_dir() else "FILE"
            size_kb = item.stat().st_size / 1024 if item.is_file() else 0
            print(f"[{file_type}] {item.name:<30} ({size_kb:.1f} KB)")  

    current_os = platform.system()
    
    # 4. Write an output summary report on the Desktop
    report_file = desktop_path / "desktop_audit_report.txt"
    try:
        report_file.write_text(
          f"Audit Executed Successfully on {current_os}\n"
          f"Total Items scanned on Desktop :{len(files)}\n"
        )  
        print(f"\n[+] Created summary report: {report_file.name}")
    except PermissionError:
     print("\n Permission denied")

    print("++++++++++++++++++++++++++++++")    

# Run statement to check if the script is being run directly    
if __name__ == "__main__":
    run_windows_audit()


# Keeps the command Prompt window open if double-clicked in windows Explorer
if platform.system() == "Windows":
    input("\nPress Enter to exit...")