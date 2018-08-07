"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def score_output():
    score = float(input("Enter score: "))
    judgement = score_checker(score)
    print(judgement)

def score_checker(score):
    if score < 0 or score > 100:
        judgement = "Invalid score"
    elif score >= 50 and score < 90:
        judgement = "Passable"
    elif score >= 90:
        judgement = "Excellent"
    elif score < 50:
        judgement= "Bad"
    return judgement


score_output()




