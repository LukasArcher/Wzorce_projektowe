class WrongPassword(Exception):
    pass

def get_name(_):
    def wrapper(*args, **kwargs):
        name = input("What's your name? ")
        print(f"Hello, {name}")
        # decorated_func(*args, **kwargs)
    return wrapper


def password_required(decorated_function):

    def wrapper(*args, **kwargs):
        wrong_password_counter = 0
        PASSWORD = '1234'
        user_password = input("Password please: ")
        try:
            if PASSWORD == user_password:
                decorated_function(*args, **kwargs)
            else:
                raise WrongPassword
        except WrongPassword:
            wrong_password_counter += 1
            if wrong_password_counter == 3:
                print("Account blocked!")
                return
            print("Wrong password!")
            wrapper(*args, **kwargs)
    return wrapper



@password_required
def main(name: str) -> None:
    print(f"Hello, {name}")


if __name__ == '__main__':
    main('Hmmm?')