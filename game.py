import pygame
import colors
import images
import sounds
import player_module
import enemy_module
import projectile_module
import functions

pygame.init()

#Display size
display_width = 852
display_height = 480

#Draw display
game_display = pygame.display.set_mode((display_width,display_height))

#Game title
pygame.display.set_caption('Learning')

#Time object to work with Frames each Second
clock = pygame.time.Clock()

#Frames per second
FPS = 27

#play background music
pygame.mixer.music.play(-1)



def draw_window():
	game_display.blit(images.background, (0,0))
	john.draw()
	goblin.draw()

	for bullet in bullets:
		bullet.draw(game_display)

	pygame.display.update()


#Creating the characther
john = player_module.Player(300,380,64,64,game_display,display_width,display_height)
#Creating enemy
goblin = enemy_module.Enemy(100,385,64,64,display_width-100,game_display)

bullets = []


def game_over():

	#Draw game over screen
	functions.message_to_screen("Game over",game_display,colors.red, display_width//2,display_height//2-50)
	functions.message_to_screen("Press C to play again or Q to quit",game_display,colors.black,
								display_width//2, display_height//2 + -10)
	pygame.display.update()

	while True:
		
		#Player choices
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_c:
				#Restart game

				elif event.key == pygame.K_q:
					pygame.quit()

def game_loop():

	#Main loop
	run = True

	while run:


		#Check if the goblin is alive
		if goblin.alive == True:
			#Check if the player collides with the goblin
			if john.hitbox.colliderect(goblin.hitbox):
				john.hit()

		
		#Bullet events
		for bullet in bullets:

			#Check if the goblin is alive
			if goblin.alive == True:
				#Deletes the bullet when hits the goblin
				if bullet.hitbox.colliderect(goblin.hitbox):
					bullets.pop(bullets.index(bullet))
					goblin.hit()
					sounds.hit_sound.play()
				

			if bullet.x < display_width and bullet.x > 0:
				bullet.x += bullet.speed

			else: 
				#Deletes the bullet when is off screen
				bullets.pop(bullets.index(bullet))


		#User events
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
						bullets.append(projectile_module.Projectile( round(john.x+john.width//2) , round(john.y+john.height//2) ,5,colors.red,direction))


		#User pressed keys events
		press = pygame.key.get_pressed()

		if press[pygame.K_LEFT] and john.x > john.speed:
			john.x -= john.speed
			john.left = True
			john.right = False
			john.standing = False

		elif press[pygame.K_RIGHT] and john.x < display_width - john.width - john.speed:
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

		if john.alive:
			draw_window()
		else:
			game_over()
		
		clock.tick(FPS)

	pygame.quit()

game_loop()
