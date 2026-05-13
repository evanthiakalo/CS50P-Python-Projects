import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate (ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for group in matches.groups():

            if group.startswith("0") and len(group)>1:
                return False
            if int(group) >255:
                return False
        return True
    return False
if __name__ == "__main__":
    main()
