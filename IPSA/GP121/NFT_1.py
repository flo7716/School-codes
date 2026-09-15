

import random
from PyQt5 import uic, QtWidgets

#fenêtres

def win0 ():
    print("Menu initial")
    win.show()

def win1 ():
    print("NFT_1 - Disque de Feu")
    win_1.show()
    win_1.pushButton.clicked.connect(achat_NFT)
    win_1.pushButton_2.clicked.connect(win0)

def win2 ():
    print("NFT_2 - Rimmel près")
    win_2.show()

def win3 ():
    print("NFT_3 - Fou du rire")
    win_3.show()

def win4 ():
    print("NFT_4 - Tennis de table")
    win_4.show()

def win5 ():
    print("NFT_5 - Vie dépravée")
    win_5.show()

def win6():
    print("NFT_6 - Greenpace")
    win_6.show()

def win7():
    print("NFT_7 - Coup de choc")
    win_7.show()

def win8():
    print("NFT_8 - Abeille Furtive")
    win_8.show()

def win9():
    print("NFT_9 - Grippe et colère")
    win_9.show()

def win10():
    print("NFT_10 - Loup garou")
    win_10.show()

def win11():
    print("NFT_11 - C´est finit")
    win_11.show()

def win12():
    print("NFT_12 - Bizarre")
    win_12.show()
    
def win13():
    print("Achat NFT terminé")
    win_13.show()

def achat_NFT():
    print ("Achat NFT")


#boutons

app = QtWidgets.QApplication([])                
win = uic.loadUi("data/ecran_principal.ui")       
win.pushButton.clicked.connect(win1)
win.pushButton_2.clicked.connect(win2)
win.pushButton_3.clicked.connect(win3)
win.pushButton_4.clicked.connect(win4)
win.pushButton_6.clicked.connect(win5)
win.pushButton_5.clicked.connect(win6)
win.pushButton_8.clicked.connect(win7)
win.pushButton_7.clicked.connect(win8)
win.pushButton_10.clicked.connect(win9)
win.pushButton_9.clicked.connect(win10)
win.pushButton_12.clicked.connect(win11)
win.pushButton_11.clicked.connect(win12)

#chargement des fenêtres

win_1 = uic.loadUi("data/NFT_1.ui")
win_2 = uic.loadUi("data/NFT_2.ui")
win_3 = uic.loadUi("data/NFT_3.ui")
win_4 = uic.loadUi("data/NFT_4.ui")
win_5 = uic.loadUi("data/NFT_5.ui")
win_6 = uic.loadUi("data/NFT_6.ui")
win_7 = uic.loadUi("data/NFT_7.ui")
win_8 = uic.loadUi("data/NFT_8.ui")
win_9 = uic.loadUi("data/NFT_9.ui")
win_10 = uic.loadUi("data/NFT_10.ui")
win_11 = uic.loadUi("data/NFT_11.ui")
win_12 = uic.loadUi("data/NFT_12.ui")
win_13 = uic.loadUi("data/ecran_achat_finalise.ui")

#Ecran d'achat

win_1.pushButton.clicked.connect(win13)             #achat validé
win_1.pushButton.clicked.connect(win_1.close)       #achat validé
win_1.pushButton_2.clicked.connect(win_1.close)     #retour

win_2.pushButton.clicked.connect(win13)             #achat validé
win_2.pushButton.clicked.connect(win_2.close)
win_2.pushButton_2.clicked.connect(win_2.close)     #retour

win_3.pushButton.clicked.connect(win13)
win_3.pushButton.clicked.connect(win_3.close)
win_3.pushButton_2.clicked.connect(win_3.close)

win_4.pushButton.clicked.connect(win13)
win_4.pushButton.clicked.connect(win_4.close)
win_4.pushButton_2.clicked.connect(win_4.close)

win_5.pushButton.clicked.connect(win13)
win_5.pushButton.clicked.connect(win_5.close)
win_5.pushButton_2.clicked.connect(win_5.close)

win_6.pushButton.clicked.connect(win13)
win_6.pushButton.clicked.connect(win_6.close)
win_6.pushButton_2.clicked.connect(win_6.close)

win_7.pushButton.clicked.connect(win13)
win_7.pushButton.clicked.connect(win_7.close)
win_7.pushButton_2.clicked.connect(win_7.close)

win_8.pushButton.clicked.connect(win13)
win_8.pushButton.clicked.connect(win_8.close)
win_8.pushButton_2.clicked.connect(win_8.close)

win_9.pushButton.clicked.connect(win13)
win_9.pushButton.clicked.connect(win_9.close)
win_9.pushButton_2.clicked.connect(win_9.close)

win_10.pushButton.clicked.connect(win13)
win_10.pushButton.clicked.connect(win_10.close)
win_10.pushButton_2.clicked.connect(win_10.close)

win_11.pushButton.clicked.connect(win13)
win_11.pushButton.clicked.connect(win_11.close)
win_11.pushButton_2.clicked.connect(win_11.close)

win_12.pushButton.clicked.connect(win13)
win_12.pushButton.clicked.connect(win_12.close)
win_12.pushButton_2.clicked.connect(win_12.close)

win_13.pushButton.clicked.connect(win_13.close)

win.show()
app.exec()