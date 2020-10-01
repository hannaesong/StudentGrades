def NormalStandard(_grade):
    if _grade == "A" or 90.00 <= _grade <= 100.00:
        return "Great"
    elif _grade == "B" or 80.00 <= _grade <= 89.99:
        return "Good"
    elif _grade == "C" or 70.00 <= _grade <= 79.99:
        return "Average"
    elif _grade == "D" or 60.00 <= _grade <= 79.99:
        return "Okay"
    elif _grade == "F" or 0 <= _grade <= 59.99:
        return "Bad"
    else:
        return "Unvalid grade"
   