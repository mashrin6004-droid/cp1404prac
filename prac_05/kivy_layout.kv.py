# kivy_layout.kv
# Layout definition for KivyDemo app

BoxLayout:
    orientation: "vertical"
    padding: 10
    spacing: 10

    Label:
        text: app.status_text
        font_size: 48
        size_hint_y: 0.2
        halign: "center"
        valign: "middle"
        text_size: self.size

    BoxLayout:
        orientation: "horizontal"
        size_hint_y: 0.2
        spacing: 10

        Button:
            text: "Up"
            font_size: 32
            on_press: app.handle_press(1)

        Button:
            text: "Down"
            font_size: 32
            on_press: app.handle_press(-1)

    BoxLayout:
        id: names_box
        orientation: "vertical"
        spacing: 10



