class Box:
    size = 70
    boxes = [
        [0, 50, 50, 0],
        [0, 50, 70, 0],
        [0, 0, 70, 0],
        [0, 0, 80, 0]
    ]

    def __init__(self, position=0):
        self.gen_starting_box()

    def gen_starting_box(self):

        a = random.choice(self.generate_random_position())
        b = random.choice(self.generate_random_position())

        if all((Box.can_render(a), Box.can_render(b),  a != b)):
            Box.boxes[a[0]][a[1]] = random.choice([2, 4])
            Box.boxes[b[0]][b[1]] = random.choice([2, 4])

    def generate_random_position(self):

        for i in range(len(Box.boxes)):
            for  j in Box.boxes[i]:
                if j == 0:
                    return tuple((i, j))

    def run(self):

        for x in range(1, 5):
            for y in range(2, 6):
                rect = pygame.Rect(x * Box.size, y * Box.size,
                                   Box.size - 4, Box.size - 4)

                if Box.can_render(Box.boxes[x - 1][y - 2]):
                    screen.blit(font_size['MEDIUM'].render(
                        str(Box.boxes[x - 1][y - 2]),
                        True, COLOR['TXT_PRI']),
                        (rect.left + 25 // 2, rect.bottom - 35))

    @staticmethod
    def can_render(data):
        return data != 0

    @staticmethod
    def move(key):

        a = [Box.boxes[i][0] for i in range(4)]
        b = [Box.boxes[i][1] for i in range(4)]
        c = [Box.boxes[i][2] for i in range(4)]
        d = [Box.boxes[i][3] for i in range(4)]
        
        data = (a, b, c, d)
        if key == pygame.K_UP:
            Movement(data).up()
        if key == pygame.K_UP:
            Movement(data).down()
        if key == pygame.K_LEFT:
            Movement(data).left()
        if key == pygame.K_RIGHT:
            Movement(data).right()
