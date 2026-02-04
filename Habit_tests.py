from genericpath import exists
import unittest
import json
import Habit_tracker_app
from datetime import date, timedelta
from Habit_Class import Habit

class FakeHabitName:
            def __init__(self, name) :
                self.name = name

            def to_dict(self):
                return {"name": self.name}

class test_test(unittest.TestCase):

    def test_find_habit_name(self):
        
        habit = FakeHabitName("Reading")

        database = [habit]

        result = Habit_tracker_app.find_habit("Reading", database)

        assert result == habit

    
    def test_find_habit_invalid(self):

        habit = FakeHabitName("Reading")

        database = [habit]

        result = Habit_tracker_app.find_habit("XYZ", database)

        assert result == None

    
    """update_streak/check_habit daily"""

    def test_update_streak_first_time(self):
          
        habit = Habit("Leer", 31, True, "Placeholder", False, 0, None, [])

        test_today = date.today()
        habit.check_habit()
        habit.update_streak()

        assert habit.streak == 1
        assert habit.last_check == str(test_today)
    
    def test_update_streak_consecutive(self):

        test_today = date.today()

        yesterday = test_today - timedelta(days = 1)
          
        habit = Habit("Leer", 31, True, "Placeholder", False, 1, str(yesterday), [str(yesterday)])

        habit.check_habit()
        habit.update_streak()

        assert habit.streak == 2
        assert habit.last_check == str(test_today)

    def test_update_streak_broken(self):

        test_today = date.today()

        day_before_yesterday = test_today - timedelta(days = 2)
          
        habit = Habit("Leer", 31, True, "Placeholder", False, 1, str(day_before_yesterday), [str(day_before_yesterday)])

        habit.check_habit()
        habit.update_streak()

        assert habit.streak == 1
        assert habit.last_check == str(test_today)

    def test_update_streak_same_day(self):

        test_today = date.today()
        yesterday = test_today - timedelta(days = 1)
          
        habit = Habit("Leer", 31, True, "Placeholder", True, 2, str(test_today), [str(test_today), str(yesterday)])

        habit.check_habit()
        habit.update_streak()

        assert habit.streak == 2
        assert habit.last_check == str(test_today)
    


    """update_streak/check_habit weekly"""
    
    def test_update_streak_consecutive_week(self):

        test_today = date.today()
          
        habit = Habit("Leer", 6, False, "Placeholder", False, 1, str("2026-01-29"), [str("2026-01-29")])

        habit.check_habit()
        habit.update_streak()

        assert habit.streak == 1
        assert habit.last_check == str(test_today)

    
    
def test_save_habits(tmp_path ):
        
    archivo = tmp_path / "habits.json"

    habits = [
    FakeHabitName("leer"),
    FakeHabitName("ejercicio")
]
    Habit_tracker_app.save_json(habits, archivo)

    assert archivo.exists()

    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "leer"
    assert data[1]["name"] == "ejercicio"


def test_add_habit_success():
    habits = []
    habit = FakeHabitName("leer")

    result = Habit_tracker_app.add_habit(habits, habit)

    assert result is True
    assert len(habits) == 1

def test_add_habit_duplicate():
    habit = FakeHabitName("leer")
    habits = [habit]

    result = Habit_tracker_app.add_habit(habits, FakeHabitName("leer"))

    assert result is False
    assert len(habits) == 1

    