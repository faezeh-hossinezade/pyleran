import random
import arcade

from rocket import Rocket
from ball import Ball

class Game(arcade.Window):
    def __init__(self):
       super().__init__(width=800,height=500,title="Pong 2024 🏓") 
       arcade.set_background_color(arcade.color.BAZAAR)
       self.me=Rocket(40,self.height/2,arcade.color.RED,"Faeze")
       self.you=Rocket(self.width-40,self.height/2,arcade.color.GREEN,"Mojtaba")
       self.ball=Ball(self)
       self.lists=[self.you,self.me]
    
    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_rectangle_outline(self.width/2,self.height/2,self.width-30,self.height-30,arcade.color.WHITE,border_width=10)
        arcade.draw_line(self.width/2,30,self.width/2,self.height-30, color=arcade.color.WHITE,line_width=10)
        arcade.draw_text(self.me.score, 30, 30 ,arcade.color.WHITE, 20)
        arcade.draw_text(self.you.score, self.width - 40, 30 ,arcade.color.WHITE, 20)
        self.me.draw()
        self.you.draw()
        self.ball.draw()
        arcade.finish_render()
    
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # self.me.center_x=x
        if self.me.height<y<self.height-self.me.height:
            self.me.center_y=y
            
    def on_update(self, delta_time: float):
        self.ball.move()
        # if  self.you.height<self.you.center_y-self.you.speed  or \
        #     self.you.center_y+self.you.speed  <self.height-self.you.center_y:
        self.you.move(self, self.ball)
            
        if (self.ball.center_y<30) or (self.ball.center_y>self.height-30):
            self.ball.change_y *=-1
            
        if arcade.check_for_collision(self.ball,self.me) or \
            arcade.check_for_collision(self.ball,self.you):
            self.ball.change_x *=-1
            # self.me.score +=1
            
        
        if self.ball.center_x<0:
            self.you +=1
            del self.ball
            self.ball=Ball(self)
            
        if self.ball.center_x>self.width:
            self.me.score +=1
            del self.ball
            self.ball=Ball(self)
            
        
    

game=Game()
arcade.run()