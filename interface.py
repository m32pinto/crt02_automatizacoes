# interface.py
# =====================================================#
## Interface com botões para substituir atalhos de teclado ##
# =====================================================#
#1 importações

import tkinter as tk
from indice import colar_texto


# =====================================================#
## 2 Funções de callback para os botões ##
# =====================================================#

def callback_button1():
    colar_texto('chave_1')

# =====================================================#
## Criação da interface gráfica ##
# =====================================================#

#3
def criar_interface():
    janela = tk.Tk()
    janela.title("Repyta")
    janela.geometry("500x800")
    janela.resizable(False, False)

    # Frame principal com padding
    frame_principal = tk.Frame(janela, padx=10, pady=10)
    frame_principal.pack(fill=tk.BOTH, expand=True)

    # Configurar pesos do grid do frame_principal para expansão correta
    frame_principal.columnconfigure(1, weight=1)  # Coluna do canvas expande
    frame_principal.rowconfigure(1, weight=1)     # Linha do conteúdo expande

    # Título
    titulo = tk.Label(frame_principal, text="Botões de Atalho", font=("Arial", 14, "bold"))
    titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # ===== SCROLL (código compacto e funcional) =====
    canvas = tk.Canvas(frame_principal, height=620)
    scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    frame_botoes = tk.Frame(canvas)
    #canvas.create_window((0, 0), window=frame_botoes, anchor="nw")

    # Configurar colunas do frame_botoes para centralização:
    # Coluna 0 e 3 = espaçadores expansíveis (peso 1)
    # Colunas 1 e 2 = colunas reais dos botões (peso 0 = largura fixa)
    frame_botoes.columnconfigure(0, weight=1)  # Espaçador esquerdo
    frame_botoes.columnconfigure(1, weight=0)  # Coluna botões esquerda
    frame_botoes.columnconfigure(2, weight=0)  # Coluna botões direita
    frame_botoes.columnconfigure(3, weight=1)  # Espaçador direito

    canvas_window = canvas.create_window((0, 0), window=frame_botoes, anchor="nw")

    # Função de scroll UNIFICADA (funciona em Linux/Windows)
    def _on_mousewheel(event):
        if event.num == 4 or event.delta > 0:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            canvas.yview_scroll(1, "units")
        return "break"

    # Bind no canvas e frame para capturar scroll
    canvas.bind_all("<Button-4>", _on_mousewheel)
    canvas.bind_all("<Button-5>", _on_mousewheel)
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Atualiza região de scroll quando conteúdo muda
    frame_botoes.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Forçar largura do frame_botoes = largura do canvas para preencher horizontalmente
    canvas.bind("<Configure>", lambda e: frame_botoes.configure(width=e.width))

    # POSICIONAMENTO: scrollbar à esquerda (coluna 0), canvas à direita (coluna 1)
    scrollbar.grid(row=1, column=0, sticky="ns")   # Scrollbar no canto esquerdo
    canvas.grid(row=1, column=1, sticky="nsew")    # Canvas expande no espaço restante
    # ===== FIM SCROLL =====

    #4 Criação dos botões em grade 2 colunas
    botoes = [
        ("nome_do_botao_1", callback_button1),
    ]

    #5 estrutura de repetição

    for i, (texto, comando) in enumerate(botoes):
        linha = (i // 2) + 1
        coluna = i % 2
        btn = tk.Button(
            frame_botoes,
            text=texto,
            command=comando,
            width=25,
            height=3,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 9),
            relief=tk.RAISED,
            cursor="hand2",
            wraplength = 180

        )
        btn.grid(row=linha, column=coluna, padx=5, pady=5, sticky="ew")

    #6 Botão de fechar
    btn_fechar = tk.Button(
        frame_principal,
        text="Fechar",
        command=janela.destroy,
        width=20,
        height=2,
        bg="#f44336",
        fg="white",
        font=("Arial", 10, "bold")
    )
    btn_fechar.grid(row=len(botoes) // 2 + 2, column=0, columnspan=2, pady=15)

    #7 Mensagem de instrução
    instrucao = tk.Label(
        frame_principal,
        text="Clique onde deseja colar o texto\nantes de usar os botões",
        font=("Arial", 8, "italic"),
        fg="#666"
    )
    instrucao.grid(row=len(botoes) // 2 + 3, column=0, columnspan=2, pady=(10, 0))

    #8
    janela.mainloop()


    #9
if __name__ == "__main__":
    criar_interface()