"""
data access layer
"""

import json

def load_questions():
    filepath = "C:\\Users\\acer\Desktop\STUDY\pycharm\MBA\models\\all_questions.py"
    with open(filepath, "r") as foo:
        return json.load(foo)

question_set = load_questions()