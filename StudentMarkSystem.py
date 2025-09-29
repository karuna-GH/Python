class studentManagement:

    def __init__(self):
        self.marks = []

    def add_marks(self):

        subject1 = int(input("Enter First Subject marks : "))
        subject2 = int(input("Enter Second Subject marks : "))
        subject3 = int(input("Enter Third Subject marks : "))
        subject4 = int(input("Enter Fourth Subject marks : "))
        subject5 = int(input("Enter Fifth Subject marks : "))

        if (0 <= subject1 <= 100 and
                0 <= subject2 <= 100 and
                0 <= subject3 <= 100 and
                0 <= subject4 <= 100 and
                0 <= subject4 <= 100):
            self.marks.append(subject1)
            self.marks.append(subject2)
            self.marks.append(subject3)
            self.marks.append(subject4)
            self.marks.append(subject5)

            print("Marks added successfully")

    def show_marks(self):
        if not self.marks:
            print("No Marks Entered Yet..!!!")
        else:
            print(self.marks)

    def calculateAverage(self):
        if not self.marks:
            raise IndexError("No Marks Entered Yet")
        else:
            avg = sum(self.marks)/len(self.marks)
            print(f"Your Average is : ",avg)

    def exit(self):
        print("Exiting the program")
try:

    obj = studentManagement()

    while True:
        print("\n1. Add Marks")
        print("2. Show All Marks")
        print("3. Show Average")
        print("4. Exit")

        user_choice = int(input("Enter Choice : "))

        if user_choice == 1:
            obj.add_marks()

        elif user_choice==2:
            obj.show_marks()

        elif user_choice==3:
            obj.calculateAverage()

        elif user_choice==4:
            obj.exit()
            break

        else:
            print("Enter Proper Number ")

except ValueError:
    print("Value not properly entered")
except Exception as e:
    print("ERROR : Something went wrong. ",e)
