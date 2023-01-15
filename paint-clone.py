import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.core.window import Window
from kivy.uix.button import Button

class Dibujador(Widget):
    Window.clearcolor = (1,1,1,1)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,0,0)           
            touch.ud['dibujo'] = Line(points=touch.pos)
    def on_touch_move(self, touch):
        touch.ud['dibujo'].points += touch.pos
    def limpiar_pantalla(self, obj):
        self.canvas.clear()


class MiApp(App):
    def build(self):
        parent = Widget()
        dibujador = Dibujador()
        btn = Button(text='Borrar', size_hint=(None, None), size=(100, 50))
        btn.bind(on_press=dibujador.limpiar_pantalla)
        parent.add_widget(dibujador)
        parent.add_widget(btn)
        return parent
if __name__ == "__main__":
    MiApp().run()
