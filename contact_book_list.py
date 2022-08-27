import sqlite3
con = sqlite3.connect('users.db')

def dataEntry(name,phone,email):
    query = 'insert into users (NAME,PHONE,EMAIL) values(?,?,?)'
    con.execute(query, (name, phone, email))
    con.commit()
    print('New contact created')

def updateData(id, name, phone, email):
    query = 'update users set NAME=?, PHONE=?, EMAIL=? where ID=?;'
    con.execute(query, (name, phone, email, id))
    con.commit()
    print('New contact created')

def deleteData(id):
    query = 'delete from users where ID=?;'
    con.execute(query, id)
    con.commit()
    print('Data deleted')

print('1. Insert    2. Update    3.Delete')

default = 1

while default == 1:
    choice = int(input('Enter your option: '))

    if choice == 1:
        print('Insert new contact details: ')
        name=input('Enter the name: ')
        phone=input('Enter the phone number: ')
        email= input('Enter an email Id: ')
        dataEntry(name, phone, email)

    elif choice == 2:
        print('Update the fields: ')
        id = input('Enter the ID: ')
        name = input('Enter the name: ')
        phone = input('Enter the phone number: ')
        email = input('Enter an email Id: ')
        updateData(id, name, phone, email)

    elif choice == 3:
        print('Delete the data: ')
        id = input('Enter the ID: ')
        deleteData(id)

    else:
        print('Please enter valid option number: ')

    default = int(input('Enter 1 to continue or 0 to exit: '))

print('Thank You!!!')
