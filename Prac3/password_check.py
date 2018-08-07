
def main():
    # statements...
    password = get_password()
    do_stuff(password)


def get_password():
    password = str(input("Password?"))
    return password


def do_stuff(password):
    for i in range(0, len(password)):
        print("*", end="")

