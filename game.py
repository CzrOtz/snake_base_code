# Import the Pygame library
from re import L
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up the game grid
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Set up the snake
snake_blocks = [(2, 0), (1, 0), (0, 0)]  # The starting position of the snake 
snake_direction = 'down'  # The direction the snake is moving in

head_x, head_y = snake_blocks[0] #this is called touple unpacking

# Main game loop
running = True
while running:
    # Handle events
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                head_y -= 1
            
            if event.type == pygame.K_DOWN:
                head_y += 1
            
            if event.type == pygame.K_RIGHT:
                head_x += 1
            
            if event.type == pygame.K_LEFT:
                head_x -= 1

    
    
    
    
    # if x is less than 0 or greater than width, or y is less than zero or greater than heigth, end the game
    #this is for boundaries
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        running = False
    
    # Check for collision with snake body
    if (head_x, head_y) in snake_blocks[1:]:
        running = False
    
    # Update the snake's position
    #if 
    snake_blocks.insert(0, (head_x, head_y))
    if (head_x, head_y) != snake_blocks[-1]:
        snake_blocks.pop()
    
    # Clear the screen
    game_window.fill((0, 0, 0))
    
    # Draw the game grid
    for x in range(GRID_WIDTH):
        pygame.draw.line(game_window, (255, 255, 255), (x * GRID_SIZE, 0), (x * GRID_SIZE, WINDOW_HEIGHT))
    for y in range(GRID_HEIGHT):
        pygame.draw.line(game_window, (255, 255, 255), (0, y * GRID_SIZE), (WINDOW_WIDTH, y * GRID_SIZE))
    
    # Draw the snake
    for block in snake_blocks:
        block_rect = pygame.Rect(block[0] * GRID_SIZE, block[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(game_window, (0, 255, 0), block_rect)
    
    # Update the screen
    pygame.display.update()
    
    # Set the game's frame rate
    FPS = 60
    clock = pygame.time.Clock()
    clock.tick(FPS)