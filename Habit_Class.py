from datetime import datetime, timedelta, date


class Habit:

    def __init__(self, name = str , ts = int, period = bool, details = str,
                  checked = bool, streak = 0, last_check = None, history = None):
        """
        Initializes a new Habit instance.

        Args:
            name (str): Name of the habit.
            timespan (int): Amount of days that the user wishes to complete the habit for.
            period (bool): Habit periodicity. True for daily habits, False for weekly habits.
            details (str): Additional information or notes about the habit.
            checked (bool): Indicates whether the habit has been checked for the current period.
            streak (int, optional): Current streak count. Defaults to 0.
            last_check (date or None, optional): Date of the last completion.
            history (list or None, optional): List of past completion dates.
        """

        self.name = name
        self.timespan = ts 
        self.periodicity = period #if True, periodicity = daily. if False, periodicity = weekly
        self.details = details
        self.checked = checked
        self.streak = streak
        self.last_check = last_check
        self.history = history

    def __str__(self) -> str:
        return f"{self.name}; {self.timespan}; {self.periodicity}; {self.details};
          {self.checked}; {self.streak}; {self.last_check}; {self.history}"

    def check_habit(self):
        today = date.today().isoformat()
        if self.history == None:
            self.history.append(today)
            self.last_check = today
            
        if self.history != None:
            if today not in self.history:
                self.history.append(today)
                self.last_check = today
        self.checked = True

    def to_dict(self):
        return {
            "name": self.name,
            "timespan": self.timespan, 
            "periodicity": self.periodicity,
            "details": self.details,
            "check":self.checked, 
            "streak" :self.streak,
            "last_check": self.last_check,
            "history" : self.history
        }
    
    @classmethod
    def from_dict(cls, data):
        return(cls(data["name"],
                     data["timespan"],
                     data["periodicity"],
                     data["details"],
                     data["check"],
                     data["streak"],
                     data["last_check"],
                     data["history"]))
 
    def update_streak(self):


        """
        Updates the habit streak based on completion history and periodicity.

        For daily habits, the streak is calculated by counting back the consecutive days
        up to the current date present in the habit history. If the previous day
        is missing, the streak counter stops and updates the streak.

        For weekly habits, the streak is updated based on whether the habit was
        completed in consecutive calendar weeks, including correct handling of
        year transitions.

        The method updates the streak value and records the current date as the
        last check. This method does not return a value.
        """

        if not self.history:
            self.streak = 1
            return
        
        dates = []
        today_t = date.today()

        for d in self.history:
            year, month, day = d.split("-")
            dates.append(date(int(year), int(month), int(day)))


        if self.periodicity == True: #daily
            helper = today_t
            yesterday = helper - timedelta(days = 1)
            self.streak = 0

            if yesterday not in dates:
                print("\n You lost your streak! Back to square one")


            while helper in dates:
                self.streak += 1
                helper -= timedelta(days = 1)


        if self.periodicity == False: #weekly

            year, month, day = self.last_check.split("-")
            last_check_to_date = datetime(int(year), int(month), int(day))

            last_checked_week = (last_check_to_date.isocalendar().year, last_check_to_date.isocalendar().week)

            helper = (today_t.isocalendar().year, today_t.isocalendar().week)

            if last_checked_week == helper:
                "You have already checked this week"
                pass
            
            if last_checked_week != helper:
                if (last_checked_week[1] + 1 == helper[1] and last_checked_week[0] == helper[0]) or \
                    (last_checked_week[1] == 53 and helper[1] == 1 and last_checked_week[0] + 1 == helper[0]):
                    self.streak += 1               
                else:
                    self.streak = 1

        self.last_check = today_t.isoformat()



    def habit_analysis(self):

        """
        Displays a detailed status report of the habit's progress.

        The method prints information about the habit, including its periodicity
        (daily or weekly), last checked date, current streak length, and
        progress toward the defined target timespan. If the goal has been reached, 
        exceeded or not yet completed, a corresponding message is displayed. Additional habit
        details provided by the user are also shown.

        This method outputs information to the console and does not return a value.
        """

        print("Here is the current status of your habit in detail \n")       
        if self.periodicity == True:
            print("This is a daily Habit\n")           
            print("It was last done on the " + str(self.last_check) + " \n")
            print("The habit " + self.name + " has been done for " + str(self.streak)+" straight days \n")

            if int(self.timespan) < int(self.streak):
                print("That is more than you initial goal of a " + str(self.timespan) + " day(s) streak! Well Done! \n")

            if int(self.timespan) > int(self.streak):
                time_left = int(self.streak) - int(self.timespan) 
                absolute_time_left = abs(int(time_left))
                print("You still need " + str(absolute_time_left) + " day(s) until fully achieving your goal of " + str(self.timespan)+" days. \n")

            if int(self.timespan) == int(self.streak):
                print("Congratulations! You just completed your goal of " + str(self.streak) + " days completing your new habit. \n")

        
        if self.periodicity == False:
            print("This is a weekly Habit\n")           
            print("It was last done on the " + str(self.last_check) + " \n")
            print("The habit " + self.name + " has been done for " + str(self.streak)+" straight weeks \n")

            if int(self.timespan) < int(self.streak):
                print("That is more than you initial goal of a " + str(self.timespan) + " week(s) streak! Well Done! \n")

            if int(self.timespan) > int(self.streak):
                time_left = int(self.streak) - int(self.timespan) 
                absolute_time_left = abs(int(time_left))
                print("You still need " + str(absolute_time_left) + " week(s) until fully achieving your goal of " + str(self.timespan)+" weeks. \n")

            if int(self.timespan) == int(self.streak):
                print("Congratulations! You just completed your goal of " + str(self.streak) + " weeks completing your new habit. \n")
        
        print("The details provided for the habit were: \n " + str(self.details))