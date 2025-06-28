#list to store exam schedules
exams = []

#function to add exam details
def add_exam():
    #ask user for exam details
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
    room = input("Enter assigned room: ")

#dictionary for storing exams
    exam = {
        "name": name,
        "date": date,
        "time": time,
        "room": room
    }

#add an exam to the list "exams"
    exams.append(exam)
    print("Exam was added successfully.\n")

#function to view stored exams
def view_exams():
    if not exams:
        print("You have no scheduled exams yet.\n")
        return
    print("\n Scheduled Exams:")
    #loop exam list and print
    for i, exam in enumerate(exams, start=1):
        print(f"{i}. {exam['name']} - {exam['date']} at {exam['time']} in Room {exam['room']}")
    print()

#function to edit stored exams
def edit_exam():
    #show the exams
    view_exams()
    if not exams:
        return
    try:
        #ask user for the number of the exam to edit
        index = int(input("Enter exam number to edit: ")) - 1
        if 0 <= index < len(exams):
            #lets user update details about the exams
            print("Leave field blank to keep current value.")
            name = input(f"New name (current: {exams[index]['name']}): ") or exams[index]['name']
            date = input(f"New date (current: {exams[index]['date']}): ") or exams[index]['date']
            time = input(f"New time (current: {exams[index]['time']}): ") or exams[index]['time']
            room = input(f"New room (current: {exams[index]['room']}): ") or exams[index]['room']
            #update dictionary with the updated values
            exams[index] = {"name": name, "date": date, "time": time, "room": room}
            print("Exam updated successfully!\n")
        else:
            print("Invalid exam number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

#function to delete exams
def delete_exam():
    view_exams() #show the exams
    if not exams:
        return
    try:
        #ask user for the number of the exam to delete
        index = int(input("Enter exam number to delete: ")) - 1
        if 0 <= index < len(exams):
            removed = exams.pop(index)
            print(f" Exam '{removed['name']}' deleted successfully!\n")
        else:
            print("Invalid exam number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

#program execution/loop
def main():
    while True:
        #display the menu
        print(" SMART SCHEDULER MENU")
        print("1. Add New Exam")
        print("2. View All Exams")
        print("3. Edit Exams")
        print("4. Delete Exams")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        #handle user choices
        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print(" Exiting Smart Scheduler. Goodbye!")
            break #exit loop and terminate program
        else:
            print("Invalid option. Please try again.\n")

#to ensure that main function only runs if script is executed directly
if __name__ == "__main__":
    main()