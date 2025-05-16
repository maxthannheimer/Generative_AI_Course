import pygame
import sys
import random
from game_logic import update_game_state, reset_game, is_game_over

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1800, 1000  # Updated resolution
FPS = 60
TIMER_START = 15  # Timer starts at 15 seconds

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Game")
font = pygame.font.Font(None, 36)  # Font for displaying scores

# Initialize timer
timer_start_ticks = pygame.time.get_ticks()  # Record the start time

# Define the Player class (if not already defined elsewhere)
class Player:
    def __init__(self, position, size, color, controls, image_path=None):
        self.position = position
        self.size = size
        self.color = color
        self.controls = controls
        self.speed = 5
        self.score = 0  # Initialize score
        self.image = pygame.image.load(image_path) if image_path else None
        self.original_image = None
        self.flipped_image = None
        if self.image:
            # Scale the image
            self.image = pygame.transform.scale(self.image, (int(self.size * 3), int(self.size * 3)))  # 1.5x size
            self.original_image = self.image  # Store the original image
            self.flipped_image = pygame.transform.flip(self.image, True, False)  # Create a flipped version

    def move(self):
        keys = pygame.key.get_pressed()
        new_position = self.position[:]

        if keys[self.controls['up']] and self.position[1] - self.size > 0:
            new_position[1] -= self.speed
        if keys[self.controls['down']] and self.position[1] + self.size < HEIGHT:
            new_position[1] += self.speed
        if keys[self.controls['left']] and self.position[0] - self.size > 0:
            new_position[0] -= self.speed
            if self.original_image:  # Flip image when moving left
                self.image = self.flipped_image
        if keys[self.controls['right']] and self.position[0] + self.size < WIDTH:
            new_position[0] += self.speed
            if self.original_image:  # Restore original image when moving right
                self.image = self.original_image

        # Create a temporary rectangle for the player's new position
        player_rect = pygame.Rect(new_position[0] - self.size, new_position[1] - self.size, self.size * 2, self.size * 2)

        # Check for collision with the wall
        if not player_rect.colliderect(wall):
            self.position = new_position  # Update position only if no collision

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.position[0] - self.size, self.position[1] - self.size))
        else:
            pygame.draw.circle(screen, self.color, self.position, self.size)

    def eat(self, other):
        self.size += other.size // 2
        self.score += 1  # Increment score when eating another player
        other.size = 0

# Create player instances with adjusted starting positions
player1 = Player([200, 200], 50, (255, 0, 0), 
                 {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d}, 
                 image_path="/home/thannhmx/Git/Generative_AI_Course/src/logo.png")  # Replace with the actual path to your image
player2 = Player([1600, 800], 50, (0, 0, 255), 
                 {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT},
                 image_path="/home/thannhmx/Git/Generative_AI_Course/src/KI-Geldberg.jpg")  # Replace with the actual path to your image

# Define the wall
wall = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 4, 100, HEIGHT // 2)  # A vertical wall in the middle

# Load the hamburger image
hamburger_image = pygame.image.load("/home/thannhmx/Git/Generative_AI_Course/src/hamburger.jpg")  # Replace with the actual path
hamburger_image = pygame.transform.scale(hamburger_image, (40, 40))  # Scale to a smaller size

# List to store hamburgers
hamburgers = []

# Function to spawn a hamburger at a random position
def spawn_hamburger():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    hamburgers.append(pygame.Rect(x, y, 40, 40))  # Add a new hamburger rectangle

# Function to handle hamburger collisions
def handle_hamburger_collisions():
    for hamburger in hamburgers[:]:  # Iterate over a copy of the list
        if pygame.Rect(player1.position[0] - player1.size, player1.position[1] - player1.size, player1.size * 2, player1.size * 2).colliderect(hamburger):
            player1.score += 0.5  # Player 1 gets 0.5 points
            hamburgers.remove(hamburger)  # Remove the hamburger
        elif pygame.Rect(player2.position[0] - player2.size, player2.position[1] - player2.size, player2.size * 2, player2.size * 2).colliderect(hamburger):
            player2.score += 0.5  # Player 2 gets 0.5 points
            hamburgers.remove(hamburger)  # Remove the hamburger

def show_title_screen():
    # Load the logo
    logo = pygame.image.load("/home/thannhmx/Git/Generative_AI_Course/src/logo.png")
    logo = pygame.transform.scale(logo, (400, 400))  # Scale the logo

    # Title screen loop
    while True:
        screen.fill((0, 0, 0))  # Clear the screen

        # Display the logo
        screen.blit(logo, (WIDTH // 2 - 200, 100))  # Center the logo at the top

        # Display the title
        title_text = font.render("Two Player Game", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 520))

        # Display the game explanation
        explanation_text = [
            "Player 1 (Frank): Use W, A, S, D to move.",
            "Player 2 (KI): Use Arrow Keys to move.",
            "Player 1 chases Player 2 to eat them.",
            "If the timer reaches 0, Player 2 gets a point.",
            "In HAMBURGER Mode, collect hamburgers for extra points.",
        ]
        for i, line in enumerate(explanation_text):
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 580 + i * 40))

        # Display the game mode options
        normal_text = font.render("Press SPACE for NORMAL Mode", True, (255, 255, 0))
        hamburger_text = font.render("Press ENTER for HAMBURGER Mode", True, (255, 255, 0))
        screen.blit(normal_text, (WIDTH // 2 - normal_text.get_width() // 2, 800))
        screen.blit(hamburger_text, (WIDTH // 2 - hamburger_text.get_width() // 2, 850))

        # Refresh the display
        pygame.display.flip()

        # Check for key press to start the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "NORMAL"  # Start NORMAL mode
                if event.key == pygame.K_RETURN:
                    return "HAMBURGERS"  # Start HAMBURGERS mode

# Show the title screen and get the selected mode
game_mode = show_title_screen()

# Function to show score change message
def show_score_change_message(player, points):
    # Create the message text
    message = f"{player} +{points} Points!"
    message_surface = font.render(message, True, (255, 255, 0))  # Yellow text
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text

    # Display the message for 0.5 seconds
    screen.blit(message_surface, message_rect)
    pygame.display.flip()
    pygame.time.delay(500)  # Delay for 0.5 seconds

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    player1.move()
    player2.move()

    # Update game state
    if update_game_state(player1, player2):
        print("Player 1 ate Player 2!")
        reset_game(player1, player2)
        timer_start_ticks = pygame.time.get_ticks()  # Reset the timer

    # Check if the game is over
    if is_game_over(player2):
        print("Game Over!")
        running = False

    # Calculate remaining time
    elapsed_time = (pygame.time.get_ticks() - timer_start_ticks) / 1000  # Convert to seconds
    remaining_time = max(0, TIMER_START - int(elapsed_time))  # Ensure it doesn't go below 0

    # Check if timer reached zero
    if remaining_time == 0:
        print("Timer reached zero! Player 2 gets a point.")
        player2.score += 1  # Increment Player 2's score
        reset_game(player1, player2)
        timer_start_ticks = pygame.time.get_ticks()  # Reset the timer

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw players
    player1.draw(screen)
    player2.draw(screen)

    # Draw the wall
    pygame.draw.rect(screen, (255, 255, 255), wall)  # White wall

    # Handle HAMBURGERS mode
    if game_mode == "HAMBURGERS":
        # Spawn a hamburger every 3 seconds
        if pygame.time.get_ticks() % 3000 < FPS:
            spawn_hamburger()

        # Handle collisions with hamburgers
        handle_hamburger_collisions()

        # Draw hamburgers
        for hamburger in hamburgers:
            screen.blit(hamburger_image, (hamburger.x, hamburger.y))

    # Display scores
    score_text1 = font.render(f"Frank Müller Score: {player1.score}", True, (255, 255, 255))
    score_text2 = font.render(f"KI Score: {player2.score}", True, (255, 255, 255))
    screen.blit(score_text1, (10, 950))  # Adjusted for bottom-left corner
    screen.blit(score_text2, (1600, 950))  # Adjusted for bottom-right corner

    # Display timer
    timer_text = font.render(f"Time Left: {remaining_time}s", True, (255, 255, 255))
    screen.blit(timer_text, (WIDTH // 2 - 100, 950))  # Centered at the bottom

    # Refresh the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()