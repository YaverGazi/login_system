import sqlite3
conn =sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
 CREATE TABLE IF NOT EXISTS users (
          id  INTEGER PRIMARY KEY, 
          username TEXT UNIQUE,
          password TEXT
 )
 ''')

conn.commit()
conn.close()

print('Datebase and users table are ready!')




def register():
    username = input('username')
    password = input('password')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,password))
        conn.commit()
        print('Registration successful')
    except sqlite3.IntegrityError:   
        print('but this username is already exits') 

    conn.close()    
        

def login():
    username = input('username: ')
    password = input('password: ')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM  users  WHERE  username = ? AND  password = ?', (username,password))
    user = cursor.fetchone()

    if user:
        print(f'Wellcome {username}')

    else:
        print('password or usrname is wrong')

    conn.close()        



while True:
    choice = input('1- Register\n2- Login\n3- Exit\nSeçim: ')

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        break
    else:
        print('Invalid selection')