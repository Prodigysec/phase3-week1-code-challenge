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
        
    
    time_24_hour = f"{hour:02d}{minute:02d}"
    return time_24_hour


print(convert_to_24_hour(0, 30, "am"))  # Output: "Not a valid number"
print(convert_to_24_hour(13, 15, "pm"))  # Output: "Not a valid number"
print(convert_to_24_hour(1, 37, "pm"))  # Output: "1337"
print(convert_to_24_hour(12, 15, "am"))  # Output: "0015"
print(convert_to_24_hour(12, 18, "pm"))  # Output: "1218"
