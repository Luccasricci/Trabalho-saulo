import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

kivy.require('2.1.0')  

class ConversorApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)
        
       
        self.valor_dolar = TextInput(hint_text="Digite o valor em dólares", multiline=False, size_hint=(1, 0.1))
        self.resultado = Label(text="Valor em Reais: ", size_hint=(1, 0.1))
        
        
        btn_converter = Button(text="Converter", size_hint=(1, 0.2))
        btn_converter.bind(on_press=self.converter)

        
        layout.add_widget(self.valor_dolar)
        layout.add_widget(btn_converter)
        layout.add_widget(self.resultado)

        return layout
    
    def converter(self, instance):
        try:
            
            valor_dolar = float(self.valor_dolar.text)
            
            
            taxa_cambio = 6.06

            
            valor_real = valor_dolar * taxa_cambio

            
            self.resultado.text = f"Valor em Reais: R$ {valor_real:.2f}"
        
        except ValueError:
            
            self.resultado.text = "Por favor, insira um valor válido."


if __name__ == '__main__':
    ConversorApp().run()
