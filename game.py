class Game:
    __size_x = 500
    __size_y = 500
    clock = pygame.time.Clock()

    def __init__(self):
        self.setup()

    def setup(self) -> None:
        pygame.init()
        pygame.display.set_caption("2048 - github: olamide142")
        global screen
        screen = pygame.display.set_mode((
            self.__size_x,
            self.__size_y
        ))

    def run(self):
        screen.fill(COLOR['GRID_PRI'])
