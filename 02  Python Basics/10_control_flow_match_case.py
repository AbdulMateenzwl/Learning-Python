# match-case is similar to switch-case from other languages (Python 3.10+)

day = "Friday"

match day:
    case "Monday":
        print("Start of work week")
    case "Friday":
        print("Almost weekend")
    case "Sunday":
        print("Rest day")
    case _:
        print("Midweek day")
