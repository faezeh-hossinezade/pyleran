import random
import arcade
# from .application import Window

class Spaceship(arcade.Sprite):
    ##children
    def __init__(self, game:int , name:str):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x=game.width/2
        self.center_y=80
        self.width=48
        self.height=48
        self.name=name
        self.speed=10

class Enemy(arcade.Sprite):
    ##children
    def __init__(self, w: int, h:int):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.center_x=random.randint(0,w)
        self.center_y=random.randint(0,h)
        self.angle=180
        self.speed=10
    
class Game(arcade.Window):
    ##parent
    def __init__(self):
        super().__init__(width=1000,height=800, title="Interestaller")
        # arcade.set_background_color(arcade.color.ALLOY_ORANGE)
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=Spaceship(self , "faeze")
        self.you=Enemy(self.width, self.height)
        ## self=Game
        ## me= Spaceship
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        self.you.draw()
        
    def on_key_press(self, symbol: int, modifiers: int):
        print("pressed key")
        print(symbol)
        if symbol==65363:
            self.me.center_x +=  self.me.speed
        elif symbol==65361:
            self.me.center_x -= self.me.speed
            
    def on_update(self, delta_time: float):
        self.you.center_y -=self.me.speed/4
            
        
window=Game()
arcade.run()