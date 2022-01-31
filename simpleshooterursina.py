from ursina import *; from ursina.prefabs.first_person_controller import *
app=Ursina()
player=FirstPersonController()
player.speed=20
Sky()
plane=Entity(model='plane',color=color.green,collider='box',scale=(100,1,100),position=(5, 1, 2))
lives=3
def e():
    global Robot,lives
    lives=lives-1
    if lives==0:
        Robot.position=random.randint(1,40),5,random.randint(1,40)
        lives=3
Robot = Entity(model='a',color=color.orange,collider='box',scale=(0.1,0.1,0.1),rotate_y=90,position=(random.randint(1,10),5,5),on_click=e)
def input(key):
    if key=='left mouse down':
        Audio('ball_hit.wav')
        dust = Entity(model=Circle(), parent=camera.ui, scale=0.03, color=color.red, position=(0,0))
        dust.animate_scale(0.001, duration=.1, curve=curve.linear)
        dust.fade_out(duration=0.1)
app.run()