from pathlib import Path
import sys

from PyQt5 import QtWidgets, uic


BASE_DIR = Path(__file__).resolve().parent
UI_DIR = BASE_DIR / "data"


def load_ui(filename):
    return uic.loadUi(str(UI_DIR / filename))


# fenêtres

def win0():
    print("Menu initial")
    win.show()


def win1():
    print("NFT_1 - Disque de Feu")
    win_1.show()


def win2():
    print("NFT_2 - Rimmel près")
    win_2.show()


def win3():
    print("NFT_3 - Fou du rire")
    win_3.show()


def win4():
    print("NFT_4 - Tennis de table")
    win_4.show()


def win5():
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


# chargement des fenêtres

app = QtWidgets.QApplication(sys.argv)

win = load_ui("ecran_principal.ui")
win_1 = load_ui("NFT_1.ui")
win_2 = load_ui("NFT_2.ui")
win_3 = load_ui("NFT_3.ui")
win_4 = load_ui("NFT_4.ui")
win_5 = load_ui("NFT_5.ui")
win_6 = load_ui("NFT_6.ui")
win_7 = load_ui("NFT_7.ui")
win_8 = load_ui("NFT_8.ui")
win_9 = load_ui("NFT_9.ui")
win_10 = load_ui("NFT_10.ui")
win_11 = load_ui("NFT_11.ui")
win_12 = load_ui("NFT_12.ui")
win_13 = load_ui("ecran_achat_finalise.ui")


# boutons du menu principal

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


# écrans d'achat

nft_windows = [
    win_1,
    win_2,
    win_3,
    win_4,
    win_5,
    win_6,
    win_7,
    win_8,
    win_9,
    win_10,
    win_11,
    win_12,
]

for nft_window in nft_windows:
    nft_window.pushButton.clicked.connect(win13)
    nft_window.pushButton.clicked.connect(nft_window.close)
    nft_window.pushButton_2.clicked.connect(nft_window.close)

win_13.pushButton.clicked.connect(win_13.close)


win.show()
sys.exit(app.exec())