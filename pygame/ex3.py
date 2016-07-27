import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()
size = (700, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Load Image")

done = False

clock = pygame.time.Clock()

carImg = pygame.image.load('car12.png')


def placeCar(x,y):
	screen.blit(carImg, (x,y))

rect_x = 50

rect_y = 50

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			break
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				rect_x += 5
			elif event.key == pygame.K_DOWN:
				rect_x -= 5				
	screen.fill(WHITE)
	placeCar(rect_x,rect_y)
	pygame.display.flip()		
	clock.tick(60)












