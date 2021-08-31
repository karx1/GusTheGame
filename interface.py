import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "HerrVille"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

# This class is meant to be subclassed
class Interface(arcade.Window):
    def __init__(self, width, height, title, background_color):
        super().__init__(width, height, title)
        arcade.set_background_color(background_color)
        self.interacted_text = ""

    def on_draw(self):
        # Make sure you call super().on_draw()
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, self.width, self.height / 3, 0, arcade.color.BLACK)

    def set_text(text):
        self.interacted_text = text


