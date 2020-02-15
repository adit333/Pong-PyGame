# Pong V1.
# In this version the dot bounces of the edge of the screen.
# The dot passes throught the paddles.
# The score does not appear.
# The game is ended when the close button is clicked.

import pygame, random

class Game:
   def __init__(self, surface):
      # General game attributes
      self.surface = surface
      self.bg_color = pygame.Color('black')
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      
      # Specific game attributes
       # Dot attributes
      self.dot = Dot('white', 5, [100,100], [2, 1], self.surface)
       # Paddle attributes
      self.left_paddle = Paddle(self.surface, 'white', 100, 175, 10, 50)
      self.right_paddle = Paddle(self.surface, 'white', 400, 175, 10, 50)

   def play(self):
      # Play the game until the player presses the close box.

      while self.close_clicked == False:  # until player clicks close box
         self.handle_events()
         self.draw()            
         if self.continue_game == True:
            self.update()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True

   def draw(self):
      # Draw all game objects.
      self.surface.fill(self.bg_color) # clear the display surface first
      self.dot.draw()
      self.left_paddle.draw()
      self.right_paddle.draw()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects.     
      self.dot.move()


class Dot:
   # An object in this class represents a Dot that moves 
   
   def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
      # Initialize a Dot.
      # - self is the Dot to initialize
      self.color = pygame.Color(dot_color)
      self.radius = dot_radius
      self.center = dot_center
      self.velocity = dot_velocity
      self.surface = surface
      
   def move(self):
      size = self.surface.get_size()      # size is a tuple [width, height]
      for index in range(0,2):
         self.center[index] = self.center[index] + self.velocity[index]
         # Left or top
         if self.center[index] < self.radius: 
            self.velocity[index] = -self.velocity[index]
         # Right or bottom
         if self.center[index] + self.radius > size[index]:
            self.velocity[index] = -self.velocity[index]      
  
   def draw(self):
      # Draw the dot on the surface
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
      

class Paddle:
   def __init__(self, surface, rect_color, rect_x, rect_y, width, height):
      # initialise the paddle.
      self.rect_x = rect_x
      self.rect_y = rect_y
      self.width = width
      self.height = height
      self.surface = surface
      self.rect_color = pygame.Color(rect_color)
      
   def draw(self):
      # Draw the paddle onto the surface
      pygame.draw.rect(self.surface, self.rect_color, (self.rect_x, self.rect_y, self.width, self.height))   
     
   
def main():
   # Initializes pygame
   pygame.init()
   
   # Creates a pygame display window
   pygame.display.set_mode((500, 400))
   
   # Set the title of the display window
   pygame.display.set_caption('Pong')
   
   # Get the display surface
   w_surface = pygame.display.get_surface() 
   
   # Creates a game object
   game = Game(w_surface)
   
   # Start the main game loop by calling the play method on the game object
   game.play() 
   
   # Quits pygame
   pygame.quit() 

main()