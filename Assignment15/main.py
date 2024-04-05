import threading
import time
import random
import arcade
from food import Apple, Avocado, Poo,Fruit
from snake import Snake


    
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500,title="super snake🐍")
        arcade.set_background_color(arcade.color.KHAKI)
        self.apple=Apple(self)
        self.avocado=Avocado(self)
        self.poo=Poo(self)
        self.foods=[self.poo,self.avocado,self.apple]
        #self==game
        self.snake=Snake(self)
        self.game_over = False
    
    
    def on_draw(self):
        arcade.start_render()
        if self.game_over:
            arcade.draw_text("Game Over :|", self.width // 2, self.height // 2, arcade.color.RED, font_size=30, anchor_x="center")
        else:
            arcade.draw_text(str(self.snake.score), self.width - 40, 40, arcade.color.WHITE, font_size=30,anchor_x="center")
            self.snake.draw()
            self.apple.draw()
            self.avocado.draw()
            self.poo.draw()

                
                
        arcade.finish_render()
        
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.UP:
            self.snake.change_x=0
            self.snake.change_y=1
            
        elif symbol==arcade.key.DOWN:
            self.snake.change_x=0
            self.snake.change_y=-1
            
        elif symbol==arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0
            
        elif symbol==arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0
        
    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.apple):
            del self.apple
            self.snake.score += 1
            self.apple = Apple(self)
        elif arcade.check_for_collision(self.snake, self.avocado):
            del self.avocado
            self.snake.score += 2
            self.avocado = Avocado(self)
        elif arcade.check_for_collision(self.snake, self.poo):
            del self.poo
            self.snake.score -= 1
            self.poo = Poo(self)
            
        if ((self.snake.score < 0) or (self.snake.center_x > self.width) or
                (self.snake.center_x < 0) or (self.snake.center_y > self.height) or
                (self.snake.center_y < 0)):
            self.game_over = True
                     
        for food in self.foods:
            if arcade.check_for_collision(food, self.snake):
                self.foods = self.snake.eat(food, self.foods)
    
if __name__ == '__main__':
    game=Game()
    arcade.run()