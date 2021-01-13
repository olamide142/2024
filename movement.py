class Movement:
    
    def __init__(self, data):
        self.data = data

    def up(self):
        self.__2048Stack(self.data).up()
    def down(self):
        self.__2048Stack(self.data).down()
    def left(self):
        self.__2048Stack(self.data).left()
    def right(self):
        self.__2048Stack(self.data).right()

    class __2048Stack:

        def __init__(self, data):
            self.data = data
            self.stack = []

        def right(self):
            for datum in self.data:
                self.stack.append(stack_it_right(datum))
        print(stack)


        def down(self):
            pass