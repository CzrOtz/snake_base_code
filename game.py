from tkinter import Grid
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 680
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up the game grid
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Set up the snake
snake_blocks = [(2, 0), (1, 0), (0, 0)]  # The starting position of the snake 
snake_direction = 'down'  # The direction the snake is moving in

head_x, head_y = snake_blocks[0] #this is called touple unpacking

r1_x = random.randint(0, GRID_SIZE)
r1_y = random.randint(0, GRID_SIZE)
r2_x = random.randint(0, GRID_SIZE)
r2_y = random.randint(0, GRID_SIZE)

snake_food = [(r1_x, r1_y), (r2_x, r2_y)]

food_counter = 2


snake_length = 3

clock = pygame.time.Clock()

# Main game loop
running = True

once = True

while running:
  

    

    # Store the position of the food in a list
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                snake_direction = 'up'
            
            if event.key == pygame.K_DOWN:
                snake_direction = 'down'
            
            if event.key == pygame.K_RIGHT:
                snake_direction = 'right'
            
            if event.key == pygame.K_LEFT:
                snake_direction = 'left'


    if snake_direction == 'up':
        head_y -= 1
    elif snake_direction == 'down':
        head_y += 1
    elif snake_direction == 'right':
        head_x += 1
    elif snake_direction == 'left':
        head_x -= 1
    
    # if x is less than 0 or greater than width, or y is less than zero or greater than heigth, end the game
    #this is for boundaries
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        running = False

    # Check for collision with snake body
    #checking to see if the tuple is in the second to i'th element of the array
    #what does it mean if the head is somewhere else other than the front? collision
    if (head_x, head_y) in snake_blocks[1:]:
        print(' crashed into yourself, game over, your score was  ', snake_length - 3)
        running = False
    
    # Update the snake's position
    #at index 0 of the snake, you're inserting a touple contianing the next block
    
    snake_blocks.insert(0, (head_x, head_y))
    
    if (head_x, head_y) != snake_blocks[-2]:
        snake_blocks.pop()
    
    # Clear the screen
    game_window.fill((0, 0, 0))
    
    # Draw the game grid
    for x in range(GRID_WIDTH):
        pygame.draw.line(game_window, (255, 255, 255), (x * GRID_SIZE, 0), (x * GRID_SIZE, WINDOW_HEIGHT))
    for y in range(GRID_HEIGHT):
        pygame.draw.line(game_window, (255, 255, 255), (0, y * GRID_SIZE), (WINDOW_WIDTH, y * GRID_SIZE))
    
   
    for block in snake_blocks:
        snake_color1 = random.randint(10, 70)
        snake_color2 = random.randint(150, 255)
        snake_color3 = random.randint(10, 70)

        #the position of the blocks are miltiples of the grid so it gives it the 
        #illusion of being whithin the grid
        #in reality whats happening is that the blocks are fitting within the grid lines
        block_rect = pygame.Rect(block[0] * GRID_SIZE, block[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(game_window, (snake_color1, snake_color2, snake_color3), block_rect)

    #display the snake food
    # pygame.Rect(x, y, width, height)
    for food in snake_food:
        #remeber that food is a tuple [(x,y), (x,y)]
    
        food_rect = pygame.Rect(food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(game_window, (255,0,0), food_rect)
    
        if (head_x, head_y) == food:
            snake_blocks.append(snake_blocks[-1])  # Add a new block to the snake
            # snake_food.remove(food)  # Remove the food that was eaten
            snake_length += 1
            print(' hit +1 snake length is now => ', snake_length)
            # Remove the eaten food and add a new one
            snake_food.remove((head_x, head_y))



            for i in range(food_counter):
                snake_food.append((random.randint(0, GRID_WIDTH), random.randint(0, GRID_HEIGHT)))
                
                
                
                    

            
