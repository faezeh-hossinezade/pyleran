import arcade
from bullet import Bullet

class Spaceship(arcade.Sprite):
    ##children
    def __init__(self, game:int , name:str):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x=game.width/2
        self.change_x=0
        self.change_y=0
        self.center_y=80
        self.width=48
        self.height=48
        self.name=name
        self.speed=5
        self.game_width=game.width
        self.live=3
        self.bullet_list=[]


    def fire(self):
        new_bullet=Bullet(self)
        self.bullet_list.append(new_bullet) 
        
    def move(self,):
        if self.change_x==1:
            if self.center_x>0:
                self.center_x -=  self.speed
        elif self.change_x==-1:
            if self.center_x<self.game_width:
                 self.center_x += self.speed