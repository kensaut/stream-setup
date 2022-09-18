import argparse
import os
import webbrowser
import wmi


URLS = [
    "https://www.youtube.com",
    "https://www.facebook.com/",
    "https://www.twitch.tv/"
    ]



def open_tools():
    os.startfile("\\Users\\Ken\\Desktop\\church-example\\nginx-sample.txt")
    os.startfile("\\Users\\Ken\\Desktop\\church-example\\atom")
    for url in URLS:
        webbrowser.open_new_tab(url)


def check_processes(process):
    c = wmi.WMI()
    for p in c.Win32_Process():
        if process == p.Name:
            print(f"{process} is running.")
        else:
            print(f"{process} is not running.")



# Main function to run program
def main():
    # Initiates the program and parser
    parser = argparse.ArgumentParser(
        prog="Streaming setup",
        description="Set up streaming",
    )
    # Argument for time of service
    parser.add_argument(
        "-t", "--time",
        default="9:00",
        choices=["9:00", "11:00", "10:00"],
        required=True,
    )
    # Argument for sermon
    parser.add_argument(
        "-s", "--sermon",
        required=True,
    )
    args = parser.parse_args()

    # Open browser to URLs and nginx
    open_tools()

    # Check certain processes
    check_processes("notepad.exe")




if __name__ == "__main__":
    main()
