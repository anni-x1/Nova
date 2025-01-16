import subprocess

def open_calculator():
    try:
        # Open the calculator using the subprocess module
        subprocess.Popen("calc.exe")
        # print("Calculator opened successfully!")
        return "Calculator opened!"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while opening the calculator."