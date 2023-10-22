
# Import a library of functions called 'pygame'
import pygame

#init the game
pygame.init()
 
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Set the height and width of the screen
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Akif text Rotate")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
text_rotate_degrees = 50
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

 
    # Clear the screen and set the screen background
    screen.fill(GREEN)


 
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Verdana', 50, True, False)
 
    # Animated rotation
    text = font.render("AKIF", False, RED)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    text_rotate_degrees += 5
    screen.blit(text, [100, 100])
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()