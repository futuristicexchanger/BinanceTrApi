class TimeModel:
    def __init__(self, timeData):
        self.code = timeData["code"]
        self.ms = timeData["ms"]
        self.data = timeData["data"]
        self.timestampt = timeData["timestampt"]
