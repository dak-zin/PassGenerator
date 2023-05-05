import random
import string
import argparse
import colorama
from datetime import datetime

colorama.init()

def generate_password(length, uppercase, lowercase, numbers, symbols):
    chars = []
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_password_strength(password):
    length = len(password)
    uppercase = sum(1 for c in password if c.isupper())
    lowercase = sum(1 for c in password if c.islower())
    numbers = sum(1 for c in password if c.isdigit())
    symbols = sum(1 for c in password if c in string.punctuation)

    score = length * 4
    if uppercase > 0:
        score += (length - uppercase) * 2
    if lowercase > 0:
        score += (length - lowercase) * 2
    if numbers > 0:
        score += numbers * 4
    if symbols > 0:
        score += symbols * 6

    if score >= 80:
        strength = 'strong'
        color = colorama.Fore.GREEN
    elif score >= 60:
        strength = 'medium'
        color = colorama.Fore.YELLOW
    else:
        strength = 'weak'
        color = colorama.Fore.RED

    return (strength, score, color)

def generate_passwords(length, count, uppercase, lowercase, numbers, symbols):
    passwords = []
    for i in range(count):
        password = generate_password(length, uppercase, lowercase, numbers, symbols)
        passwords.append(password)

    return passwords

def save_passwords(passwords, filename):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

def read_wordlist(filename):
    """Read a wordlist file into a list of words."""
    with open(filename, 'r') as file:
        words = [line.strip() for line in file]

    return words

def generate_password_from_wordlist(wordlist, length):
    password = random.choice(wordlist) + str(random.randint(0, 999))
    if len(password) < length:
        password += generate_password(length - len(password), True, True, True, False)
    return password



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Password Generator')
    parser.add_argument('-n', '--num-passwords', type=int, default=1, help='Number of passwords to generate (default: 1)')
    parser.add_argument('-l', '--length', type=int, default=8, help='Length of the password (default: 8)')
    parser.add_argument('-s', '--save', action='store_true', help='Save the generated passwords to a file')
    parser.add_argument('-w', '--wordlist', help='Wordlist file to generate passwords based on words')
    parser.add_argument('-v', '--verify', action='store_true', help='Verify the strength of the generated passwords')

    args = parser.parse_args()

    passwords = []
    for i in range(args.num_passwords):
        if args.wordlist:
            password = generate_password_from_wordlist(read_wordlist(args.wordlist))
        else:
            password = generate_password(args.length, uppercase=True, lowercase=True, numbers=True, symbols=True)

        # Verify the strength of the password
        if args.verify:
            strength, score, color = check_password_strength(password)
            print(f'{color}{password}{colorama.Style.RESET_ALL} ({strength} - {score} points)')
        else:
            print(f'{password}')

        passwords.append(password)

    if args.save:
        filename = f'passwords_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt'
        save_passwords(passwords, filename)
        print(f'Passwords saved to "{filename}"')

