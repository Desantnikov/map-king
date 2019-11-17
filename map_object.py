class MapObject:
    """
    Generic class for all objects on a map

    """

    def __init__(self, x, y):
        self.x, self.y = x, y

    def get_location(self):
        return self.x, self.y

