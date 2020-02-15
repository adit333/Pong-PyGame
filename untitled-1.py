# Pong V3.
# In this version the dot bounces of the edge of the screen.
# The dot passes through only the front side of the paddle.
# The score appears.
# The game is ended when either score reaches 11 or close button is clicked .

import pygame, random


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
      
   
   def re_center(self):
      return self.center
   def re_velocity(self):
      return self.velocity
      
   def set_velocity(self):
      self.velocity[0] = -self.velocity[0]
            
   def r_edge(self):
      # Checking right edge bounce
      if self.center[0] + self.radius > 500:
         return True
      
   def l_edge(self):
      # Checking left edge bounce
      if self.center[0] < self.radius:
         return True
  
   def draw(self):
      # Draw the dot on the surface
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
      



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
      self.dot = Dot('white', 5, [75,100], [2, 1], self.surface)
       # Paddle attributes
      self.l_paddle = pygame.Rect(100, 175, 10, 50)
      self.r_paddle = pygame.Rect(400, 175, 10, 50)      
      self.l_score = 0
      self.r_score = 0

   def play(self):
      # Play the game until the player presses the close box.
      while self.close_clicked == False:  # until player clicks close box
         self.handle_events()
         self.draw()            
         if self.continue_game == True:
            self.update()
            self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.KEYDOWN and self.continue_game:
               self.handle_key_down(event)
         if event.type == pygame.KEYUP and self.continue_game:
               self.handle_key_up(event)
               
   def handle_key_down(self, event):
      if event.key == pygame.K_q:
         self.l_paddle.move_ip(0,-5)
      if event.key == pygame.K_a:
         self.l_paddle.move_ip(0,+5)
   
   def handle_key_up(self, event):
      if event.key == pygame.K_p:
         self.r_paddle.move_ip(0,-5)
      if event.key == pygame.K_l:
         self.r_paddle.move_ip(0,+5)
   
   def left_score(self):
      # Setting up the color
      fg_color = pygame.Color('white')
      
      # Create font object
      font = pygame.font.SysFont(None, 100) 
      
      # Create left textbox by rensenring left font object
      l_text_box = font.render(str(self.l_score), True, fg_color, self.bg_color)
      
      # Compute location of text box
      l_location = (0,0)
      
      # Step 5 - Blit the textbox on the surface
      self.surface.blit(l_text_box, l_location) 

   def right_score(self):
      # Setting up the color
      fg_color = pygame.Color('white')
      
      # Create font object
      font = pygame.font.SysFont(None, 100) 
      
      # Create left textbox by rensenring left font object
      r_text_box = font.render(str(self.r_score), True, fg_color, self.bg_color)
      
      # Compute location of text box
      surface_width = self.surface.get_width()
      r_text_box_width = r_text_box.get_width()
      r_location = (surface_width - r_text_box_width, 0)
      
      # Step 5 - Blit the textbox on the surface
      self.surface.blit(r_text_box, r_location)
      

   def draw(self):
      # Draw all game objects.
      self.surface.fill(self.bg_color)
      
      # Draw the dot
      self.dot.draw()
      
      # Draw the paddles
      pygame.draw.rect(self.surface, pygame.Color('white'), self.l_paddle)
      pygame.draw.rect(self.surface, pygame.Color('white'), self.r_paddle)
      self.collison()
      
      
      # Draw the scores
      self.left_score()
      self.right_score()
      
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects.     
      self.dot.move()

      # Updating l_score
      if self.dot.r_edge() == True:
         self.l_score += 1      
      
      # Updating r_score
      if self.dot.l_edge() == True:
         self.r_score += 1
         
   def decide_continue(self):
      if self.l_score == 11 or self.r_score == 11:
         self.continue_game = False
         
   def collison(self):
      self.center = self.dot.re_center()
      self.velocity = self.dot.re_velocity()
      # Left paddle
      if pygame.Rect(self.l_paddle).collidepoint(self.center[0], self.center[1]) and self.velocity[0] < 0:
         self.dot.set_velocity()
      
      # Right paddle
      if pygame.Rect(self.r_paddle).collidepoint(self.center[0], self.center[1]) and self.velocity[0] < 0:
         self.dot.set_velocity()      
         
     
   
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