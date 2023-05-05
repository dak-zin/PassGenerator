# Password Generator

🔒 A simple command-line tool for generating secure passwords.

## Dependencies

This tool requires the following Python libraries to be installed:

- `random`: for generating random characters
- `string`: for working with strings and character sets
- `argparse`: for parsing command-line arguments
- `colorama`: for adding color to console output

You can install these dependencies by running the following command:


pip install random string argparse colorama

## Usage

To generate a random password, simply run the `password.py` script with the desired options. Here are the available options:

- `-n/--num-passwords`: number of passwords to generate (default: 1)
- `-c/--length`: length of the password (default: 8)
- `-s/--save`: save the passwords to a file
- `-w/--wordlist`: use a wordlist file to generate passwords based on words
- `-v/--verify`: check the strength of the generated passwords

For example, to generate three passwords with a length of 12 characters and save them to a file, run the following command:


python password.py -n 3 -c 12 -s

If you want to generate passwords based on words from a wordlist, specify the path to the wordlist file with the `-w` option. Here's an example command:

python password.py -n 3 -w wordlist.txt

By default, the script will output the generated passwords to the console. If you want to check the strength of the passwords, use the `-v` option. Here's an example command:

python password.py -n 1 -c 16 -v

You can free-use and edit this code!
