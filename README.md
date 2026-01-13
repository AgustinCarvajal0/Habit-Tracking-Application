# Habit Tracker App 

The habit tracker app is a program that aims to help their users with the creation and continuation of new habits they may want to take on, by monitoring their progress and giving them on-demand analysis of their habits


## Installation

First, the repository has to be cloned
```bash
git clone https://github.com/AgustinCarvajal0/Habit-Tracking-App
```

next, the directory has to be opened

```bash
cd Habit-Tracking-App
```

finally, the program can be run as intended executing

```bash
python menu.py
```


### Requirements

python 3.12

Libraries Used: json, datetime


## Usage 

When running menu.py, you will be met with a menu with all the possible actions by the user.

```bash
python3 main.py
```
```bash 
"Hello, and welcome to the habit tracking app."
"Please, select what you would like to do"

"1.- Check one of your habits as done."
"2.- Add a new habit."
"3.- Delete a habit "
"4.- Request analysis of the habits "
"5.- Request analysis of a specific habit "
"6.- Close the program "

"What are you going to do? select the number of the option"
```

The input has to be the number of the desired action.

The first option is to check one of the habits off. This will show the list of all habits, and ask the user which one they wish to
check. Once done, the streak is updated, and it is marked as done for the day/week

The user is also able to add new habits to their databases. The program asks for the users for the name, periodicity, timespan, details. The rest of the attributes for the Habit class are automatically filled.

There is also the chance to delete a habit, in case the user chooses that they no longer want to keep track of it. It simply requires the name of the habit, and it will be deleted from the data base.

Alongside that, there is the option to receive the analysis of all the habits, that prints all the habits and their streak, as well as listing them from the longest streak, to shortest.

In the case of the analysis of a sample habit, the outcome of "request analysis of a specific habit" would be a description, including facts
like the last time it was checked, the streak, and whether the user surpassed their streak goal.

An example of the app would be the request of the analysis of a habit. In that case the app would output the following text.

```bash
"Here is the current status of your habit in detail 

This is a weekly Habit

It was last done on the 2026-01-05 

The habit Bouldering has been done for 6 straight weeks 

That is more than you initial goal of a 5 week(s) streak! Well Done! 

The details provided for the habit were: 
Going every weekend to do some rock climbing with friends"
```

## Structure

The whole information is stored in a json file, in a list of dictionaries with all the information of the habit. It is opened and edited whenever the user makes changes to the habits. It is very organized not only for humans, but also very easy to read for the app.

```json
    {
        "name": "Bouldering",
        "timespan": 5,
        "periodicity": false,
        "details": "Going every weekend to do some rock climbing with friends",
        "check": true,
        "streak": 6,
        "last_check": "2026-01-06",
        "history": [
            "2025-12-03",
            "2025-12-10",
            "2025-12-17",
            "2025-12-23",
            "2026-01-02",
            "2026-01-06"
        ]
    },
```

### Attributes

The Habit is structured with different attributes, all with their respective use either for calculations or for the analysis.

1. Name: A String that serves both the user and the program to differentiate the different objects.

2. Timespan: The amount of days or weeks for which the user wishes to fulfill their habit. This is made in order to set a streak goal.

3. Periodicity: Determines whether the habit is weekly or daily. In case it is daily, it is set to True. If it is weekly, False.

4. Details: Details added by the user themselves. These are not used by the program, but allows the user to add more information in case they need it.

5. Check: Boolean variable that states whether the user has checked their habit within their periodicity.

6. Last Check: States the last day where the user checked their habit. The format is "isoformat" (yyyy-mm-dd).

7. History: List of all the dates in which the habit was checked by the user.

