import time

username = 'xargon'
password = 'secret'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Access granted.')
    print('Please wait...')
    time.sleep(5)
    print('Ok... Loading')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('Security clearence acknowledged.')
    print(f'Welcome {username} to the administrator mainframe.')
elif username_input == username and password_input != password:
    print('Password incorrect')
elif username_input != username and password_input == password:
    print('Username incorrect')
else:
    print('Username and password are incorrect')