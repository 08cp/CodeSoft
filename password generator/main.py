import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase + uppercase + digits + special_characters

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("How long do you want your password to be? (Minimum 4 characters): "))
            if length < 4:
                print("Please choose a length of at least 4 characters for security reasons.")
            else:
                break
        except ValueError:
            print("Oops! That doesn't seem to be a valid number. Please try again.")

    password = generate_password(length)

    print("Here is your generated password:", password)

if __name__ == "__main__":
    main()