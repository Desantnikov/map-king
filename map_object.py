class MapObject:
    """
    Generic class for all objects on a map

    """

    def __init__(self, x, y, image_name=None):
        self.x, self.y = x, y
        self.image_name = image_name

    def get_location(self):
        return self.x, self.y

    def get_image_name(self):
        return self.image_name