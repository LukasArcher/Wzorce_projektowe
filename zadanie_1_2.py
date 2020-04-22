class WrongPassword(Exception):
    pass

def get_name(decorated_func):
    def wrapper(*args, **kwargs):
        decorated_func(input("What's your name? "))
    return wrapper


def password_required(decorated_function):

    def wrapper(*args, **kwargs):
        wrong_password_counter = 0
        PASSWORD = '1234'
        user_password = input("Password please: ")
        while wrong_password_counter != 2 and user_password != PASSWORD:
            wrong_password_counter += 1
            print("Wrong password!")
            user_password = input("Password please: ")
        if wrong_password_counter == 2:
            print("Account blocked!")
        else:
            decorated_function(*args, **kwargs)
    return wrapper



@get_name
def main(name: str) -> None:
    print(f"Hello, {name}")


if __name__ == '__main__':
    main('Hmmm?')