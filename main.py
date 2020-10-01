import os, sys
import LetToNumGrade
import NumToLetGrade
import AsianStandards
import NormalStandards

UserName = input("Enter you name: ")
_nGrade = float(input("Enter your grade in percentage: "))
UserAsian = (input("Are you Asian? Answer 'yes' or 'no': "))
UserAsian = UserAsian.lower()

print("\n")
_lGrade = NumToLetGrade.NumToLet(_nGrade)
print(f"{UserName} you letter grade is {_nGrade}; your percentage grade in the letter grading system is: {_lGrade}")

_aGrade = AsianStandards.AsianStandard(_nGrade)
_normGrade = NormalStandards.NormalStandard(_nGrade)
if UserAsian == 'yes':
    print(f"As an Asian, you {_aGrade}")
elif UserAsian == 'no':
    print(f"As a non-Asian, your grade is {_normGrade}")
else:
    print("Who are you then?")


print("\n")
