import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.gridlayout import GridLayout

class Dibujador(Widget):
    Window.clearcolor = (1,1,1,1)
    color = [0,0,0,1]
    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color)
            touch.ud['dibujo'] = Line(points=(touch.x, touch.y))
            
    def on_touch_move(self, touch):
        touch.ud['dibujo'].points += [touch.x, touch.y]

    def clear_canvas(self):
        self.canvas.clear()

    def update_color(self, colorpicker, color):
        self.color = color

class MiApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        dibujador = Dibujador()
        clear_button = Button(text="Borrar", on_press=dibujador.clear_canvas)
        color_picker = ColorPicker()
        color_picker.bind(color=dibujador.update_color)
        layout.add_widget(dibujador)
        layout.add_widget(clear_button)
        layout.add_widget(color_picker)

        return layout

if __name__ == "__main__":
    MiApp().run()


