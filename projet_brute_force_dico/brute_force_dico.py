# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:58:34 2023

@author: Florian ANDRE
"""

import zipfile
import time
import itertools
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

def try_password(args):
    zip_file, word = args
    try:
        zip_file.extractall(pwd=word.strip())
        return word.decode().strip()
    except:
        return None

def dictionnaire(zip_file, wordlist):
    zip_file = zipfile.ZipFile(zip_file)
    n_words = len(list(open(wordlist, "rb")))
    print("nombre total de mots de passe nécessaires pour valider : ", n_words)
    
    with open(wordlist, "rb") as wordlist:
        with Pool(cpu_count()) as pool:
            results = list(tqdm(pool.imap(try_password, [(zip_file, word) for word in wordlist]), total=n_words, unit="word"))
            for result in results:
                if result:
                    print("[+] Password found:", result)
                    return
    print("[!] Mot de passe non trouve. Reessayez avec le brute force")

def brute_force(zip_file, charset="abcdefghijklmnopqrstuvwxyz", maxlength=8):
    zip_file = zipfile.ZipFile(zip_file)
    
    def generate_words():
        for length in range(1, maxlength + 1):
            for word in itertools.product(charset, repeat=length):
                yield "".join(word).encode()
    
    with Pool(cpu_count()) as pool:
        results = list(tqdm(pool.imap(try_password, [(zip_file, word) for word in generate_words()]), total=sum(len(charset)**i for i in range(1, maxlength + 1)), unit="word"))
        for result in results:
            if result:
                print("[+] Password found:", result)
                return
    print("[!] Mot de passe non trouve. Reessayez avec le dictionnaire")

def piratage_mdp_archive():
    your_archive = input("Entrez le chemin d'accès de votre archive ZIP : \n")
    wordlist = input("Entrez le chemin d'accès de votre fichier dictionnaire : \n")
    choix_attaque = input("\nchoisissez votre méthode d'attaque. 1 = dictionnaire, 2 = bruteforce : \n")
    if choix_attaque == "1":
        dictionnaire(your_archive, wordlist)
    else:
        brute_force(your_archive)

if __name__ == "__main__":
    piratage_mdp_archive()

