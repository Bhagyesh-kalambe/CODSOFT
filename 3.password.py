import random

def gen_pass(length):
    password = ''
    for i in range(length):
        random_ascii = random.randint(33, 126)
        password += chr(random_ascii)
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    password = gen_pass(length)
    print(f"Generated Password : {password}")

main()
