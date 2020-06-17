import pygame
pygame.init()

win=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("TIC-TAC-TOE")


#global variables
t = 0
pos = 0
movesxy = (100 , 100)
movexy = [ (j , i ) for i in range (300 , 99 , -100) for j in range (100 , 301 , 100) ]
winnermoves = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
xarray=[]
oarray=[]

# all the images used in the prgm , make sure that they are all saved in same folder as the this program
Ximg = pygame.image.load('x.png')
Oimg = pygame.image.load('o.png')
Blankimg = pygame.image.load('blank.png')
Xwinimg = pygame.image.load('xwinner.png')
Owinimg = pygame.image.load('owinner.png')
Numimg = pygame.image.load('num.png')
Instimg = pygame.image.load('inst.png')
Titleimg = pygame.image.load('title.png')

# Resizing all the images 
ximg = pygame.transform.scale(Ximg, (100, 100))
oimg = pygame.transform.scale(Oimg, (100, 100))
blankimg = pygame.transform.scale(Blankimg, (100, 100))
xwinimg = pygame.transform.scale(Xwinimg , (100 , 100))
owinimg = pygame.transform.scale(Owinimg , (100 , 100))
numimg = pygame.transform.scale(Numimg , (300 ,300))
instimg = pygame.transform.scale(Instimg , (300 , 300))
titleimg = pygame.transform.scale(Titleimg , (200, 30))

# fucntion declaration
def draw_base():
  for i in range(100 , 301,100):
		for j in range(100 , 301,100):
			win.blit(blankimg, (j , i)) 

def check_win():
	for i in winnermoves:
		if i.intersection(xarray) == i:
			win.blit(xwinimg , (100 , 500))
		if i.intersection(oarray) == i:
			win.blit(owinimg , (100 , 500))

def if_key_pressed():
	if keys[pygame.K_1]:
		return True
	if keys[pygame.K_2]:
		return True
	if keys[pygame.K_3]:
		return True
	if keys[pygame.K_4]:
		return True
	if keys[pygame.K_5]:
		return True
	if keys[pygame.K_6]:
		return True
	if keys[pygame.K_7]:
		return True
	if keys[pygame.K_8]:
		return True
	if keys[pygame.K_9]:
		return True


def get_post():
	global pos
	keys = pygame.key.get_pressed()

	if keys[pygame.K_1]:
		pos = 1

	if keys[pygame.K_2]:
		pos = 2

	if keys[pygame.K_3]:
		pos = 3

	if keys[pygame.K_4]:
		pos = 4

	if keys[pygame.K_5]:
		pos = 5

	if keys[pygame.K_6]:
		pos = 6

	if keys[pygame.K_7]:
		pos = 7

	if keys[pygame.K_8]:
		pos =8

	if keys[pygame.K_9]:
		pos =9
def draw_moves():
	global pos 
	global movesxy
	for i in range (1,10):
		if pos == i:
			movesxy = movexy[i-1]
def draw_inst():
	win.blit(numimg, (500 ,100))
	win.blit(instimg, (500 ,410))
	win.blit(titleimg, (300 ,50))



# to draw the basic board (blue bg) and draw the appropriate instructions
draw_base()
draw_inst()

# main loop
run = True
while run:
	pygame.time.delay(50)
	
	

	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			run= False


	keys = pygame.key.get_pressed()

	if keys[pygame.K_a]:
		t=1
		
	if keys[pygame.K_d]:
		t=2
		


	if t == 1:	
		if if_key_pressed():
			get_post()
			draw_moves()
			xarray.append(pos)
			check_win()
			win.blit(ximg, movesxy)

	if t == 2:
		if if_key_pressed():
			get_post()
			draw_moves()
			oarray.append(pos)
			check_win()
			win.blit(oimg, movesxy)

	

	pygame.display.update()


pygame.quit()
