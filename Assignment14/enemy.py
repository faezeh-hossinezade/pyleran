import random
import arcade
# from .application import Window
    

class Enemy(arcade.Sprite):
    ##children
    def __init__(self, w: int, h:int):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        # self.center_x=random.randint(0,w)
        # self.center_y=random.randint(0,h)
        # self.angle=180
        # self.speed=10
        self.width = 50
        self.height = 50
        self.change=-1
        self.center_x = random.randint(10, w)
        self.center_y = h 
        self.angle = 180
        self.speed = 5
        
    def move(self):
        self.center_y -=self.speed/5
        
    def rise_speed(self):
        self.speed+=1
        print(self.speed)