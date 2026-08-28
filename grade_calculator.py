name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

if not (0 <= maths <= 100 and 0 <= science <= 100 and 0 <= english <= 100):
    print("Invalid marks! Marks must be between 0 and 100.")
else:
    total = maths + science + english
    average = total / 3

    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average:", average)

    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 60:
        print("Grade: C")
    elif average >= 50:
        print("Grade: D")
    else:
        print("Grade: F")
