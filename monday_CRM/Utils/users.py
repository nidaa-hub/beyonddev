valid_users = [
    {"name": "", "email": "gethelpproject2021@gmail.com", "password": "gethelp24"}]


def get_valid_user(name):
    try:
        return next(user for user in valid_users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)


def get_all_valid_users():
    return valid_users
