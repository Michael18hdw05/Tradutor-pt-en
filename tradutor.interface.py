import tkinter as tk
from googletrans import Translator

class TradutorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tradutor EN-PT")
        self.root.geometry("400x300")
        self.root.configure(bg="white")

        self.label = tk.Label(root, text="Digite o texto:", bg="white", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.textbox = tk.Entry(root, width=40, font=("Helvetica", 12))
        self.textbox.pack(pady=10)

        self.button_traduzir = tk.Button(root, text="Iniciar", command=self.traduzir, bg="blue", fg="white", font=("Helvetica", 12))
        self.button_traduzir.pack(pady=10)

        self.button_alternar = tk.Button(root, text="Alternar Idioma", command=self.alternar_idioma, bg="green", fg="white", font=("Helvetica", 12))
        self.button_alternar.pack(pady=10)

        self.result_label = tk.Label(root, text="", bg="white", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        # Inicialmente, tradução de inglês para português
        self.idioma_origem = 'en'
        self.idioma_destino = 'pt'

    def traduzir(self):
        texto = self.textbox.get()
        translator = Translator()
        traducao = translator.translate(texto, src=self.idioma_origem, dest=self.idioma_destino).text
        self.result_label.config(text=f"Tradução: {traducao}")

    def alternar_idioma(self):
        # Trocar os idiomas de origem e destino
        self.idioma_origem, self.idioma_destino = self.idioma_destino, self.idioma_origem
        self.button_traduzir.invoke()  # Invocar a tradução automaticamente ao alternar o idioma

if __name__ == "__main__":
    root = tk.Tk()
    app = TradutorApp(root)
    root.mainloop()
