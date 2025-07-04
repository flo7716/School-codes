#include <stdio.h>
#include "board.h"
#include "move.h"

int main() {
    char board[8][8];
    initBoard(board);

    int turn = 0; // 0 = blanc, 1 = noir
    while (1) {
        printBoard(board);
        printf("%s joue (ex: e2 e4) : ", turn == 0 ? "Blanc" : "Noir");

        char src[3], dst[3];
        scanf("%s %s", src, dst);

        int srcRow = 8 - (src[1] - '0');
        int srcCol = src[0] - 'a';
        int dstRow = 8 - (dst[1] - '0');
        int dstCol = dst[0] - 'a';

        if (isValidMove(board, srcRow, srcCol, dstRow, dstCol, turn)) {
            movePiece(board, srcRow, srcCol, dstRow, dstCol);
            turn = 1 - turn;
        } else {
            printf("Coup invalide. Réessaie.\n");
        }
    }

    return 0;
}
