import string, random, sqlite3

connection = sqlite3.connect("passwordsqlite.db")
cursor = connection.cursor()

# users_info = []

def get_user():
    name = input("What is your name? (Enter 'q' to quit): ")
    if name == 'q':
        return False
    surname = input("What is your surname?: ")
    full_name = f"{name} {surname}"
    username = ''.join(random.sample(str(name + surname), k=6))
    password = ''.join(random.sample(string.ascii_letters + string.digits + "@$#€?!", k=15))
    return full_name, username, password

def get_users():
    users = []
    while True:
        user = get_user()
        if user:
            users.append(user)
        else:
            return users

users = get_users()

def database():
    cursor.execute("create table if not exists passwordsqlite(full name text, username text, password blob)")
    cursor.executemany("insert into passwordsqlite values(?,?,?)", users)
    for row in cursor.execute("select * from passwordsqlite"):
        print(row)
    connection.commit()

database()
print("Database has been updated")
connection.close()

# import sys; sys.exit()

# def username_password_generator():
#     user_info = []
#     while True:
#         name = input("What is your name? (Enter 'q' to quit): ")
#         if name == "q":
#             print("Thanks!")
#             break
#         surname = input("What is your surname? (Enter 'q' to quit): ")
#         if surname == "q":
#              print("Thanks!")
#              break
#         else:
#             full_name = f"{name} {surname}"
#             username = ''.join(random.sample(str(name + surname), k=6))
#             user_info.append(full_name)
#             user_info.append(username)
#             password = ''.join(random.sample(string.ascii_letters + string.digits + "@$#€?!", k=15))
#             user_info.append(password)
#             break
#     user_tuple = tuple(user_info)
#     users_info.append(user_tuple)
        
# # def formatted_info():
#     # filename = "username-info.txt"
#     # with open("username-info.txt", "a+") as file:
#     #     for item in user_info:
#     #         file.write(str(item))

# def function_loop():
#     steps = [username_password_generator()]
#     for item in steps:
#         result = steps

# function_loop()

# while True:
#     message = input("Do you want a new username and password? y/n: ")
#     if message == "n":
#         break
#     else:
#         function_loop()



# cursor.execute("create table if not exists passwordsqlite(full name text, username text, password blob)")
# cursor.executemany("insert into passwordsqlite values(?,?,?)", users_info)
# for row in cursor.execute("select * from passwordsqlite"):
#     print(row)

# connection.commit()
# print("Database has been updated")
# connection.close()