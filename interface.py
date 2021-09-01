import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Gus: The Game"
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

        self.camera_sprites = None
        self.camera_gui = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        )
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_draw(self):
        # Make sure you call super().on_draw()
        # Start the camera
        self.player_list.draw()
        self.camera_gui.use()
        arcade.draw_lrtb_rectangle_filled(
            0, self.camera_gui.viewport_width, self.camera_gui.viewport_height / 3, 0, arcade.color.BLACK
        )

        if not self.interacted_text == "":
            arcade.draw_text(f"* {self.interacted_text}", 50, SCREEN_HEIGHT * (1 / 3) - 50, arcade.color.WHITE, DEFAULT_FONT_SIZE)

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera_sprites.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera_sprites.viewport_height / 2)

        if screen_center_x < 0:
           screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera_sprites.move_to(player_centered)

    def on_update(self, delta_time):
        # Make sure you call super().on_update()

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed and not self.player_sprite.bottom <= (self.camera_gui.viewport_height / 3) + 10:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED
            

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        self.player_list.update()

        self.center_camera_to_player()
    
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
