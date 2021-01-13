class Content:

    def __init__(self):
        self.score = 0
        self.best = 0

    def update_best(self, data):
        self.best += data
        # update db

    def update_score(self, data):
        self.score += data
        if self.score > self.best:
            self.update_best(
                self.score
            )

    def run(self):
        global font_size
        font_size = {'BIG': pygame.font.Font(None, 72),
                     'MEDIUM': pygame.font.Font(None, 36),
                     'SMALL': pygame.font.Font(None, 18)}
        pygame.draw.rect(
            screen, COLOR['GRID_SEC'], (0, 0, 480, 100))
        score_board = pygame.draw.rect(
            screen, COLOR['TXT_SEC'], (350, 0, 260, 100))

        length = score_board.right - score_board.left
        screen.blit(font_size['MEDIUM'].render(
            "Score:", True, COLOR['GRID_PRI']), (score_board.left + 5, 15))
        screen.blit(font_size['BIG'].render(
            str(self.score), True, COLOR['GRID_PRI']), (score_board.left + 20, 50))

        screen.blit(font_size['BIG'].render(
            "2048", True, COLOR['TXT_SEC']), (25, 25))

