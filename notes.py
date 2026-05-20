import tkinter as tk
from tkinter import filedialog, messagebox


class EditorNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Notas")
        self.geometry("600x400")

        self.texto_area = tk.Text(self, undo=True)  # habilita desfazer/refazer
        self.texto_area.pack(expand=True, fill=tk.BOTH)

        self.criar_menu()

    def criar_menu(self):
        menubar = tk.Menu(self)

        # Menu Arquivo
        arquivomenu = tk.Menu(menubar, tearoff=0)
        arquivomenu.add_command(label="Abrir", command=self.abrir_arquivo)
        arquivomenu.add_command(label="Salvar", command=self.salvar_arquivo)
        arquivomenu.add_separator()
        arquivomenu.add_command(label="Sair", command=self.quit)
        menubar.add_cascade(label="Arquivo", menu=arquivomenu)

        # Menu Editar
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copiar", command=lambda: self.texto_area.event_generate("<<Copy>>"))
        editmenu.add_command(label="Colar", command=lambda: self.texto_area.event_generate("<<Paste>>"))
        editmenu.add_command(label="Recortar", command=lambda: self.texto_area.event_generate("<<Cut>>"))
        menubar.add_cascade(label="Editar", menu=editmenu)

        self.config(menu=menubar)

    def abrir_arquivo(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        if not filepath:
            return
        try:
            with open(filepath, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
            self.texto_area.delete(1.0, tk.END)
            self.texto_area.insert(tk.END, conteudo)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")

    def salvar_arquivo(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        if not filepath:
            return
        try:
            conteudo = self.texto_area.get(1.0, tk.END)
            with open(filepath, "w", encoding="utf-8") as arquivo:
                arquivo.write(conteudo)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar o arquivo: {e}")


if __name__ == "__main__":
    app = EditorNotas()
    app.mainloop()
