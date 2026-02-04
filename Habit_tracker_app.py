import json
from datetime import date
from Habit_Class import Habit
    
def load_json(filename = "Habit_Database.json"):
    with open(filename, "r") as archivo:
        data = json.load(archivo)
        return [Habit.from_dict(d) for d in data]


def save_json(habits, filename = "Habit_Database.json"):
    with open(filename, "w") as archivo:
        json.dump([t.to_dict() for t in habits], archivo, indent=4, ensure_ascii=False)

def find_habit(user_input, database):
    for index, habit in enumerate(database, 1):
        if user_input == habit.name or user_input == str(index):
            return habit
        pass

def add_habit(habit_list, new_habit):

    for h in habit_list:
        if new_habit.name == h.name:
            return False
    
    habit_list.append(new_habit)
    return True




def create_habit():

    try:
        habits_list = load_json()
    except FileNotFoundError:
        habits_list = []

    helper = False
    helper_list = []
    new_name = input("Please insert the name of your brand new Habit: ")

    for h in habits_list:
        if new_name == h.name:
            new_name = input("That name is already taken. Choose a new one: ")
    
    new_periodicity = input("Please enter the frequency in which you would like to complete the habit ('d' for daily, 'w' for weekly): ")

    while helper == False:
        if new_periodicity == str("d"):
            period = True
            helper = True

        if new_periodicity == str("w"):
            period = False
            helper = True

        if helper == False:
            new_periodicity = input("Please enter a valid input following the stated instructions ('d' for daily, 'w' for weekly): ")

    if new_periodicity == "d":
        timespan = input("Please state the amount of days that you want to keep this habit streak for: ")

    if new_periodicity == "w":
        timespan = int(input("Please state the amount of weeks that you want to keep this habit streak for: "))
            
    #if True, periodicity = daily. if False, periodicity = weekly
    new_details = str(input("Add any details you would like to the habit: "))
    today = date.today().isoformat()
    helper_list.append(today)

    new_habit = Habit(new_name, timespan, period, str(new_details), False, 0, None, [])

    if add_habit(habits_list, new_habit):
        save_json(habits_list)

    print("Your New habit has been added to the database \n")



def delete_habit():

    print("Your current habits are: \n")
    opened_database = load_json()
    contador = 1
    habits_to_keep = []
    list_of_inputs = []
    deleted = None

    for habit in opened_database:
        print(str(contador)+ ".- " + habit.name)
        contador += 1
        valid_inputs = {
            "name": habit.name,
            "number": str(contador - 1)
        }
        list_of_inputs.append(valid_inputs)

    deleted_o = input("\n Please type the name or number of the habit you wish to delete: \n")    
    for h in list_of_inputs:

        if deleted_o == h["name"] or deleted_o == h["number"]:
            deleted = h["name"]

    if deleted == None:
        print("This is an unvalid input! Try again")
        return


    with open("Habit_Database.json","w") as archivo:

        for linea in opened_database:

            if str(deleted).lower() != str(linea.name).lower():
                habits_to_keep.append(linea)

            if str(deleted).lower() == str(linea.name).lower():
                print("Habit successfully deleted \n")
    save_json(habits_to_keep)



def check_a_habit():

    print("Your current habits are: \n")
    opened_database = load_json()

    list_of_inputs = []
    contador = 1

    for habit in opened_database:
        print(str(contador)+ ".- " + habit.name)
        contador += 1
        valid_inputs = {
            "name": habit.name,
            "number": str(contador - 1)
        }
        list_of_inputs.append(valid_inputs)

    checked_o = input("\n Please type the name or number of the habit you wish to check: \n")    
    for h in list_of_inputs:

        if checked_o == h["name"] or checked_o == h["number"]:
            checked = h["name"]

    if checked == None:
        print("This is an unvalid input! Try again")
        return

    for i in opened_database:
        if i.name == checked:
            print("\n")
            i.update_streak()
            i.check_habit()
    
    save_json(opened_database)



def request_overall_analysis():

    habits_list = load_json()
    current_habits = list()
    
    def streak(e):
        return e[1]


    for habits in habits_list:
        habits.update_streak()
        name_and_streak_and_period = (habits.name, habits.streak, habits.periodicity)
        current_habits.append(name_and_streak_and_period)
    
    current_habits.sort(reverse = True, key = streak)

    printed_week = []
    printed_day = []

    count_daily = 1
    count_week = 1
    for habits in current_habits:
        if habits[2] == True:
            current_message = str(count_daily) + ".- The habit " + habits[0] + " is on a "+ str(habits[1]) +" day streak \n"
            printed_day.append(current_message)
            count_daily += 1

        if habits[2] == False:
            current_message = str(count_week) + ".- The habit " + habits[0] + " is on a "+ str(habits[1]) +" week streak \n"
            printed_week.append(current_message)
        
            count_week += 1
    
    print("The list of the longest streak for daily streaks is: \n")
    for item in printed_day:
        print(str(item))

    print("The list of the longest streak for weekly streaks is: \n")
    for item in printed_week:
        print(str(item))


def specific_habit_analysis():

    print("Your current habits are: \n")
    opened_database = load_json()
    list_of_inputs = []
    contador = 1

    for habit in opened_database:
        print(str(contador)+ ".- " + habit.name)
        contador += 1
        valid_inputs = {
            "name": habit.name,
            "number": str(contador - 1)
        }
        list_of_inputs.append(valid_inputs)

    analyzed_o = input("\n Please type the name or number of the habit you wish to analyze: \n")    
    for h in list_of_inputs:

        if analyzed_o == h["name"] or analyzed_o == h["number"]:
            analyzed = h["name"]

    if analyzed == None:
        print("This is an unvalid input! Try again")
        return

    for habit in opened_database:
        if habit.name == analyzed:
            habit.habit_analysis()

    pass



