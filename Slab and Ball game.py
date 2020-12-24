import pygame
x=pygame.init()
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
Display=pygame.display.set_mode((1000,600))
pygame.display.set_caption("Slab and ball Game")
exitgame=False
gameover=False
slab_length=150
slab_width=20
ball_size=12
ball_speed_x=10
ball_speed_y=10
slab_position_x=0
slab_position_y=470
ball_position_x=1
ball_position_y=1
score=0
clock=pygame.time.Clock()
fps=20
Font=pygame.font.SysFont(None,70)
def score1(text,color,x1,y1):
    score2=Font.render(text,True,color)
    Display.blit(score2,[x1,y1])
while not exitgame:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exitgame=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                slab_position_x=slab_position_x+40
            if event.key==pygame.K_LEFT:
                slab_position_x=slab_position_x-40

    if abs(ball_position_x - slab_position_x) < 130 and abs(ball_position_y - slab_position_y) < 15:
        ball_speed_y=-ball_speed_y
    if ball_position_x>=1000:
        ball_speed_x=-ball_speed_x
    if ball_position_x<=0:
        ball_speed_x=-ball_speed_x
    if ball_position_y<=0:
        ball_speed_y=-ball_speed_y

    ball_position_x=ball_position_x+ball_speed_x
    ball_position_y=ball_position_y+ball_speed_y

    if abs(ball_position_x-slab_position_x)<130 and abs(ball_position_y-slab_position_y)<15:
        score=score+1
    Display.fill(white)
    score1(str('Score'+':')+str(score), green, 10, 10)

    if ball_position_y>=600:
        score1('Game Over',red,400,250)

    pygame.draw.rect(Display,black,[ball_position_x,ball_position_y,ball_size,ball_size])
    pygame.draw.rect(Display, green, [slab_position_x,slab_position_y,slab_length ,slab_width ])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()