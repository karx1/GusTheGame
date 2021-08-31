import arcade
import random
import string
from interface import Interface, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from sprite import Sprite

class HerrVille(Interface):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, f"{SCREEN_TITLE} - HerrVille", arcade.color.GRAY)

        self.npc_list = None
    
    def setup(self):
        super().setup()

        self.npc_list = arcade.SpriteList()

        for i in range(10):
            npc = Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png")

            npc.center_x = random.randrange(SCREEN_WIDTH)
            
            while True:
                npc.center_y = random.randrange(int(SCREEN_HEIGHT * (1 / 3)), SCREEN_HEIGHT)
                
                if not npc.bottom <= SCREEN_HEIGHT * (1 / 3):
                    break
            

            npc.interacted_text = "".join(random.choice(string.ascii_letters) for x in range(10))


            self.npc_list.append(npc)

    def on_draw(self):
        super().on_draw()

        self.npc_list.draw()

def main():
    window = HerrVille()
    window.setup()
    arcade.run()

