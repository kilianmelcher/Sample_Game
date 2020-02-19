import pygame
import colors
import images
import sounds
import player_module

pygame.init()

#Screen size
screen_width = 852
screen_height = 480

game_display = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Learning')

#Time object to work with Frames each Second
clock = pygame.time.Clock()

#Frames per second
FPS = 27

#play background music
pygame.mixer.music.play(-1)


class Projectile(object):
	def __init__(self,x,y,radius,color,direction):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.direction = direction
		self.speed = 10 * direction
		self.hitbox = (self.x,self.y,5,5)

	def draw(self,display):	
		pygame.draw.circle(game_display,self.color, (self.x,self.y) ,self.radius)

		#Set the position as the bullet moves
		self.hitbox = (self.x,self.y,5,5)

	def get_projectile_hitbox(self):
		return pygame.draw.rect(game_display,colors.red,self.hitbox)


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
				game_display.blit(images.enemy_walk_right[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

			else:
				#Draw moving left
				game_display.blit(images.enemy_walk_left[self.walk_count//3], (self.x,self.y) )
				self.walk_count += 1

			#Set the position as the enemy walks
			self.hitbox = (self.x + 17, self.y+2,31,57)

			#Draw life bar
			pygame.draw.rect(game_display,colors.red, (self.hitbox[0],self.y - 20,50,10) )
			pygame.draw.rect(game_display,colors.green, (self.hitbox[0],self.y - 20, self.health*5 ,10) )

	def get_enemy_hitbox(self):
		return pygame.draw.rect(game_display,colors.red,self.hitbox)

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
	


def draw_window():
	game_display.blit(images.background, (0,0))
	john.draw(game_display)
	goblin.draw(game_display)

	for bullet in bullets:
		bullet.draw(game_display)

	pygame.display.update()



#Creating the characther
john = player_module.Player(300,380,64,64)
#Creating enemy
goblin = Enemy(100,385,64,64,screen_width-100)

bullets = []


#Main loop
run = True

while run:
	
	
		
	for bullet in bullets:

		bullet_hitbox = bullet.get_projectile_hitbox()
		goblin_hitbox = goblin.get_enemy_hitbox()

		#Deletes the bullet when hits the goblin
		if bullet_hitbox.colliderect(goblin_hitbox):
			bullets.pop(bullets.index(bullet))
			goblin.hit()
			sounds.hit_sound.play()
			


		if bullet.x < screen_width and bullet.x > 0:
			bullet.x += bullet.speed

		else: 
			#Deletes the bullet when is off screen
			bullets.pop(bullets.index(bullet))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:

				if john.left:
					direction = -1

				elif john.right:
					direction = 1

				#Set the maximium bullets at the same time on the screen
				if len(bullets) < 5:
					sounds.bullet_sound.play()
					bullets.append(Projectile( round(john.x+john.width//2) , round(john.y+john.height//2) ,5,colors.red,direction))


	press = pygame.key.get_pressed()

	if press[pygame.K_LEFT] and john.x > john.speed:
		john.x -= john.speed
		john.left = True
		john.right = False
		john.standing = False

	elif press[pygame.K_RIGHT] and john.x < screen_width - john.width - john.speed:
		john.x += john.speed
		john.right = True
		john.left = False
		john.standing = False

	else:
		john.standing = True
		john.walk_count = 0

	if not john.jumping:

		if press[pygame.K_UP]:
			sounds.jump_sound.play()
			john.jumping = True
			john.walk_count = 0


	else:

		if john.jump_count >= -10:
			negative = 1

			if john.jump_count < 0:
				negative = -1

			john.y -= (john.jump_count ** 2) * 0.5 * negative 
			john.jump_count -= 1

		else:
			john.jumping = False
			john.jump_count = 10

	draw_window()
	
	clock.tick(FPS)

pygame.quit()
