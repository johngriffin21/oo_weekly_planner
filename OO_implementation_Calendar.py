class Calendar():
    days = {"Monday": None,
            "Tuesday": None,
            "Wednesday": None,
            "Thursday": None,
            "Friday": None,
            "Saturday": None,
            "Sunday": None
}

    appointments = 0

    def __init__(self, day, stime, etime, details):
        self.day = day
        self.stime = stime
        self.etime= etime
        self.details = details

    def __str__(self):                     #This can be used for printing individual days
        return "On {}, You have {} From {} to {}".format(self.day, self.details, self.stime, self.etime)

    def time_taken(self, day, stime, etime):      #This checks if the time wanted for an appt is taken
        for x in range(days[day][0], days[day][1]):  # to check if an time is available, we iterate from the previous appts start time and see if...
            if int(stime) == x:  # any time between that matches the start time of new appt to be added
                print("The time {} - {} on {} is already taken sorry.".format(stime, etime,day))  # here we have matched it, so the time is unavailable..#  print("Here is {}'s schedule".format(day))  # a simple output message lets the user know this.
                print("For {}, you have an appointment of {} from {} to {}.".format(day, days[day][2], days[day][0],days[day][1]))
                return False
            return True

    def inday(self, dayy):  # Check if the days given are valid
        sevendays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        l = len(sevendays)
        for x in range(0, l):
            if dayy == sevendays[x]:            #this means that the input the user entered is equal to one of the...
                return True                     #days in the list above which makes it a valid day.
        print("This isn't a day, please try again") #No match so we return false whhich stops appointment from being made
        return False


    def appointment(self, day, stime, etime, details): #this instance method adds an appointment to the class variable days
        days = Calendar.days
        if not self.inday(day):
            return "Invalid day"
        if days[day] != None:
            x = valid(stime)
            z = valid(etime)
            if time_taken(stime):  # The time is already taken so
                return "This time is already taken"
            if not x.time(stime) and not z.time(etime):  #uses the valid class to check if the time is valid(not above 60 mins etc)
                return "Invalid time(s) received"
            days[day].append(int(stime))  # the list already exist if we're in this loop, so appending each value works.
            days[day].append(int(etime))
            days[day].append(details)

            Calendar.appointments += 1
            return True  # return True to let the user know the appts been added.
        else:
            days[day] = [int(stime), int(etime),details]  # the day is empty, so we create a list as the values and add the respective figures into the list.
            Calendar.appointments += 1
            return True

    def remove_appointment(self,day, stime, etime,details):
        # this function will remove appointments if they are requested by the user
        days = Calendar.days
        days[day].remove(int(stime))  # use int stime etime etc in this as they are appended as these types
        days[day].remove(int(etime))
        days[day].remove(details)
        Calendar.appointments -= 1

    @classmethod
    def how_many(cls):
        print("You have {} appointments booked.".format(cls.appointments))  # prints how many appointments are booked

class valid():
    def __init__(self, t=0):
        self.t = t

    def time(self, t):  # Check if the times given are valid
        x = str(t)
        hr = x[:2]
        min = x[2:]
        hr1 = int(hr)
        min1 = int(min)
        if hr1 < 24 and min1 < 60:
            return True
        return False

class out():
    def __init__(self, day = " ", days = " "):
        self.day = day
        self.days = days


    def print_week(self, days):
        print("{:<12} {:<40} {:<10} {:<10}".format('Day:', 'Description:', 'Start:', 'End:'))
        for i in days:
            if days[i] == None or days[i] == []:  # The day has none as the value so the user hasn't entered any appointments for that day
                print("{:<12} {:<40} {:<10} {:<10}".format(i, 'No appts', 'N/A', 'N/A'))
            elif len(days[i]) == 3:  # If the user only has one appt for that day then where stime, dtime and details are in the list are fixed
                print("{:<12} {:<40} {:<10} {:<10}".format(i, days[i][2], days[i][0], days[i][1]))
            elif len(days[i]) > 3:  # The user has entered more than one appt for the day so I made something to iterate through the lit
                print("{:<12} {:<40} {:<10} {:<10}".format(i, days[i][2], days[i][0],days[i][1]))  # The first appt will always be fixed
                x = len(days[i])
                t = (x / 3)  # We use this to find the index we need to display (I change it later on to y as an index cant be a float)
                am = (x / 3) - 1  # We know now how many appts after the first one there is, ie 9 things in list would equal 3 appts therfore giving us a value of two after the first appt.
                amt = int(am)
                y = int(t)
                for q in range(0, amt):
                    print("{:<12} {:<40} {:<10} {:<10}".format("     ", days[i][y + 3], days[i][y + 1], days[i][y + 2]))
                    y += 3


    def print_day(self, day, days):
        print("{:<12} {:<40} {:<10} {:<10}".format('Day:', 'Description:', 'Start:', 'End:'))
        if len(days[day]) == 3:  # If the user only has one appt for that day then where stime, dtime and details are in the list are fixed
            print("{:<12} {:<40} {:<10} {:<10}".format(day, days[day][2], days[day][0], days[day][1]))
        elif len(days[day]) > 3:  # The user has entered more than one appt for the day so I made something to iterate through the lit
            print("{:<12} {:<40} {:<10} {:<10}".format(day, days[day][2], days[day][0],days[day][1]))  # The first appt will always be fixed
            x = len(days[day])
            t = (x / 3)  # We use this to find the index we need to display (I change it later on to y as an index cant be a float)
            am = (x / 3) - 1  # We know now how many appts after the first one there is, ie 9 things in list would equal 3 appts therfore giving us a value of two after the first appt.
            amt = int(am)
            y = int(t)
            for q in range(0, amt):
                print("{:<12} {:<40} {:<10} {:<10}".format("     ", days[day][y + 3], days[day][y + 1], days[day][y + 2]))
                y += 3

def main():

    print("Welcome to the appointment maker, please type any key to add an appointment or type 'Exit' & enter to leave")
    while input() != "Exit":
        print("Please enter the day you want to make an appointment for(Please use a capital letter to start the day:")
        day2 = input()
        print("Thanks, now please enter a start time for your appointment(24hrs ex: 1pm is 1300):")
        stime2 = input()
        print("Thanks, now please enter an end time for your appointment(24hrs ex: 1pm is 1300):")
        etime2 = input()
        print("Enter your details:")
        details2 = input()
        print("Please enter the details of your appointment:")
        c = Calendar(day2, stime2, etime2, details2)
        c.appointment(day2, stime2, etime2, details2)
        Calendar.how_many()
        print("Your appointment has now been added, please type any key to add an appointment or type 'Exit' & enter to leave")

    print("Would you like to remove an appointment ? Type 'Yes' if you do, 'No' if you dont.")
    x = input()
    while x == "Yes" or x == "yes":
        print("Please enter the day of the appointment you want to remove:")
        day = input()
        print("Thanks, now please enter a start time for that appointment(24hrs ex: 1pm is 1300):")
        stime1 = input()
        print("Thanks, now please enter an end time for that appointment(24hrs ex: 1pm is 1300):")
        etime1 = input()
        print("Please enter the details of that appointment:")
        details1 = input()
        c = Calendar(day, stime1, etime1, details1)
        c.remove_appointment(day, stime1, etime1, details1)
        Calendar.how_many()
        print("Your appointment is now removed. Type 'Yes' to remove another or 'No' to leave.")
        x = input()
    print("-"*120)
    x = out("None", Calendar.days)
    x.print_week(Calendar.days)
    print("-" * 120)
    print("If you want to see an individual day please type it here:")
    day = input()
    x = out(day, Calendar.days)
    x.print_day(day, Calendar.days)


    



if __name__ == '__main__':
    main()