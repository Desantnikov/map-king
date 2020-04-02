class MapObject:
    """
    Generic class for all objects on a map

    """

    def __init__(self, x, y, object_name=None):
        self.x, self.y = x, y
        self.object_name = object_name

    def get_location(self):
        return self.x, self.y

    def get_object_name(self):
        return self.object_name