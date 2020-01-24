class Target:
    def __init__(self, galaxy, ss_system, planet, proximity):
        self.galaxy = galaxy
        self.ss_system = ss_system
        self.planet = planet
        self.proximity = proximity

    def location(self):
        return f"[{self.galaxy}:{self.ss_system}:{self.planet}]"
