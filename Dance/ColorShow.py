import sys

class ColorShow:

    def __init__(self, color_number = 3,
                       color = 'GREEN'):

        self.color_numbers = [3, 4, 5, 8]
        self.colors = ['GREEN', 'YELLOW', 'RED', 'ORANGE']

        self.color = color if color_number == 3 else self.colors[self.color_numbers.index(color_index)]
        self.color_number = color_number if color == 'GREEN' else self.color_numbers[self.colors.index(color)]

        self.color_index = self.colors.index(self.color)
        

    def get_next_color(self):

        color_index = self.colors.index(self.color)
        next_color_index = color_index + 1 if color_index + 1 != len(self.colors) else 0

        self.color = self.colors[next_color_index]
        self.color_index = next_color_index
        self.color_number = self.color_numbers[self.color_index]

        return self.color, self.color_numbers[self.color_index]




