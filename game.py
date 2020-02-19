import pygame
import colors
import images
import sounds
import player_module
import enemy_module
import projectile_module

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
goblin = enemy_module.Enemy(100,385,64,64,screen_width-100)

bullets = []

#Main loop
run = True

while run:
	
	
	#Bullet events
	for bullet in bullets:

		bullet_hitbox = bullet.get_projectile_hitbox(game_display)
		goblin_hitbox = goblin.get_enemy_hitbox(game_display)

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
