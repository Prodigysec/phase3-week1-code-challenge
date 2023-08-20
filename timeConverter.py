def convert_to_24_hour(hour, minute, period):
    if (hour > 0 and hour <= 12) and (minute > 0 and minute <= 59) and (period == "am" or period == "pm"):
        if hour == 12:
            if period == "am":
                hour = 0
        elif hour != 12:
            if period == "pm":
                hour += 12
    else:
        return "Not a valid time format"
    