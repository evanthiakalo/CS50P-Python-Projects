import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert (s):
    match = re.search(
        r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$",
        s
    )


    if not match:
        raise ValueError
    h1,m1,p1,h2,m2,p2 = match.groups()

    def to_24(h,m,p):
        h = int(h)
        m = int (m) if m else 0

        if h<1 or h>12 or m>59:
            raise ValueError
        if p == "AM":
            if h == 12:
                h= 0
        else:
            if h != 12:
                h += 12

        return f"{h:02}:{m:02}"
    start = to_24(h1, m1, p1)
    end = to_24(h2, m2, p2)

    return f"{start} to {end}"
if __name__ == "__main__":
    main()
