import pygame
import chess

class GameUI:
    def __init__(self, board):
        pygame.init()
        self.board = board
        self.size = 480
        self.square_size = self.size // 8
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("AI Chess")

    def draw_board(self):
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(col*self.square_size, row*self.square_size,
                                             self.square_size, self.square_size))
        pygame.display.flip()
