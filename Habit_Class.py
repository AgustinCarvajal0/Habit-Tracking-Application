from datetime import datetime, timedelta, date


class Habit:

    def __init__(self, name = str , ts = int, period = bool, details = str, checked = bool, streak = 0, last_check = None, history = None):
        self.name = name
        self.timespan = ts 
        self.periodicity = period #if True, periodicity = daily. if False, periodicity = weekly
        self.details = details
        self.checked = checked
        self.streak = streak
        self.last_check = last_check
        self.history = history

    def __str__(self) -> str:
        return f"{self.name}; {self.timespan}; {self.periodicity}; {self.details}; {self.checked}; {self.streak}; {self.last_check} ; {self.history}"


    def change_timespan(self, new_timespan):
        self.timespan = new_timespan
        
    def change_periodicity(self):
        if self.periodicity == False:
            self.periodicity = True
            pass
        if self.periodicity == True:
            self.periodicity = False
            pass
    
    def change_details(self, new_details):
        self.details = new_details
        print("The new details have been set!")

    def change_streak(self, new_streak):
        self.streak = new_streak
        print("Your new streak has been updated!")

    def check_habit(self):
        today = date.today().isoformat()
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

        if not self.history:
            self.streak = 1
            return
        
        dates = []
        today_t = date.today()

        for d in self.history:
            year, month, day = d.split("-")
            dates.append(date(int(year), int(month), int(day)))

        """daily streaks, periodicity == True"""
        if self.periodicity == True:
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