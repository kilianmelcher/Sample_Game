import pygame
import images
import functions
import colors

class Player(object):

	def __init__(self,x,y,width,height,display,display_width,display_height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = 5
		self.jumping = False
		self.jump_count = 10
		self.left = False
		self.right = True
		self.walk_count = 0
		self.standing = True
		self.hitbox = pygame.Rect(self.x+18,self.y+12,28,50)
		self.display_width = display_width
		self.display_height = display_height
		self.display = display
		self.health = 10
		self.alive = True


	def draw(self):

		if self.walk_count + 1 >= 27:
			self.walk_count = 0

		if not self.standing:

			if self.left:
				self.display.blit(images.walk_left[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

			elif self.right:
				self.display.blit(images.walk_right[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

		else: 

			if self.right:
				self.display.blit(images.walk_right[0], (self.x,self.y) )
			else:
				self.display.blit(images.walk_left[0], (self.x,self.y) )

		#Set the position as the character walks
		self.hitbox = pygame.Rect(self.x+18,self.y+12,28,50)

		functions.message_to_screen('Your life', self.display, colors.black, 80,30,14)

		#Draw lifebar
		pygame.draw.rect(self.display,colors.black, (28,48,104,24) )
		pygame.draw.rect(self.display,colors.red, (30,50,100,20) )
		pygame.draw.rect(self.display,colors.green, (30,50, self.health*10 ,20) )

		
	def hit(self):
		#Stop the jumping to avoid going off the screen
		self.jumping = False
		self.jump_count = 10

		if self.health > 1:
			self.health -= 1
		else: 
			#Death
			self.alive = False
			

		#When player collides with goblin, resets his prosition
		self.x = 60
		self.y = 380
		self.walk_count = 0

		pygame.display.update()


