def AsianStandard(_grade):
    if _grade == "A" or 90.00 <= _grade <= 100.00:
        return "are Average"
    elif _grade == "B" or 80.00 <= _grade <= 89.99:
        return "are Below Average"
    elif _grade == "C" or 70.00 <= _grade <= 79.99:
        return "can't eat"
    elif _grade == "D" or 60.00 <= _grade <= 79.99:
        return "don't come home"
    elif _grade == "F" or 0 <= _grade <= 59.99:
        return "should find new family"
    else:
        return "Unvalid grade"
   