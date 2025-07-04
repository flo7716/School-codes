#include "move.h"

void movePiece(char board[8][8], int srcRow, int srcCol, int dstRow, int dstCol) {
    board[dstRow][dstCol] = board[srcRow][srcCol];
    board[srcRow][srcCol] = ' ';
}

// Version simplifiée : permet tout déplacement d'une pièce du bon camp
int isValidMove(char board[8][8], int srcRow, int srcCol, int dstRow, int dstCol, int turn) {
    char piece = board[srcRow][srcCol];
    if (piece == ' ') return 0;

    // Vérifie la couleur de la pièce
    if (turn == 0 && piece >= 'a' && piece <= 'z') return 0; // blanc joue mais pièce noire
    if (turn == 1 && piece >= 'A' && piece <= 'Z') return 0; // noir joue mais pièce blanche

    // Pour l'instant, autorise tout déplacement non vide (à améliorer)
    return 1;
}
