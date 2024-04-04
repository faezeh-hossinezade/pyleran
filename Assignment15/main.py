import random
import arcade
from food import Apple, Avocado, Poo
from snake import Snake


    
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500,title="super snake🐍")
        arcade.set_background_color(arcade.color.KHAKI)
        self.foods=[]
        self.foods = [Apple(self), Avocado(self), Poo(self)]
        # self.food_one=Apple(self)
        # self.food_two=Avocado(self)
        # self.food_three=Poo(self)
        #self==game
        self.snake=Snake(self)
        self.game_over = False
    
    
    def on_draw(self):
        arcade.start_render()
        # self.food_one.draw()
        # self.food_two.draw()
        # self.food_three.draw()
        if self.game_over:
            arcade.draw_text("Game Over :|", self.width // 2, self.height // 2, arcade.color.RED, font_size=30, anchor_x="center")
        else:
            arcade.draw_text(str(self.snake.score), self.width - 40, 40, arcade.color.WHITE, font_size=30,anchor_x="center")
            self.snake.draw()
            for food in self.foods:
                food.draw()
                
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
        if ((self.snake.score < 0) or (self.snake.center_x > self.width) or
                (self.snake.center_x < 0) or (self.snake.center_y > self.height) or
                (self.snake.center_y < 0)):
            self.game_over = True
        # for num, body in enumerate(self.snake.body):
        #     if arcade.check_for_collision(self.snake, body):
        #         if len(self.snake.body) - 20 < num:
        #             continue
        #         self.game_over = True
                
        for food in self.foods:
            if arcade.check_for_collision(food, self.snake):
                self.foods = self.snake.eat(food, self.foods)

        
        # if arcade.check_for_collision(self.snake, self.food_one):
        #     self.snake.eat(self.food_one)
        #     self.food_one=Apple(self)
        # elif arcade.check_for_collision(self.snake , self.food_two):
        #     self.snake.eat(self.food_two)
        #     self.food_two=Avocado(self)
        # elif arcade.check_for_collision(self.snake , self.food_three):
        #     self.snake.eat(self.food_three)
        #     self.food_three=Poo(self)
    

    
if __name__ == '__main__':
    game=Game()
    arcade.run()