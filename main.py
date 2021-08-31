import arcade
import arcade.gui

class GusWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Gus: The Game", resizable=True)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        open_message_box_button = arcade.gui.UIFlatButton(text="info", width=200)
        open_message_box_button.on_click = self.on_click_open
        self.v_box.add(open_message_box_button)

        self.manager.add(
                arcade.gui.UIAnchorWidget(
                        anchor_x="center_x",
                        anchor_y="center_y",
                        child=self.v_box
                    )
                )

    def on_click_open(self, event):
        message_box = arcade.gui.UIMessageBox(
                width=300,
                height=200,
                message_text="Welcome to GUS: THE GAME",
                buttons=["Yay Huzzah"]
                )

        self.manager.add(message_box)

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()

window = GusWindow()
arcade.run()
