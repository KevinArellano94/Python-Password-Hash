import hashlib
import getpass
import pyperclip

def main():
    string = getpass.getpass('> ')
    hash = hashlib.sha256(string.encode()).hexdigest()
    hash = hashlib.sha512(hash.encode()).hexdigest()
    pyperclip.copy(hash)
    print('Done.')

if __name__ == "__main__":
    main()