global min_year
global max_year
min_year = 1800
max_year = 9999
months = [31,28,31,30,31,30,31,31,30,31,30,31]

class Date(object):

    # def __int__(self):
    #     self.day = 1
    #     self.month = 1
    #     self.year = 2000
    #     self.printdate()
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

        self.printdate()

    def isLeapYear(self,year):
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def isValidDate(self):

        if self.month < 1 or self.month > 12:
            return False

        if self.year < min_year or self.year > max_year:
            return False

        isLeap = self.isLeapYear(self.year)


        if (isLeap and self.month == 2) and  (self.day < 1 or self.day > 29):
            return False

        elif(isLeap and self.month == 2) and  (self.day >= 1 or self.day <= 29):
            return True

        if self.day < 1 or self.day > months[self.month-1]:
            return False

        return True


    def printdate(self):

        if self.isValidDate():
            if self.day < 9:
                print('0' + str(self.day) + '/', end="")
            else:
                print(str(self.day) + '/', end="")

            if self.month < 10:
                print('0' + str(self.month) + '/', end="")
            else:
                print(str(self.month) + '/', end="")

            print(str(self.year))
        else:
            print("Entered date is not correct")

    def addDays(self,days):
        if days < 1:
            print("Enter days greater than 0 ")
            return

        self.day += days
        ly = self.isLeapYear(self.year)
        if ly :
            months[1] = 29
        else:
            months[1] = 28
        while self.day > months[self.month-1]:
            if ly and self.month == 2:
                self.day -= 29

            else:
                self.day -= months[self.month-1]

            self.month +=1

            if self.month >12:
                self.month = self.month % 12
                self.year +=1
                ly = self.isLeapYear(self.year)
                if ly : months[1]= 29
                else: months[1] = 28

        print("Date after adding {} days ".format(days))
        self.printdate()



date1 = Date(12,2,2000)
date1.addDays(400)