import mysql.connector
import time

def connect_db():
    return mysql.connector.connect(host="localhost",user="root",password="1234",database="rishit")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Players (Name varchar(100) PRIMARY KEY, Age INT NOT NULL, Nationality varchar(100) NOT NULL, Team varchar(100) NOT NULL, TG int NOT NULL, ETV INT NOT NULL)''')
    conn.close()

def set_data():
    print("ENTER Football Player'S DETAILS")
    name = input('Enter player name: ')
    age = int(input('Enter age of player:'))
    nationality = input('Enter nationality of player:')
    team = input('Enter name of club:') 
    total_goals = int(input('Enter total goals scored by player:'))
    etv = int(input('Enter evaluated transfer value of player:'))
    print()
    return (name, age, nationality, team, total_goals, etv)

def display_data(player):
    print("\nPLAYER'S DETAILS..")
    print('Name:', player[0], '\nAge:', player[1], '\nNationality:', player[2], '\nTeam:', player[3], '\nTotal Goals:', player[4], '\nETV:', player[5])

def display_data_tabular(player):        
    print(player[0],'\t', player[1],'\t', player[2],'\t', player[3],'\t', player[4],'\t\t', player[5])
def players_result():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Players')
    rows = cursor.fetchall()
    print("Name\t \tAge\t Nationality\t Team\t \tTotal Goals\t ETV")
    for row in rows:
        display_data_tabular(row)
    conn.close()

def write_record():
    conn = connect_db()
    cursor = conn.cursor()
    while True:
        player = set_data()
        cursor.execute('INSERT INTO players (name, age, nationality, team, tg, etv) VALUES (%s, %s, %s, %s, %s,%s)', player)
        conn.commit()
        ans = input('Wants to enter more record (y/n)?: ')
        if ans in 'nN':
            break
    conn.close()

def read_records():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM players')
    rows = cursor.fetchall()
    for row in rows:
        display_data(row)
    conn.close()

def search_record():
    conn = connect_db()
    cursor = conn.cursor()
    name = input('Enter the player you want to search: ')
    cursor.execute('SELECT * FROM players WHERE name = %s', (name,))
    row = cursor.fetchone()
    if row:
        display_data(row)
    else:
        print('Record not found')
    conn.close()

def delete_record():
    conn = connect_db()
    cursor = conn.cursor()
    name = input('Enter player name: ')
    cursor.execute('DELETE FROM players WHERE name = %s', (name,))
    conn.commit()
    if cursor.rowcount:
        print('Record deleted')
    else:
        print('Record not found')
    conn.close()
    
def modify_record():
    conn = connect_db()
    cursor = conn.cursor()
    name = input('Enter player name: ')
    cursor.execute('SELECT * FROM players WHERE name = %s', (name,))
    row = cursor.fetchone()
    if row:
        print('Current record:')
        display_data(row)
        print('Modify fields (leave empty to keep current value):')
        name = input('Enter player name: ')
        age = int(input('Enter age of player:'))
        nationality = input('Enter nationality of player:')
        team = input('Enter name of club:') 
        total_goals = int(input('Enter total goals scored by player:'))
        etv = int(input('Enter evaluated transfer value of player:'))
        cursor.execute('''UPDATE players SET name = %s, age = %s, nationality = %s, team = %s, tg = %s, etv = %s WHERE name = %s''', (name, age, nationality, team, total_goals, etv, name))
        conn.commit()
        print('Record updated')
        display_data((name, age, nationality, team, total_goals, etv))
    else:
        print('Record not found')
    conn.close()

def intro():
    print("="*70)
    print("{: ^60s}".format("Football Player Database"))
    print("{: ^60s}".format("Final 12th Grade C.S. PROJECT"))
    print("{: ^60s}".format("MADE BY: Rishit Garg"))
    print("="*70)
    print()

def main_menu():
    print("MAIN MENU\n1. PLAYER MENU\n2. ADMIN MENU\n3. EXIT")

def player_menu():
    print("PLAYER MENU\n1. All Players Information\n2. Search for a Player's Information\n3. BACK TO MAIN MENU")

def admin_menu():
    print("""\nADMIN MENU\n1. CREATE PLAYER RECORD
2. DISPLAY ALL PLAYERS RECORDS
3. SEARCH PLAYER RECORD
4. MODIFY PLAYER RECORD
5. DELETE PLAYER RECORD
6. BACK TO MAIN MENU""")

def main():
    intro()
    create_table()
    while True:
        main_menu()
        choice = input('Enter choice(1-3): ')
        print()
        if choice == '1':
        
            while True:
                player_menu()
                rchoice = input('Enter choice(1-3): ')
                print()
                if rchoice == '1':
                    players_result()
                elif rchoice == '2':
                    search_record()
                elif rchoice == '3':
                    break
                else:
                    print('Invalid input\n')
                print()
        elif choice == '2':
            while True:
                admin_menu()
                echoice = input('Enter choice(1-6): ')
                print()
                if echoice == '1':
                    write_record()
                elif echoice == '2':
                    read_records()
                elif echoice == '3':
                    search_record()
                elif echoice == '4':
                    modify_record()
                elif echoice == '5':
                    delete_record()
                elif echoice == '6':
                    break
                else:
                    print('Invalid input\n')
        elif choice == '3':
            print('Thanks for using Football Player Management System')
            break
        else:
            print('Invalid input')
    print()
main()
