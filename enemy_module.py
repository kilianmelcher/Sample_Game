import pygame
import images
import colors


class Enemy():

	def __init__(self,x,y,width,height,end,display):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x,self.end]
		self.walk_count = 0
		self.speed = 3
		self.hitbox = pygame.Rect(self.x + 17, self.y+2,31,57)
		self.health = 10
		self.alive = True
		self.display = display

	def draw(self):
		self.move()

		#Check if he is alive
		if self.alive:

			if self.walk_count + 1 >= 33:
				self.walk_count = 0	 

			if self.speed > 0:
				#Draw moving right
				self.display.blit(images.enemy_walk_right[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

			else:
				#Draw moving left
				self.display.blit(images.enemy_walk_left[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

			#Set the position as the enemy walks
			self.hitbox = pygame.Rect(self.x + 17, self.y+2,31,57)

			#Draw life bar
			pygame.draw.rect(self.display,colors.red, (self.x + 17,self.y - 20,50,10) )
			pygame.draw.rect(self.display,colors.green, (self.x + 17,self.y - 20, self.health*5 ,10) )
			


	def move(self):
		if self.speed > 0:
			#Going right
			if self.x + self.speed < self.path[1]:
				self.x += self.speed

			else:
				self.speed *= -1
				self.walk_count = 0

		else:
			#Going left
			if self.x - self.speed > self.path[0]:
				self.x += self.speed

			else:
				self.speed *= -1
				self.walk_count = 0


	def hit(self):

		if self.health > 1:
			self.health -= 1
		else: 
			self.alive = False
