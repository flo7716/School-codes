#Hector LAMALLE et Florian ANDRE
#2B DIA
#TP2 BIn223

import os


def generate_file_from_filename(filename):
        with open(filename,'w') as f:
                f.write('1')


def multi_process_generate_files(filenames):
        for n in filenames:
                pid=os.fork()
                if pid == 0:
                        generate_file_from_filename(n)
                        os._exit(0) #genere un processus
                elif pid < 0:
                        print("erreur") #erreur systeme
                else :
                        pass #passe



files = ['g1.txt', 'g2.txt', 'g3.txt', 'g4.txt', 'g5.txt', 'g6.txt']
multi_process_generate_files(files)
