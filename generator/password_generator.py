import random
import string


def random_password():
    """Generate a random password """
    random_source = string.ascii_letters + string.digits + string.punctuation + string.whitespace + string.hexdigits
    password = random.choice(string.ascii_lowercase + string.ascii_letters + string.ascii_uppercase
                             + string.punctuation + string.whitespace + string.punctuation)
    password += random.choice(string.digits + string.ascii_letters + string.punctuation +
                              string.whitespace + string.whitespace + string.whitespace)
    password += random.choice(string.punctuation + string.hexdigits + string.whitespace)
    password += random.choice(string.hexdigits + string.whitespace)

    for i in range(25):
        password += random.choice(random_source)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


print("First Random Password is ", random_password())
print("Second Random Password is ", random_password())
print("Third Random Password is ", random_password())
