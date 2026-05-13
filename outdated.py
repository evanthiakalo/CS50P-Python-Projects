months= {
    "January":"01",
    "February":"02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June":"06",
    "July":"07",
    "August": "08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12",

}

while True:
    date= input("Date: ").strip()

    try:

        if "/" in date:
            month, day, year = date.split("/")
            month = int (month.strip())
            day= int(day.strip())
            year = int(year.strip())
            month_str = f"{month:02d}"


        else:
            parts = date.replace(",", "").split()
            month_str= months [parts[0].capitalize()]
            day = int(parts[1])
            year = int(parts[2])



        if 1<= int (day)<= 31 and 1<= int (month_str)<=12:
            print(f"{year:04d}-{month_str}-{day:02d}".replace(":", "-"))
            break
        else:
            pass
    except (KeyError, ValueError):
        pass


