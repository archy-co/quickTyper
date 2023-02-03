import sys
import os
import random

def main():
    print("Enter string: ")
    line = sys.stdin.readline()
    os.system("sleep 3")

    xdotool_cmd = "xdotool key --delay 2 "

    for char in line:
        os.system("sleep " + str(random.uniform(0, 0.02)))

        if char == ";":
            os.system(xdotool_cmd + "semicolon")
        elif char == "'":
            os.system(xdotool_cmd + "apostrophe")
        elif char == " ":
            os.system(xdotool_cmd + "space")
        elif char == ".":
            os.system(xdotool_cmd + "period")
        elif char == ",":
            os.system(xdotool_cmd + "comma")
        elif char == "?":
            os.system(xdotool_cmd + "question")
        elif char == ":":
            os.system(xdotool_cmd + "colon")
        elif char == "!":
            os.system(xdotool_cmd + "exclam")
        else:
            os.system(xdotool_cmd + char)

if __name__ == "__main__":
    main()
