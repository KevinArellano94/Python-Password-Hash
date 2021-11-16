# Python - Password Hash

Simple script that hashes your string in terminal two-fold and saves it in your clipboard.

## Getting Started

These instructions will guide you in creating the project, getting it up and running on your local machine'a virtual environment for development and testing purposes.

Folder structure:
    ```PowerShell
    ~python\{ Project Name }
    ```

Future updates:

-See deployment for notes on deploying the project on a live system.

### Prerequisites

An installation of Python ( version 3.10.0 ) and PIP ( version 21.2.3 )

### Installing

Assuming you are inside the project folder, which we will call "\Password Hash", open the Windows Terminal Preview ( or Powershell ).

Create venv and activate it
```python
py -m venv venv
.\venv\Scripts\Activate.ps1
```
Install dependencies

    pip install hashlib; pip install getpass; pip install pyperclip;

Create file in "python\Password Hash" called "main.py" and add following code

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

Test script in terminal

    py .\main.py

Type "Test" after the ">" and paste to get the result

    > 
    Done.

After the script is finished you should have in your clipboard the following string

    5842211db0f242d61a5ed09ffb9ffce51e15bc4eed62a0a5d85c3cb11ef01343a6433fb3a8a649d57e488df0c087db2079a0ddb031346162661a0427d37a1b38

## Running the tests

Simply run the "main.py" file in terminal

## Deployment

*Future update*

## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
  - [Creative Commons](https://creativecommons.org/) - Used to choose
    the license

## Contributing

Feel free to contribute

## Versioning

For the versions available, see the [tags on thisrepository](https://github.com/KevinArellano94/a-good-readme-template/tags).

## Authors

  - **Kevin Arellano** - *Created project* - [KevinArellano94](https://github.com/KevinArellano94)

See also the list of
[contributors](https://github.com/KevinArellano94/Python-Password-Hash/graphs/contributors)
who participated in this project.

## License

This project is licensed under the [MIT License](LICENSE.md)

## Acknowledgments

  - Thank you for reading this far