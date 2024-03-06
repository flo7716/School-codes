# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:58:34 2023

@author: Florian ANDRE
"""

import zipfile,time


import itertools
tc=time.time()

import zipfile
from tqdm import tqdm

def dictionnaire(zip_file, wordlist="G:\Mon Drive\IPSA\Aéro 1\semestre 2 2022-2023\grand projet\\fr_utf8.dic"):
    zip_file = zipfile.ZipFile(zip_file)
    n_words = len(list(open(wordlist, "rb")))
    print("nombre total de mots de passe nécessaires pour valider : ", n_words)
    
    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=n_words, unit="word"):
            try:
                zip_file.extractall(pwd=word.strip())
            except Exception as e:
                continue
            else:
                print("[+] Password found:", word.decode().strip())
                return
    print("[!] Mot de passe non trouve. Reessayez avec le brute force")

def brute_force(zip_file, charset="abcdefghijklmnopqrstuvwxyz", maxlength=8):
    zip_file = zipfile.ZipFile(zip_file)
    
    for length in range(1, maxlength + 1):
        for word in itertools.product(charset, repeat=length):
            attempt = "".join(word).encode()
            print("[*] Trying password:", attempt.decode())  # Affiche la tentative de mot de passe
            try:
                zip_file.extractall(pwd=attempt)
            except Exception as e:
                continue
            else:
                print("[+] Password found:", attempt.decode())
                return
    print("[!] Mot de passe non trouve. Reessayez avec le dictionnaire")




def piratage_mdp_archive():
    your_archive = input("Entrez le chemin d'accès de votre archive ZIP : \n")
    # Fonction pour pirater le mot de passe d'une archive ZIP. Tente d'abord une attaque par dico. Si celle ci ne marche pas, essaie avec le brute force.
    choix_attaque=input("\nchoisissez votre méthode d'attaque. 1 = dictionnaire, 2 = bruteforce : \n")
    if choix_attaque=="1":
        dictionnaire(your_archive)
    else:
        brute_force(your_archive)

piratage_mdp_archive()

