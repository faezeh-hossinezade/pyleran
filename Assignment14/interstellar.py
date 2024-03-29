import time
import random
import threading
import arcade
from bullet import Bullet
from spaceship import Spaceship
from enemy import Enemy
    
class Game(arcade.Window):
    ##parent
    def __init__(self):
        super().__init__(width=1000,height=800, title="Interestaller")
        # arcade.set_background_color(arcade.color.ALLOY_ORANGE)
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=Spaceship(self , "faeze")
        self.doshmanha=[]
        self.you=Enemy(self.width,self.height)
        self.doshmanha.append(self.you)
        self.life = 3
        self.time_space = 3
        self.life_background = arcade.load_texture(":resources:images/topdown_tanks/treeGreen_small.png")
        self.game_over = False
        self.score = 0
        self.sound = arcade.load_sound(":resources:sounds/hit3.wav")
        self.rise_speed=time.time()
        self.second=time.time()
        ## self=Game
        ## me= Spaceship
       
    def creator(self):
            self.new_doshman=Enemy(self.width,self.height)
            self.doshmanha.append(self.new_doshman) 
            
    def on_draw(self):
        arcade.start_render()
        
        if self.game_over:
            arcade.draw_text("Game Over :|", self.width // 2, self.height // 2,
                             arcade.color.RED, font_size=30, anchor_x="center")
        else:
            self.me.draw()
            arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
            arcade.draw_text(str(self.score), self.width - 40, 40, arcade.color.WHITE, font_size=30, anchor_x="center")



            for num in range(self.life):
                arcade.draw_lrwh_rectangle_textured((num * 50) + 10, 20, 50, 50, self.life_background)
                
            for doshman in self.doshmanha:
                doshman.draw()
                
            for bullet in self.me.bullet_list:
                bullet.draw()      
        arcade.finish_render()
        
    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x=0
        
    def on_key_press(self, symbol: int, modifiers: int):
        # print("pressed key")
        # print(symbol)
        if symbol==65363:
            self.me.change_x=-1
        elif symbol==65361:
            self.me.change_x=+1
        elif symbol==arcade.key.SPACE:
            self.me.fire()
            

    def on_update(self, delta_time: float):
        
        for doshman in self.doshmanha:
            if time.time()-self.rise_speed>=5:
                self.rise_speed=time.time()
                for doshman in self.doshmanha:
                    doshman.rise_speed()
            doshman.move()
            
        self.me.move()
        
        #move me and doshmanha
        for doshman in self.doshmanha:
            if arcade.check_for_collision(self.me,doshman):
                self.life -=1
                # print("life:",self.life)
                if self.life ==0:
                    self.game_over = True
            if doshman.center_y < 0:
                self.doshmanha.remove(doshman)
                   
        for doshman in self.doshmanha:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(bullet ,doshman):
                    self.doshmanha.remove(doshman)
                    self.me.bullet_list.remove(bullet)
                    arcade.play_sound(self.sound)
                    self.score += 1  
                    
        #collision
        
        # for doshman in self.doshmanha:
        #     if doshman.center_y>0:
        #         self.doshmanha.remove(doshman)
      
        # if random.randint(1,6)==6:
        #     self.new_doshman=Enemy(self.width,self.height)
        #     self.doshmanha.append(self.new_doshman)
            
        
        for bullet in self.me.bullet_list:
            bullet.move()
              
        if (random.randint(1, 100) == 100):
            timer = threading.Timer(3.0, self.creator)
            timer.start()
            # if (time.time()-start_time) %self.time_space==1:
            # self.second=time.time()
                # self.new_doshman=Enemy(self.width,self.height)
                # self.doshmanha.append(self.new_doshman)
               
        
        # # while time.time()-start_time == self.time_space:
        #     new_doshman = Enemy(self , self.bad_spaceships_start_speed)
        #     self.doshmanha.append(new_doshman)
                        


    ## hamishe ejra mishe
             
        
window=Game()
arcade.run()