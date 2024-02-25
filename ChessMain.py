

import pygame as py
import ChessEngine

WIDTH=HEIGHT=532
DIMENSION=8
SQ_SIZE=HEIGHT//DIMENSION
MAX_FPS=15
IMAGES={}

def loadImages():
    pieces=["wp","wR","wN","wB","wQ","wK","bR","bN","bB","bQ","bK","bp"]
    for piece in pieces:
        IMAGES[piece]=py.transform.scale(py.image.load("Images/"+piece+".png"),(SQ_SIZE,SQ_SIZE))


def main():
    py.init()
    screen=py.display.set_mode((WIDTH,HEIGHT))
    clock=py.time.Clock()
    screen.fill(py.Color("white"))
    gs=ChessEngine.GameState()
    loadImages()
    running=True
    while(True):
        for e in py.event.get():
            if e.type==py.QUIT:
                running=False
                py.quit()
        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        py.display.flip()


def drawGameState(screen,gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)


def drawBoard(screen):
    colors=[py.Color("white"),py.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color=colors[(r+c)%2==0]
            py.draw.rect(screen,color,py.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece=board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],py.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

if __name__=="__main__":
    main()