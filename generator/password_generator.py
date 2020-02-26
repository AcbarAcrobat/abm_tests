import random
import string


def randomPassword():
    """Generate a random password """
    randomSource = string.ascii_letters + string.digits + string.punctuation + string.whitespace + string.hexdigits
    password = random.choice(string.ascii_lowercase + string.ascii_letters + string.ascii_uppercase + string.punctuation + string.whitespace + string.punctuation)
    # password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits + string.ascii_letters + string.punctuation + string.whitespace + string.whitespace + string.whitespace)
    password += random.choice(string.punctuation + string.hexdigits + string.whitespace)
    password += random.choice(string.hexdigits + string.whitespace)

    for i in range(25):
        password += random.choice(randomSource)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password


print("First Random Password is ", randomPassword())
print("Second Random Password is ", randomPassword())
print("Third Random Password is ", randomPassword())
