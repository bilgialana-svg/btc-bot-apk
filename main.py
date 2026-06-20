from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.core.window import Window


class TestApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#1a1a2e')

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        title = Label(
            text='BTC/TRY Bot',
            font_size=32,
            bold=True,
            color=get_color_from_hex('#00b894')
        )
        layout.add_widget(title)

        info = Label(
            text='Test APK Calisiyor!\nAPK basariyla derlendi.',
            font_size=18,
            color=get_color_from_hex('#dfe6e9')
        )
        layout.add_widget(info)

        btn = Button(
            text='TIKLA',
            font_size=20,
            background_color=get_color_from_hex('#0984e3'),
            size_hint_y=0.3
        )
        btn.bind(on_press=self.on_click)
        layout.add_widget(btn)

        self.click_count = 0
        self.click_label = Label(
            text='Tiklama: 0',
            font_size=16,
            color=get_color_from_hex('#fdcb6e')
        )
        layout.add_widget(self.click_label)

        return layout

    def on_click(self, instance):
        self.click_count += 1
        self.click_label.text = 'Tiklama: ' + str(self.click_count)


if __name__ == '__main__':
    TestApp().run()
