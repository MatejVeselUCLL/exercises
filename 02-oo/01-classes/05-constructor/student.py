class Wall:
    armor = 10
    height = 5

    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = self.width * self.height * self.depth

    # def get_cost(self):
    #     return self.armor * self.height

    # # don't touch below this line

    # def fortify(self):
    #     self.armor *= 2