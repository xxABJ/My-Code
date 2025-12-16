# Testing basic sqlite database creations
import sqlite3


# Establish a connection, create a database
def get_connection(db_name):
    try:
        connection = sqlite3.connect(db_name)
        return connection
    
    except Exception as e:
        print(f"{e}: Could not establish a connection.\n")

# Create a table, Table is only knows as 'users', add argument and edit code to have more.
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
    )
    """

    try:
        with connection:
            connection.execute(query)
        print("Table has been created!\n")

    except Exception as e:
        print(f"{e}: Could not create table, might already exist.\n")

# Add a user
def insert_user(connection, name:str, age:int, email:str):
    query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"

    try:
        with connection:
            connection.execute(query, (name, age, email))
        print(f"User {name} was added to the datebase!\n")
    
    except Exception as e:
        print(f"{e}: User could not be added to the database.\n")

# Query all users in the Database
def fetch_users(connection, condition:str = None, value:str = None) -> list[tuple]: #(Ali, 27, ylllllb@outlook.com)
    query = "SELECT * FROM users"
    if condition:
        query += f" WHERE {condition} = ?"
        print(query+"\n")
        try:
            with connection:
                condition_rows = connection.execute(query, (value,))

                conditional_list = []
                for users in condition_rows:
                    conditional_list.append(users)

                if len(conditional_list) > 0:
                    return condition_rows
                else:
                    return print("Could not specify *condition and *value")

        except Exception as e:
            print(f"{e}: could not execute the contintion: {condition} ")
            print("Could not fetch all users from database.\n")
            return 

    try:
        with connection:
            rows = connection.execute(query)
        return rows

    except Exception as e:
        print(f"{e}: Could not fetch all users from database.\n")

# Delete a user
def delete_user(connection, user_id:int):
    query = "DELETE FROM users WHERE id = ?"
    condition = "id"
    value = user_id

    try:
        if fetch_users(connection, condition, value):
            print(f"User id: {user_id} found!")

            with connection:
                connection.execute(query, (user_id,))
            print(f" User id: {user_id} has been deleted!\n")
        
        else:
            print(f" User id: {user_id} is not in the database!\n")

    except Exception as e:
        print(f"{e}: Could not delete User id: {user_id}\n")

# Update a user
def update_user(connection, user_id:int, user_name:str):
    query = "UPDATE users SET name = ? WHERE id = ?" # order of codes:  1.(?) name   ->    2.(?) id 

    try:
        with connection:
            connection.execute(query, (user_name, user_id)) # <- the tuple has to match the order of the query's code: (1.(?) user_name, *THEN* 2.(?) user_id) , not (2.(?) user_id, 1.(?) user_name)
        print(f"User id {user_id} has changed his name to: {user_name} !\n")

    except Exception as e:
        print(f"{e}: Could not update User id: {user_id} 's name.\n")

# Add multiple users
def insert_users(connection, users:list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"

    try:
        with connection:
            connection.executemany(query, users)
        for user in users:
            print(user)
        print(f"{len(users)} new users has been added to the database table(users) !\n")
    
    except Exception as e:
        print(f"{e}: Could not add many new users.\n")

# A Main function
def main():

    # Establish connection, create my database
    connection = get_connection("first_database.db") # creates .db file even if it doesn't exist.

    try:
        # Create my table
        create_table(connection)

        while True:
            start = input("Enter an option (Add, Delete, Fetch, Update, Add Many, Exit): ").lower()

            if start == "add":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                email = input("Enter email: ")
                insert_user(connection, name, age, email)

            elif start == "fetch":
                print()
                rows = []
                for users in fetch_users(connection):
                    print(users)
                    rows.append(users)

                if len(rows) > 0:
                    print("Fetched all users successful!\n")
                else:
                    print("Table is empty.\n")
            
            elif start == "delete":
                user_id = int(input("Enter User id: "))
                delete_user(connection, user_id)

            elif start == "update":
                
                print()
                for user in fetch_users(connection):
                    print(user)
                print()

                user_id = int(input("Enter User id: "))
                user_name = input("Enter your new name: ")
                update_user(connection, user_id, user_name)

            elif start == "add many":
                users = []

                new_user = ([input("Enter name: "), int(input("Enter age: ")), input("Enter email: ")])
                users.append(new_user)
                print(f"New user added to list!\n")

                while True:
                    try:
                        more_users = input("Do you want to add users?: (Y/N): ").lower()
                        while not more_users == "y":

                            if more_users == "n":
                                break
                            else:
                                print("Please enter a valid option.")
                                more_users = input("Do you want to add users?: (Y/N): ").lower()
                                break
                        
                        if more_users == "n":
                            break
                    
                    except Exception as e:
                        print(f"{e}: how here?")

                    if more_users == "y":
                        new_user = ([input("Enter name: "), int(input("Enter age: ")), input("Enter email: ")])
                        users.append(new_user)
                        print(f"New user added to list!\n")
                    else:
                        print("Please enter a valid option.")

                insert_users(connection, users)

            elif start == "exit":
                break

            else:
                print("Please enter a valid option.\n")

    # 'finally' can be set without except, will always run.
    finally:
        print("Good bye <3\n")
        connection.close()

if __name__ == "__main__":
    main()