import random
import arcade


class Fruit(arcade.Sprite):
    def __init__(self,image,game):
        super().__init__(image)
        self.width =48
        self.height =48
        self.center_x=random.randint(10,game.width-10)
        self.center_y=random.randint(10,game.height-10)
        self.change_x=0
        self.change_y =0
        

class Apple(Fruit):
    def __init__(self,game):
        super().__init__("input/apple_icon.png",game)
        
        
class Avocado(Fruit):
    def __init__(self,game):
        super().__init__("input/avocados_icon.png",game)
        

class Poo(Fruit):
    def __init__(self,game):
        super().__init__("input/poo_icon.png",game)