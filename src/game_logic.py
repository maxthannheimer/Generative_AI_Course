def update_game_state(player1, player2):
    player1.move()
    player2.move()

    if check_collision(player1, player2):
        player1.eat(player2)
        return True  # Player 1 has eaten Player 2
    return False  # No collision

def check_collision(player1, player2):
    distance = ((player1.position[0] - player2.position[0]) ** 2 + 
                (player1.position[1] - player2.position[1]) ** 2) ** 0.5
    return distance < (player1.size + player2.size) / 2

def reset_game(player1, player2):
    player1.position = [200, 200]  # Reset to starting position
    player2.position = [1600, 800]  # Reset to starting position
    player1.size = 100  # Reset size
    player2.size = 100  # Reset size

def is_game_over(player2):
    return player2.size <= 0  # Player 2 is eaten and no longer exists