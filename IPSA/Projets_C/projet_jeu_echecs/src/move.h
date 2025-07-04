#ifndef MOVE_H
#define MOVE_H

int isValidMove(char board[8][8], int srcRow, int srcCol, int dstRow, int dstCol, int turn);
void movePiece(char board[8][8], int srcRow, int srcCol, int dstRow, int dstCol);

#endif
