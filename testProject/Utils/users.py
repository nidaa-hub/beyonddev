valid_users = [
    {"name": "mohammadkhayyo12account", "email": "mohammadkhayyo12@gmail.com", "password": "+j.q2B,TrA8+#pj"}]


def get_valid_user(name):
    try:
        return next(user for user in valid_users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)


def get_all_valid_users():
    return valid_users
