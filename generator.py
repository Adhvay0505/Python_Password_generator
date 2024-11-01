import random
import string

def generate_passwords(length: int):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

length = int(input("Enter the desired length of your password: "))
num_passwd = int(input("How many passwords do you want to generate? "))

if length <=0 or num_passwd <=0:
    print("You didnt mention a valid length or a valid number of passwords")

else:
    passwords = [generate_passwords(length) for _ in range(num_passwd)]
    print("Generated passwords: ")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")
    