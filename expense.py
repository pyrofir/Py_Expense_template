from PyInquirer import prompt
import csv

def get_users():
    f = open('./users.csv', 'r')
    lines = f.readlines()
    f.close()
    users = []
    for user in lines:
        users.append(user.rstrip('\n'))
    return users

def get_nbr_user():
    list = [str(i) for i in range(1,len(get_users()) + 1)]
    return list

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices":get_users(),
    },
]


expense_questions_multiple_spender = [
    {
        "type":"list",
        "name":"spender",
        "message":"Spender: ",
        "choices":get_users(),
    },
    {
        "type":"input",
        "name":"amount",
        "message":"Amount: (empty for equal repartition)",
    },
]

multi_spender = [
    {
        "type":"list",
        "name":"number_spender",
        "message":"How many spender: ",
        "choices":get_nbr_user(),
    },
]

total_amount_and_label = [
    {
        "type":"input",
        "name":"total_amount",
        "message":"Expense Total Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"Expense - Label: ",
    }
]



def new_expense(*args):
    
    
    f = open('./expense_report.csv', 'r')
    s = f.read()
    f.close
    b = False
    if (s == "") :
        b = True
    file = open('./expense_report.csv', 'a')
    writer = csv.DictWriter(file, fieldnames = ["amount", "label", "spender", "People involved"])

    if b:
        writer.writeheader()

        
    nbr_spender = int(prompt(multi_spender).get("number_spender"))

    if nbr_spender == 1:
        infos = prompt(expense_questions)
        writer.writerow({"amount":infos.get("amount"),'label':infos.get('label'), 'spender':infos.get('spender'), "People involved":infos.get('spender')})
        file.close()  
        print("Expense Added !")
        return True
    


    info_total = prompt(total_amount_and_label)

    total = int(info_total.get('total_amount'))
    label = info_total.get('label')

    rows = []
    for _ in range(nbr_spender) :


        infos = prompt(expense_questions_multiple_spender)
        amount = infos.get('amount')
        
        if amount == "" :
            amount = total / nbr_spender
        else :
            amount = int(amount)


        spender = infos.get('spender')
        rows.append([str(amount), spender])
        #writer.writerow({"amount": str(amount),"label":label,"spender":spender})
    
    involved = rows[0][1]

    for i in range(1, nbr_spender):
        involved = involved + ' - ' + rows[i][1]

    for elm in rows:
        writer.writerow({"amount":elm[0],'label':label, 'spender':elm[1], "People involved":involved})

    file.close()
    
    print("Expense Added !")
    return True


