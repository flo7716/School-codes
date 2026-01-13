#Hector LAMALLE et Florian ANDRE
#2B DIA
#TP2 BIn223

import os, threading


def generate_file_from_filename(filename):
        with open(filename,'w') as f:
                f.write('1')


def multi_thread_generate_files(filenames):
        L=[]
        for n in filenames:
                thread = threading.Thread(target=generate_file_from_filename, args=(n,))
                thread.start()
                L.append(thread)

        for i in L:
                i.join()



files = ['g1.txt', 'g2.txt', 'g3.txt', 'g4.txt', 'g5.txt', 'g6.txt']
multi_thread_generate_files(files)
