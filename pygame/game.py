import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()
size = (700, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving Box")



done = False
clock = pygame.time.Clock()

rect_x = 50
rect_y = 50
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(WHITE)
	pygame.draw.rect(screen, RED, [rect_x,rect_y,50,50])
	if rect_y == 50 and rect_x >= 50 and rect_x <=150:
		rect_x += 1
	
	if rect_x == 150 and rect_y >= 50 and rect_y <=150:
		rect_y += 1
	
	if rect_y == 150 and rect_x >= 50 and rect_x <= 150:
		rect_x -= 1

	if rect_x == 50 and rect_y >=50 and rect_y<=150:
		rect_y -= 1

	pygame.display.flip()
	clock.tick(60)

pygame.quit()