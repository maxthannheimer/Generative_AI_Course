class Player:
    def __init__(self, position, size, mouth_direction):
        self.position = position
        self.size = size
        self.mouth_direction = mouth_direction

    def move(self, direction):
        if direction == 'up':
            self.position[1] -= 5
        elif direction == 'down':
            self.position[1] += 5
        elif direction == 'left':
            self.position[0] -= 5
        elif direction == 'right':
            self.position[0] += 5

    def draw(self, screen):
        # Placeholder for drawing the player on the screen
        pass

    def eat(self, other_player):
        # Logic to determine if this player has eaten the other player
        pass