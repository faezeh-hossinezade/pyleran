import arcade
from food import Apple, Avocado, Poo

# class Body(arcade.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.width = 32
#         self.height = 32
#         self.center_x = x
#         self.center_y = y

#     def draw(self, color):
#         arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, color)


class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width =32
        self.height=32
        self.center_x=game.width//2
        self.center_y=game.height//2
        self.color=arcade.color.SAP_GREEN
        self.color2 = arcade.color.BROWN
        self.change_x=0
        self.change_y=0
        self.speed=4
        self.score=0
        self.body=[]
        
        
    def change_direction(self, symbol):
        if symbol == arcade.key.UP:
            self.change_y = 1
            self.change_x = 0
        elif symbol == arcade.key.DOWN:
            self.change_y = -1
            self.change_x = 0
        elif symbol == arcade.key.LEFT:
            self.change_x = -1
            self.change_y = 0
        elif symbol == arcade.key.RIGHT:
            self.change_x = 1
            self.change_y = 0
        
            
    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)
        for count, part in enumerate(self.body):
            if count % 2 == 0:
                arcade.draw_rectangle_filled(
                    part["x"], part["y"], self.width, self.height, self.color2
                )
            else:
                arcade.draw_rectangle_filled(
                    part["x"], part["y"], self.width, self.height, self.color
                )
        # arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
     
        # for part in self.body:
        #     arcade.draw_rectangle_filled(part['x'],part['y'],self.width,self.height,self.color)
     
    def move(self):
        self.body.append({"x": self.center_x, "y": self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)

        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
           
           
    def eat(self,food,foods):
        if isinstance(food, Apple):
            self.score += 1
            foods[0] = Apple(self)
        elif isinstance(food, Avocado):
            self.score += 2
            foods[1] = Avocado(self)
        elif isinstance(food, Poo):
            self.score -= 1
            foods[2] = Poo(self)
        return foods
        # self.score +=1
        # # self.width +=10
        # print("score: ", self.score)
        # del game
        
    