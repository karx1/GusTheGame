import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "HerrVille"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class HerrVilleWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, self.width, self.height / 3, 0, arcade.color.BLACK)



def main():
    HerrVilleWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
