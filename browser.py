import requests
import os
import sys
from bs4 import BeautifulSoup
import requests
import os
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

args = sys.argv
d = args[1]
if not os.path.exists(os.getcwd() + "/" + d):
    os.mkdir(os.getcwd() + "/" + d)


stack = []
s = ""
while True:
    s = input()

    if s == "exit":
        break

    elif s == "back":
        if len(stack) == 0 or len(stack) == 1:
            continue
        else:
            stack.pop()
            with open(os.getcwd() + "/" + d + "/" + stack[-1] + ".txt", 'r') as f:
                print(f.read())

    elif os.path.exists(os.getcwd() + "/" + d + "/" + s + ".txt"):
        with open(os.getcwd() + "/" + d + "/" + s + ".txt", 'r') as f:
            print(f.read())

    elif s.startswith("https://") and s.rfind(".") != -1:
        r = requests.get(s)
        soup = BeautifulSoup(r.content, 'html.parser')
        text = ''
        tags = ['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'span']
        for t in soup.recursiveChildGenerator():
            if t.name in tags:
                if t.name == 'a':
                    text += Fore.BLUE + t.text + Style.RESET_ALL
                else:
                    text += t.text
        print(text)
        with open(os.getcwd() + "/" + d + "/" + s[s.find("/") + 2:s.rfind(".")] + ".txt", 'w') as f:
            f.write(text)
        stack.append(s[s.find("/") + 2:s.rfind(".")])


    elif not s.startswith("https://") and s.rfind(".") != -1:
        r = requests.get("https://" + s)
        soup = BeautifulSoup(r.content, 'html.parser')
        text = ''
        tags = ['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'span']
        for t in soup.recursiveChildGenerator():
            if t.name in tags:
                if t.name == 'a':
                    text += Fore.BLUE + t.text + Style.RESET_ALL
                else:
                    text += t.text
        print(text)
        with open(os.getcwd() + "/" + d + "/" + s[:s.rfind(".")] + ".txt", 'w') as f:
            f.write(text)
        stack.append(s[s.find("/") + 2:s.rfind(".")])

    else:
        print("Error: incorrect URL")
