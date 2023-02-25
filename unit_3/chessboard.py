# 8 x 8

WHITE_POWN = "WP"
BLACK_POWN = "BP"


chess_row = ["--" for i in range(8)]
chessboard = [chess_row[:] for i in range(8)]

chessboard[0][0] = WHITE_POWN
chessboard[3][5] = BLACK_POWN

for chess_r in chessboard:
    for chess_square in chess_r:
        print(chess_square, end=" ")
    print()
