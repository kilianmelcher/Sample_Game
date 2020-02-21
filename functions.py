import pygame
import colors

def message_to_screen(message,display,color,x,y,font_size=20):

	#Set the font and the size
	font = pygame.font.Font('PressStart2P-Regular.ttf',font_size)
	#Write the message and set the color
	text = font.render(message,True,color)
	#Align the text as you wish
	text_rectangle = text.get_rect(center=(x, y)) 
	#Print the text in the screen
	display.blit(text, text_rectangle)

