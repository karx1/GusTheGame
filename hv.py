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
    
    def on_update(self, delta_time):
        super().on_update(delta_time)

        self.npc_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.npc_list)

        if len(hit_list) == 0:
            self.set_text("")
        else:
            for npc in hit_list:
                self.set_text(npc.interacted_text)

def main():
    window = HerrVille()
    window.setup()
    arcade.run()

