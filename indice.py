# =====================================================#
## Início Bibliotecas ##
# =====================================================#

import pyautogui
import pyperclip

# =====================================================#
## Fim Bibliotecas ##
# =====================================================#

# =====================================================#
## Início da Variável de dicionário ##
# =====================================================#
TEXTOS_PARA_COLAR = {

    'chave_1': """conteúdo""",

    # Adicione quantos textos quiser
    # 'minha_chave_nova': "Meu novo texto rápido."
}

# =====================================================#
## Fim da Variável de dicionário ##
# =====================================================#

# =====================================================#
## Início função colar texto ##
# =====================================================#

# 2. A função agora recebe um argumento: a 'chave_do_texto'
def colar_texto(chave_do_texto):
    print(f"\nFunção 'colar_texto' chamada com a chave: {chave_do_texto}")
    pyautogui.FAILSAFE = True

    # 3. Busca o texto no dicionário
    texto_final = TEXTOS_PARA_COLAR.get(chave_do_texto)

    # 4. Se não encontrar o texto, avisa e para
    if not texto_final:
        print(f"Erro: Chave '{chave_do_texto}' não encontrada no dicionário de textos.")
        return

    try:
        pyperclip.copy(texto_final)

        pyautogui.hotkey('ctrl', 'v')

        print(f"Texto '{chave_do_texto}' colado com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro no PyAutoGUI: {e}")

# =====================================================#
## Fim função colar_texto ##
# =====================================================#

