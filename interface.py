import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "HerrVille"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

MOVEMENT_SPEED = 5

# This class is meant to be subclassed
class Interface(arcade.Window):
    def __init__(self, width, height, title, background_color):
        super().__init__(width, height, title)
        arcade.set_background_color(background_color)
        self.interacted_text = ""
        self.player_list = None
        self.player_sprite = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        )
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        # Make sure you call super().on_draw()
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(
            0, self.width, self.height / 3, 0, arcade.color.BLACK
        )
        self.player_list.draw()

    def on_update(self, delta_time):
        # Make sure you call super().on_update()

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        self.player_list.update()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def set_text(self, text):
        self.interacted_text = text
