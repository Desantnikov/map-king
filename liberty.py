class Liberty:
    # cell owned by liberty == nobody's cell

    def __init__(self):
        self.id = None
        self.location = None

    def serialize(self):
        return {'id': self.id,
                'location': self.location}
