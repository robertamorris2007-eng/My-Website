print("Enter student names and grades.")
print("Type 'done' as the student name to finish.")
print("Type -1 as the grade to finish entering grades for a student.\n")

total = 0          
count = 0          
highest = -1       
lowest = 101       

while True:
    name = input("Enter student name: ")

    if name == "done":
        break

    while True:
        grade = int(input(f"Enter grade for {name} (-1 to stop): "))

        if grade == -1:   
           
            break  

        if grade < 0 or grade > 100:  
            print("Invalid grade. Please enter between 0 and 100.")
            continue   

        total = total + grade
        count = count + 1

        if grade > highest:
            highest = grade
        if grade < lowest:
            lowest = grade

if count > 0:
    average = total / count
    print("\nResults")
    print(f"Number of grades: {count}")
    print(f"Average grade: {average}")
    print(f"Highest grade: {highest}")
    print(f"Lowest grade: {lowest}")
else:
    print("No grades were entered.")

