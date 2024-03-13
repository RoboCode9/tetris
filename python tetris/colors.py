class Colors:
    grey = (127, 127, 127)
    green = (0, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)
    yellow = (255, 255, 0)
    purple = (255, 0, 255)
    aqua = (0, 255, 255)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    dark_red = (127, 44, 44)
    light_red = (162, 85, 59)

    @classmethod
    def get_cell_colors(cls):
        return [cls.grey, cls.green, cls.red, cls.black, cls.yellow, cls.purple, cls.aqua, cls.blue]