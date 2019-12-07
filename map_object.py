from loguru import logger

class MapObject:
    """
    Generic class for all objects that are present on a map

    """

    def __init__(self, x, y):


        #if not all([x, y]):
        #    raise ValueError(f'Blank position or no logger')

        self.x, self.y = x, y


    def get_location(self):
        return self.x, self.y

