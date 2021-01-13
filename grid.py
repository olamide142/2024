class Grid:
    
    def __init__(self):
        pass

    def run(self):

        pygame.draw.rect(screen, COLOR['TXT_SEC'], (55, 130, 310, 300), 4)
        for x in range(1, 5):
            for y in range(2, 6):
                rect = pygame.Rect(x * Box.size, y * Box.size,
                                   Box.size, Box.size)
                pygame.draw.rect(screen, COLOR['TXT_SEC'], rect, 1)

