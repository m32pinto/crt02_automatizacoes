# =====================================================#
## Início Bibliotecas ##
# =====================================================#

from pynput import keyboard
from duas_telas_teste import colar_texto # 1. Importamos nossa nova função
from duas_telas_teste import colar_texto_sequencia

import tkinter as tk
from tkinter import messagebox

# =====================================================#
## Fim Bibliotecas ##
# =====================================================#

# =====================================================#
## Início variável de mapeamento de atalhos ##
# =====================================================#

# --- 2. O Mapeamento Principal ---
# Aqui definimos: "Qual atalho chama qual chave de texto?"
# As chaves ('solicitacao_de_registro_profissional', 'solicitacao_de_interrupcao_de_registro') devem ser IDÊNTICAS
# às chaves que você definiu no dicionário TEXTOS_PARA_COLAR.
MAPEAMENTO_ATALHOS = {
    '<shift>+q': 'solicitacao_de_registro_profissional',
    '<shift>+w': 'solicitacao_de_interrupcao_de_registro',
    '<shift>+e': 'solicitacao_de_reativacao_profissional_inativos',
    '<shift>+r': 'procotolo_de_outros',
    '<shift>+t': 'protocolo_de_reativacao_de_registro',
    '<shift>+y': 'protocolo_de_reativacao_definitivo_ou_renovacao_de_provisorio',
    '<shift>+u': 'emissao_de_certidao_de_quitacao_de_pf',
    '<shift>+i': 'emissao_de_carteira_digital',
    '<shift>+o': 'solicitacao_de_carteira_fisica',
    '<shift>+p': 'inclusao_de_foto',
    '<shift>+a': 'manual_instrutivo_para_geracao_de_anuidade',
    '<shift>+s': 'protocolo_de_inclusao_de_especializacao_tecnica',
    '<shift>+d': 'protocolo_inclusao_de_titulo',
    '<shift>+f': 'protocolo_de_alteracao_de_endereco',
    '<shift>+g': 'saudacao',
    '<shift>+h': 'verificacao',
    '<shift>+j': 'documentacao_comprobatoria',
    '<shift>+k': 'aguardando_retorno',
    '<shift>+l': 'algo_mais',

# ==============================Início=========================================#
## colar texto sequência (Novo atendimento fazendo alusão ao técnico que faz) ##
# =============================================================================#

    '<shift>+ç': 'texto_1.1,texto_1.2,texto_1.3,texto_1.4,texto_1.5'

## Um string apenas com chaves separadas

# ==============================Fim============================================#

    # Adicione seus atalhos aqui. Pode usar <alt>, <shift>...
    # Exemplo: '<ctrl>+<alt>+s': 'minha_chave_nova'
}

# =====================================================#
## Fim variável de mapeamento de atalhos ##
# =====================================================#

# =====================================================#
## Início Função criar_callbacks ##
# =====================================================#

# --- 3. Função "Fábrica" de Callbacks ---
# Isso é necessário para garantir que o atalho certo
# chame a chave certa (evita um bug comum de 'closures' em loops)
def criar_callback(chave_do_texto):
    # 'lambda' cria uma pequena função que chama 'colar_texto'
    # com a chave que passamos.
    return lambda: colar_texto(chave_do_texto)

# =====================================================#
## Fim Função criar_callbacks ##
# =====================================================#


# =====================================================#
## Início Função callback par lidar com multiplas chaves (criar_callback_sequencia) ##
# =====================================================#

def criar_callback_sequencia(chaves_str):
    """
    Cria um callback que chama colar_textos_sequencia com as chaves fornecidas.
    """
    chaves = chaves_str.split(',') # Divide a ‘string’ por vírgula
    return lambda: colar_texto_sequencia(chaves)

# =====================================================#
## Fim   Função callback par lidar com multiplas chaves (criar_callback_sequencia) ##
# =====================================================#

# =====================================================#
## Início hotkeys_para_ouvir ##
# =====================================================#

# --- 4. Montagem do Dicionário para o Pynput ---
# O GlobalHotKeys espera um dicionário no formato:
# { 'atalho_string': funcao_callback }
hotkeys_para_ouvir = {}
for atalho, chave in MAPEAMENTO_ATALHOS.items():
    if '.' in chave: # Se a chave contém vírgula, é uma sequência
        hotkeys_para_ouvir[atalho] = criar_callback_sequencia(chave)
    else:
        hotkeys_para_ouvir[atalho] = criar_callback(chave)

# --- 5. Configuração e Início do Listener ---
print("Ouvinte de múltiplos atalhos iniciado.")
print("Atalhos configurados:")
for atalho, chave in MAPEAMENTO_ATALHOS.items():
    print(f"  {atalho}  ->  Texto: '{chave}'")
print("!!! ESTE TERMINAL DEVE PERMANECER ABERTO !!!")

with keyboard.GlobalHotKeys(hotkeys_para_ouvir) as listener:
    listener.join()

# =====================================================#
## Fim hotkeys_para_ouvir ##
# =====================================================#



# =====================================================#
## Conceitos ##

#Função callbacks
##Ao usar callbacks, é possível definir comportamentos específicos para diferentes eventos.
##Por exemplo, aciona-se um callback quando o usuário clica em um botão,
##insere dados em um campo de entrada ou seleciona uma opção em um menu suspenso.