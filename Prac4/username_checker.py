
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSut', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username_input = input("Please enter your username")

if username_input in usernames:
    print("Access Granted")
else:
    print("Access Denied")