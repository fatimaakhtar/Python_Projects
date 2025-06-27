import random
import string


password_length = 12
charValue=string.ascii_letters + string.punctuation + string.digits

password = ""
for i in range(password_length):
    password += random.choice(charValue)

print("Your password is:", password)
""" WE CAN ALSO USE THIS METHOD TO GENERATE A PASSWORD """

"""value = "".join(random.choice(charValue) for i in range(password_length))
print("Your password is:", value)"""