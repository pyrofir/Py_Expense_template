from PyInquirer import prompt
import csv
user_questions = [
    {
        "type":"input",
        "name":"user",
        "message":"New user -- Name: ",
    }
]

def add_user():

    infos = prompt(user_questions)


    new_user = infos.get("user")

    f = open('./users.csv', 'r')
    lines = f.readlines()
    for line in lines:
        if line == new_user :
            print("user already exist")
            f.close
            return True
    f.close
    

    file = open('./users.csv', 'a')
    writer = csv.writer(file)
    writer.writerow([new_user])
    file.close()

    print("user added")

    return True