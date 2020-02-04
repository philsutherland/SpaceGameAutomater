class Target:
    def __init__(self, galaxy, system, planet, proximity, color):
        self.galaxy = galaxy
        self.system = system
        self.planet = planet
        self.proximity = proximity
        self.color = color

    def location(self):
        return f"[{self.galaxy}:{self.system}:{self.planet}e]"
