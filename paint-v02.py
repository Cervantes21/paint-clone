import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Dibujador(Widget):
    Window.clearcolor = (1,1,1,1)
 
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,0,0)           
            touch.ud['dibujo'] = Line(points=touch.pos)
    def on_touch_move(self, touch):
        touch.ud['dibujo'].points += touch.pos
    def borrar(self, *args):
        self.canvas.clear()

class MiApp(App):
    def build(self):
        dibujador = Dibujador()
        borrar_btn = Button(text='Borrar')
        borrar_btn.bind(on_release=dibujador.borrar)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(dibujador)
        layout.add_widget(borrar_btn)
        return layout

if __name__ == "__main__":
    MiApp().run()
