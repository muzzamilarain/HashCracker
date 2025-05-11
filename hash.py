import hashlib
import time
from pyfiglet import figlet_format
from termcolor import colored

print(colored(figlet_format("HASH CRACKER", font="slant"), "red"))
print(colored("Crack the Hash You want to Crack... ... ...", "yellow"))
print(colored(figlet_format("By Muzzamil Arain", font="digital"),"red"))
print(colored("LinkedIn: muzzamil-sadiq-7195b2258","yellow"))
print()

def detect_hash_type(hash_string):
    length = len(hash_string)
    if length == 32:
        return 'md5'
    elif length == 40:
        return 'sha1'
    elif length == 56:
        return 'sha224'
    elif length == 64:
        return 'sha256'
    elif length == 96:
        return 'sha384'
    elif length == 128:
        return 'sha512'
    else:
        return None


def crack_hash(given_hash, wordlist_file):
    print(colored("[*] Analyzing hash...", "cyan"))
    time.sleep(1)

    hash_type = detect_hash_type(given_hash)
    if hash_type is None:
        print(colored("[-] Unsupported or unknown hash type.", "red"))
        return

    print(colored(f"[+] Detected hash type: {hash_type.upper()}", "green"))
    print(colored("[*] Cracking in progress...\n", "cyan"))
    time.sleep(1)

    with open(wordlist_file, 'r', encoding='latin-1') as file:
        for word in file:
            word = word.strip()
            hash_func = getattr(hashlib, hash_type)
            hashed_word = hash_func(word.encode()).hexdigest()
            if hashed_word == given_hash:
                print(colored(f"[+] Password found: {word}", "green"))
                return

    print(colored("[-] Password not found in wordlist.", "red"))

hash_to_crack = input(colored("Enter the hash you want to crack: ", "blue")).strip()
wordlist_path = "/usr/share/wordlists/rockyou.txt"
crack_hash(hash_to_crack, wordlist_path)

