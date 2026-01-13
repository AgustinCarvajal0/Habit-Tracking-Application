import Habit_tracker_app

def menu():

    print("\n Hello, and welcome to the habit tracking app. \n Please, select what you would like to do \n")
    print("1.- Check one of your habits as done.")
    print("2.- Add a new habit.")
    print("3.- Delete a habit ")
    print("4.- Request analysis of the habits ")
    print("5.- Request analysis of a specific habit ")
    print("6.- Close the program ")

    value_input = input("\n What are you going to do? (select the number of the option) \n")

    if value_input == str(1):
        Habit_tracker_app.check_a_habit()
        menu()
    if value_input == str(2):
        Habit_tracker_app.create_habit()
        menu()
    if value_input == str(3):
        Habit_tracker_app.delete_habit()
        menu()
    if value_input == str(4):
        print(Habit_tracker_app.request_overall_analysis())
        menu()
    if value_input == str(5):
        Habit_tracker_app.specific_habit_analysis()
        menu()
    if value_input == str(6):
        print("\n Goodbye!")
        pass

menu()