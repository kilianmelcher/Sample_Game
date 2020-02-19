import pygame
import images
import colors


class Enemy():

	def __init__(self,x,y,width,height,end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x,self.end]
		self.walk_count = 0
		self.speed = 3
		self.hitbox = (self.x + 17, self.y+2,31,57)
		self.health = 10
		self.visible = True

	def draw(self,display):
		self.move()

		#Check if he is alive
		if self.visible:

			if self.walk_count + 1 >= 33:
				self.walk_count = 0	 

			if self.speed > 0:
				#Draw moving right
				display.blit(images.enemy_walk_right[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

			else:
				#Draw moving left
				display.blit(images.enemy_walk_left[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

			#Set the position as the enemy walks
			self.hitbox = (self.x + 17, self.y+2,31,57)

			#Draw life bar
			pygame.draw.rect(display,colors.red, (self.hitbox[0],self.y - 20,50,10) )
			pygame.draw.rect(display,colors.green, (self.hitbox[0],self.y - 20, self.health*5 ,10) )

	def get_enemy_hitbox(self,display):
		return pygame.draw.rect(display,colors.red,self.hitbox)

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
			self.visible = False
