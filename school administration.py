import csv


def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact number", "Email-ID"])

        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    studentnumber=1

    while (condition):
        student_info = input("Enter details of the student number: {} in the format Name Age Mobile_number Email-ID: ".format(studentnumber))
        student_info_list = student_info.split(' ')
        print("Check if the given details are correct\nName: {}\nAge: {}\nContact Number: {}\nEmail-ID: {}"
                    .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        check=input("Enter yes if correct or else enter no")

        if check=="yes":
            write_into_csv(student_info_list)

            choice = input("Do you want to take more entries?(yes/no): ")
            if choice == "yes":
                condition = True
                studentnumber=studentnumber+1
            elif choice == "no":
                condition = False
        elif check=="no":
            print("RE-enter the values")
