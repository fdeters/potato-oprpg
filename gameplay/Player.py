class Player:
    def __init__(self, name) -> None:
        self._name = name

        self._destiny = 0
        self._potatoes = 0
        self._orcs = 0
    
    def __str__(self) -> str:
        return f"{self._name}'s stats: {self._destiny} Destiny | {self._potatoes} Potatoes | {self._orcs} Orcs"

    def hurl(self, danger_level: int) -> None:
        """Remove potatoes to remove orcs."""
        if self.potatoes < danger_level:
            raise ValueError(f"You must have at least {danger_level} potatoes to hurl!")
        if self.orcs < 1:
            raise ValueError("No orcs threaten you right now.")

        self.potatoes -= danger_level
        self.orcs -= 1

    @property
    def destiny(self):
        return self._destiny
    
    @destiny.setter
    def destiny(self, value):
        if value < 0:
            raise ValueError("Destiny cannot be lower than zero")
        self._destiny = value

    @property
    def potatoes(self):
        return self._potatoes
    
    @potatoes.setter
    def potatoes(self, value):
        if value < 0:
            raise ValueError("Potatoes cannot be lower than zero")
        self._potatoes = value
    
    @property
    def orcs(self):
        return self._orcs
    
    @orcs.setter
    def orcs(self, value):
        if value < 0:
            raise ValueError("Orcs cannot be lower than zero")
        self._orcs = value
