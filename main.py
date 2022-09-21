import argparse
import os
import psutil
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
    process_count = 0
    for p in psutil.process_iter():
        if process in p.name():
            process_count += 1
    if process_count >= 3:
        print("Processes are running normal.")
    else:
        print(f"Check process {process}. ")



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

    # Open browser to URLs, OBS, and nginx (Atom for now)
    open_tools()

    # Check certain processes
    check_processes("atom")


if __name__ == "__main__":
    main()
