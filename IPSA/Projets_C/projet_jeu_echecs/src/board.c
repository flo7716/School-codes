#include <stdio.h>
#include "board.h"

void initBoard(char board[8][8]) {
    // Pièces noires
    char black[8] = {'t', 'c', 'f', 'd', 'r', 'f', 'c', 't'};
    for (int i = 0; i < 8; i++) {
        board[0][i] = black[i];
        board[1][i] = 'p';
    }

    // Cases vides
    for (int i = 2; i < 6; i++)
        for (int j = 0; j < 8; j++)
            board[i][j] = ' ';

    // Pièces blanches
    char white[8] = {'T', 'C', 'F', 'D', 'R', 'F', 'C', 'T'};
    for (int i = 0; i < 8; i++) {
        board[6][i] = 'P';
        board[7][i] = white[i];
    }
}

void printBoard(char board[8][8]) {
    printf("  a b c d e f g h\n");
    for (int i = 0; i < 8; i++) {
        printf("%d ", 8 - i);
        for (int j = 0; j < 8; j++) {
            printf("%c ", board[i][j]);
        }
        printf("\n");
    }
}
