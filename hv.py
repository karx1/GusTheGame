import arcade
from interface import Interface, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

class HerrVille(Interface):
    def on_draw(self):
        super().on_draw()

def main():
    HerrVille(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, arcade.color.GRAY)
    arcade.run()

if __name__ == "__main__":
    main()
