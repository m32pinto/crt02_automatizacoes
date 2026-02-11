# =====================================================#
## Interface Gráfica com Tkinter + Listener de Atalhos ##
# =====================================================#

import tkinter as tk
from tkinter import font
import threading
from pynput import keyboard
import pyautogui
import pyperclip
import sys
import time

# =====================================================#
## Dicionário de Textos (reutilizado do duas_telas_teste.py) ##
# =====================================================#
TEXTOS_PARA_COLAR = {
    'solicitacao_de_registro_profissional': """SOLICITAÇÃO DE REGISTRO PROFISSIONAL

    Entre no site: https://corporativo.sinceti.net.br/app/view/sight/externo.php?form=CadastrarProfissional     e preencha o formulário, sendo obrigatório o preenchimento nos espaços que conterem um asterisco vermelho. Segue abaixo os documentos necessários para solicitação de Registro Profissional:

    1. Diploma ou certificado do ensino técnico;

    2. Histórico do ensino técnico com indicação das cargas horárias cursadas;

    3. RG (frente e verso)

    4. CPF (frente e verso)

    5. Comprovantes de endereço atualizado ou declaração de residência;

    6. Foto 3x4, de preferência de fundo branco;

    7. Título de eleitor (frente e verso)

    8. Prova de quitação com a Justiça Eleitoral (Certidão de quitação eleitoral)

    9. Prova de quitação com o Serviço Militar (sexo masculino).

    Obs.: anexar os documentos digitalizados em PDF ou JPG individualmente.
    Colocar um e-mail e no final gerar o boleto de análise de registo.

    Após 24h do pagamento, ao constar no sistema, a sua solicitação é enviada para ser analisada.""",

    'solicitacao_de_interrupcao_de_registro': """SOLICITAÇÃO DE INTERRUPÇÃO DE REGISTRO.

    Para solicitar a INTERRUPÇÃO DE REGISTRO proceda da seguinte forma:

    Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    Selecione a opção PROTOCOLOS, em seguida CADASTRAR;

    Em GRUPO DE ASSUNTO escolha a opção PROFISSIONAL;

    Em ASSUNTO, vá até a opção SOLICITAÇÃO DE INTERRUPÇÃO DE REGISTRO PROFISSIONAL;

    Em DESCRIÇÃO DO PROTOCOLO, descreva os motivos pelos quais deseja solicitar a interrupção do registro;

    Em DOCUMENTOS ANEXOS, clique em NOVO ARQUIVO, em seguida anexe um documento comprobatório que informe que você não possui atividade laborativa compatível com a área técnica (declaração de não ocupação de cargo ou atividade na área de sua formação técnica profissional, constando nome completo e CPF, assinada pelo requerente e datada).

    Por fim, clique em CADASTRAR.""",

    'solicitacao_de_reativacao_profissional_inativos': """SOLICITAÇÃO DE REATIVAÇÃO PROFISSIONAL (INATIVOS)

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Selecione a opção PROTOCOLOS, em seguida CADASTRAR;

    3. Em GRUPO DE ASSUNTO escolha a opção PROFISSIONAL;

    4. Em ASSUNTO, vá até a opção REATIVAÇÃO DE REGISTRO - PROFISSIONAL INATIVO ;

    5. Em DESCRIÇÃO DO PROTOCOLO, descreva os motivos pelos quais deseja solicitar a reativação de registro.

    6. selecione a opção  “Declaro, sob as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. Se precisar anexar mais de um documento, clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "responder de responder despacho".

    Aconselhamos para fins de atualização de dados cadastrais, encaminhar os seguintes documentos no protocolo:

    1. RG;
    2. CPF;
    3. Comprovantes de endereço atualizado ou declaração de residência;
    4. Foto 3x4, de preferência de fundo branco;
    5. Título de eleitor;
    6. Prova de quitação com a Justiça Eleitoral (comprovante de votação ou certidão de quitação eleitoral).""",

    'procotolo_de_outros': """PROTOCOLO DE OUTROS

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: opção de outros;

    5. DESCRIÇÃO DO PROTOCOLO: “descreva o motivo do protocolo”.

    6. Clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "CADASTRAR".

    7. Anexe uma documentação comprobatória.""",

    'protocolo_de_reativacao_de_registro': """PROTOCOLO DE REATIVAÇÃO DE REGISTRO.

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: Reativação de Registro–Profissional;

    5. Em DESCRIÇÃO DO PROTOCOLO, descreva os motivos pelos quais deseja solicitar a reativação de registro;

    6. Selecione a opção “Declaro, sobre as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. CADASTRAR.

    OBS.: Realize o pagamento do seu boleto referente a taxa de análise de Registro no valor de R$63,83 (Lembrando que o prazo para compensação de boleto é de 24 a 72 horas).""",

    'protocolo_de_reativacao_definitivo_ou_renovacao_de_provisorio': """PROTOCOLO DE REGISTRO DEFINITIVO OU RENOVAÇÃO DE PROVISÓRIO.

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: Solicitação de Registro Definitivo caso *haja diploma e histórico* ou renovação de registro provisório caso *haja declaração de conclusão de curso e histórico*

    5. Em DESCRIÇÃO DO PROTOCOLO, descreva os motivos pelos quais deseja solicitar o Registro Definitivo ou Renovação do Provisório.

    6. Selecione a opção  “Declaro, sobre as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. Clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "CADASTRAR".

    8. Anexe a documentação solicitada.

    9. Cadastrar.""",

    'emissao_de_certidao_de_quitacao_de_pf': """EMISSÃO DE CERTIDÃO DE QUITAÇÃO DE PESSOA FÍSICA:

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Selecione a opção CERTIDÕES em seguida SOLICITAR CERTIDÃO;

    3. Tipo de Certidão: Certidão de quitação de pessoa física;

    4. Confirme as suas informações;

    5. Preencha o código de segurança;

    6. Cadastrar...

    7. Selecione novamente a opção (Certidão de quitação de pessoa física) e ficará disponível a opção IMPRIMIR.""",

    'emissao_de_carteira_digital': """EMISSÃO DE CARTEIRA DIGITAL:

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Selecione a opção IMPRESSÃO DE CARTEIRA.""",

    'solicitacao_de_carteira_fisica': """SOLICITAÇÃO DE CARTEIRA FÍSICA:
    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: opção de solicitação de carteira profissional;

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a emissão da carteira profissional junto ao crt02”.""",

    'inclusao_de_foto': """INCLUSÃO DE FOTO

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR;

    3. GRUPO DE ASSUNTO: profissional;

    4. ASSUNTO: selecione a opção de inclusão de foto;

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a inclusão de foto para emissão de carteira”;

    6. Anexe dois documentos (FOTO 3X4 e RG ou CNH).""",

    'manual_instrutivo_para_geracao_de_anuidade': """*Manual Instrutivo para Geração de Anuidade*
    Este manual tem como objetivo orientar o usuário sobre como acessar e utilizar o sistema para gerar anuidades.

    *Passo 1: Acesso ao Sistema*

    1. Acesse o sistema utilizando seu CPF e senha pessoal, através do link: https://servicos.sinceti.net.br/     

    *Passo 2: Navegação para a Geração de Anuidade*

    2. No canto superior da tela, localize e clique na aba ou menu denominado "Financeiro".

    *Passo 3: Seleção da Opção Anuidade*

    3. Dentro do menu Financeiro, encontre e selecione a opção específica para "Anuidade".

    *Passo 4: Escolha dos Anos em Aberto*

    4. Na página de Anuidade, selecione os anos referentes às anuidades em aberto.

    *Passo 5: Aceitação do Termo de Compromisso*

    5. Antes de prosseguir, é necessário concordar com o termo de compromisso relacionado à geração das anuidades.

    *Passo 6: Realização de Simulações e Seleção de Parcelas*

    6. Realize simulações conforme necessário e escolha o padrão de parcelas que melhor atenda às suas necessidades. ( informamos que caso haja juros e multa ou taxa em sua simulação, haverá acréscimos de acordo com a quantidade de parcelas escolhidas.)

    *Passo 7: Geração da Anuidade*

    7. Após escolher o padrão de parcelas desejado, clique na opção "Gerar Anuidade" para finalizar o processo.

    *Observações Finais:*

    - Certifique-se de revisar todas as informações inseridas antes de confirmar a geração da anuidade.
    - A data de vencimento dos boletos ficarão definidas para o último dia do mês de cada parcela.
    - Em caso de dúvidas ou problemas técnicos, entre em contato com o suporte técnico responsável.
    Este manual visa facilitar o processo de geração de anuidades no sistema, proporcionando uma experiência clara e eficiente para o usuário.   
    """,

    'protocolo_de_inclusao_de_especializacao_tecnica': """
    PROTOCOLO DE INCLUSÃO DE ESPECIALIZAÇÃO TÉCNICA

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR

    3. GRUPO DE ASSUNTO: profissional

    4. ASSUNTO: selecione a opção de “inclusão de especialização técnica”

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a inclusão de minha especialização técnica ao registro profissional”. 

    6. Selecione a opção “Declaro, sobre as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. Clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "CADASTRAR".""",

    'protocolo_inclusao_de_titulo': """PROTOCOLO INCLUSÃO DE TÍTULO:

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR

    3. GRUPO DE ASSUNTO: profissional

    4. ASSUNTO: selecione a opção de inclusão de Título

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a inclusão de título em meu registro profissional”

    6. Selecione a opção  “Declaro, sobre as penas da Lei, serem verdadeiras as informações aqui declaradas”

    7. clique em "NOVO ARQUIVO" que encontra-se localizado acima do campo "CADASTRAR".

    8. Anexe os documentos solicitados (Diploma e Histórico)

    OBS.: O profissional deve estar ADIMPLENTE para essa solicitação…""",

    'protocolo_de_alteracao_de_endereco': """PROTOCOLO DE ALTERAÇÃO DE ENDEREÇO:

    1. Acesse seu ambiente de serviços no SINCETI; https://servicos.sinceti.net.br/    

    2. Na parte superior da sua tela vai a protocolos > CADASTRAR

    3. GRUPO DE ASSUNTO: profissional

    4. ASSUNTO: selecione a opção de “Alteração de Endereço”

    5. DESCRIÇÃO DO PROTOCOLO: “Solicito a alteração do meu endereço”

    6. Anexe a documentação solicitada (COMPROVANTE DE RESIDÊNCIA).

    OBS.: O profissional deve estar ADIMPLENTE para essa solicitação.""",

    'saudacao': """Olá me chamo Marcos do setor de atendimento do CRT 02, como posso ajudar ?""",

    'verificacao': """Vou verificar, um momento.""",

    'documentacao_comprobatoria': """Por gentileza, envie um comprovante da sua urgência, pode ser PDF, conversa, email, edital... Fico no seu aguardo. 

    Essas informações são de forma oficial pela empresa ou plataforma de contratação se possível conter também a data limite para priorização.
    """,

    'aguardando_retorno': """Fico no aguardo do seu retorno.""",

    'algo_mais': """Ajudo em algo mais ?""",

    'texto_1.1': """Olá me chamo Marcos do setor de atendimento do CRT 02👨🏽‍💻""",
    'texto_1.2': """📣Antes de começar o atendimento gostaria de apresentar a nova ferramenta para os técnicos ganharem o mercados e serem vistos de forma privilegiadas *O técnico que faz* ✅ .""",
    'texto_1.3': """📣Segue o link para acessar a plataforma: https://tecnicoquefaz.crt02.gov.br/     e fazer seu cadastro. 🔗""",
    'texto_1.4': """📣Se preferir enviamos vídeos, guias para orientar o seu cadastro.🎥""",
    'texto_1.5': """📣O técnico que faz conecta profissionais registrados com a sociedade em geral: o técnico pode incluir seu currículo e oferecer serviços; a empresa pode encontrar candidatos habilitados para preencher suas vagas; e a sociedade pode encontrar opções de serviços com qualidade e responsabilidade técnica. Cadastre-se gratuitamente agora mesmo!🌐"""
}


# =====================================================#
## Funções de Automação (reutilizadas) ##
# =====================================================#

def colar_texto(chave_do_texto):
    print(f"\nFunção 'colar_texto' chamada com a chave: {chave_do_texto}")
    pyautogui.FAILSAFE = True

    texto_final = TEXTOS_PARA_COLAR.get(chave_do_texto)
    if not texto_final:
        print(f"Erro: Chave '{chave_do_texto}' não encontrada no dicionário de textos.")
        return

    try:
        pyautogui.doubleClick(2281, 1063)
        pyautogui.sleep(0.1)
        pyperclip.copy(texto_final)
        pyautogui.hotkey('ctrl', 'v')
        print(f"Texto '{chave_do_texto}' colado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro no PyAutoGUI: {e}")


def enviar_imagens():
    print("\n Iniciando o envio de imagens (Benefícios e sobre técnico que faz)")
    pyautogui.FAILSAFE = True

    try:
        pyautogui.click(x=371, y=1028)
        pyautogui.sleep(2)
        pyautogui.click(x=37, y=465)
        pyautogui.sleep(2)
        pyautogui.click(x=1793, y=382)
        pyautogui.sleep(2)
        pyautogui.typewrite("documentos")
        pyautogui.sleep(2)
        pyautogui.press('down')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.click(x=1793, y=382)
        pyautogui.sleep(2)
        pyautogui.typewrite('Trabalho')
        pyautogui.sleep(2)
        pyautogui.press('down')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.click(x=1793, y=382)
        pyautogui.sleep(2)
        pyautogui.typewrite('crt_02')
        pyautogui.sleep(2)
        pyautogui.press('down')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.click(x=1793, y=382)
        pyautogui.sleep(2)
        pyautogui.typewrite('folders_tecnico_que_faz')
        pyautogui.sleep(2)
        pyautogui.press('down')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.press('up')
        pyautogui.sleep(2)
        with pyautogui.hold('shift'):
            pyautogui.press('down')
            pyautogui.sleep(0.5)
            pyautogui.press('down')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(2)
        pyautogui.click(x=598, y=783)
        pyautogui.sleep(2)
        print("Envio de imagens concluído com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar as imagens: {e}")


def colar_texto_sequencia(chaves):
    print(f"\nFunção 'colar_textos_sequencia' chamada com chaves: {chaves}")
    pyautogui.FAILSAFE = True

    if not chaves:
        print("Erro: lista chaves vazia")
        return

    for chave in chaves:
        print(f"Colando texto: {chave}")
        pyautogui.press('backspace')
        colar_texto(chave)
        pyautogui.sleep(2)
        pyautogui.press('enter')

    print("\nTextos colados com sucesso")
    enviar_imagens()


# =====================================================#
## Mapeamento de Atalhos ##
# =====================================================#
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
    '<shift>+ç': 'texto_1.1,texto_1.2,texto_1.3,texto_1.4,texto_1.5'
}


# =====================================================#
## Callbacks com Gerenciamento de Janela (CORRIGIDO) ##
# =====================================================#
def criar_callback(chave_do_texto):
    def callback():
        # Minimiza imediatamente
        root.iconify()

        # Executa a automação em thread separada para não bloquear a UI
        def run_automation():
            try:
                colar_texto(chave_do_texto)
            finally:
                # Restaura a janela após conclusão (usando after para garantir execução na thread principal)
                root.after(100, lambda: (
                    root.deiconify(),
                    root.lift(),
                    root.attributes('-topmost', True),
                    root.focus_force(),
                    root.after(300, lambda: root.attributes('-topmost', False))
                ))

        threading.Thread(target=run_automation, daemon=True).start()

    return callback


def criar_callback_sequencia(chaves_str):
    chaves = chaves_str.split(',')

    def callback():
        # Minimiza imediatamente
        root.iconify()

        # Executa a automação em thread separada
        def run_automation():
            try:
                colar_texto_sequencia(chaves)
            finally:
                # Restaura a janela após conclusão
                root.after(100, lambda: (
                    root.deiconify(),
                    root.lift(),
                    root.attributes('-topmost', True),
                    root.focus_force(),
                    root.after(300, lambda: root.attributes('-topmost', False))
                ))

        threading.Thread(target=run_automation, daemon=True).start()

    return callback


# =====================================================#
## Configuração da Interface Tkinter ##
# =====================================================#
root = tk.Tk()
root.title("Atalhos CRT-02")
root.geometry("400x920")
root.resizable(False, False)
root.attributes('-topmost', True)
root.configure(bg='#1e1e1e')

# Estilos
title_font = font.Font(family="Segoe UI", size=12, weight="bold")
shortcut_font = font.Font(family="Segoe UI", size=10)
header_bg = '#2d2d2d'
shortcut_bg = '#252526'
text_fg = '#d4d4d4'
highlight_bg = '#3e3e42'

# Cabeçalho
header = tk.Label(
    root,
    text="📋 ATALHOS CRT-02",
    font=title_font,
    bg=header_bg,
    fg='#569cd6',
    pady=8
)
header.pack(fill=tk.X)

# Container para os atalhos
frame = tk.Frame(root, bg='#1e1e1e', padx=10, pady=5)
frame.pack(fill=tk.BOTH, expand=True)

# Canvas com scrollbar
canvas = tk.Canvas(frame, bg='#1e1e1e', highlightthickness=0)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg='#1e1e1e')

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Mapeamento amigável para nomes dos atalhos
NOMES_AMIGAVEIS = {
    'solicitacao_de_registro_profissional': 'Solicitação de Registro',
    'solicitacao_de_interrupcao_de_registro': 'Interrupção de Registro',
    'solicitacao_de_reativacao_profissional_inativos': 'Reativação (Inativos)',
    'procotolo_de_outros': 'Protocolo de Outros',
    'protocolo_de_reativacao_de_registro': 'Reativação de Registro',
    'protocolo_de_reativacao_definitivo_ou_renovacao_de_provisorio': 'Registro Definitivo/Provisório',
    'emissao_de_certidao_de_quitacao_de_pf': 'Certidão de Quitação PF',
    'emissao_de_carteira_digital': 'Carteira Digital',
    'solicitacao_de_carteira_fisica': 'Carteira Física',
    'inclusao_de_foto': 'Inclusão de Foto',
    'manual_instrutivo_para_geracao_de_anuidade': 'Manual de Anuidade',
    'protocolo_de_inclusao_de_especializacao_tecnica': 'Inclusão de Especialização',
    'protocolo_inclusao_de_titulo': 'Inclusão de Título',
    'protocolo_de_alteracao_de_endereco': 'Alteração de Endereço',
    'saudacao': 'Saudação',
    'verificacao': 'Verificação',
    'documentacao_comprobatoria': 'Documentação Comprobatória',
    'aguardando_retorno': 'Aguardando Retorno',
    'algo_mais': 'Ajuda em algo mais?',
    'texto_1.1': 'Novo Atendimento (Parte 1)',
    'texto_1.2': 'Novo Atendimento (Parte 2)',
    'texto_1.3': 'Novo Atendimento (Parte 3)',
    'texto_1.4': 'Novo Atendimento (Parte 4)',
    'texto_1.5': 'Novo Atendimento (Parte 5)'
}

# Adiciona os atalhos na interface COM CLIQUE FUNCIONAL
for atalho, chave in MAPEAMENTO_ATALHOS.items():
    # Determina o callback correto
    if ',' in chave:
        callback = criar_callback_sequencia(chave)
        chaves_separadas = chave.split(',')
        nome_exibicao = " + ".join([NOMES_AMIGAVEIS.get(c.strip(), c.strip()) for c in chaves_separadas[:2]] + (
            ['...'] if len(chaves_separadas) > 2 else []))
    else:
        callback = criar_callback(chave)
        nome_exibicao = NOMES_AMIGAVEIS.get(chave, chave.replace('_', ' ').title())

    # Formata o atalho para exibição amigável
    atalho_exibicao = atalho.replace('<shift>+', 'Shift + ').replace('<ctrl>+', 'Ctrl + ').upper()

    # Container para cada item
    item_frame = tk.Frame(scrollable_frame, bg=shortcut_bg, pady=3, padx=8, relief=tk.RAISED, borderwidth=1)
    item_frame.pack(fill=tk.X, pady=2)

    # Nome do atalho (CLICÁVEL)
    nome_label = tk.Label(
        item_frame,
        text=nome_exibicao,
        font=shortcut_font,
        bg=shortcut_bg,
        fg=text_fg,
        anchor="w",
        wraplength=280,
        cursor="hand2"  # Cursor de mão para indicar clicável
    )
    nome_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

    # Tecla de atalho (CLICÁVEL)
    tecla_label = tk.Label(
        item_frame,
        text=atalho_exibicao,
        font=shortcut_font,
        bg=highlight_bg,
        fg='#4ec9b0',
        padx=8,
        pady=2,
        borderwidth=1,
        relief=tk.RAISED,
        cursor="hand2"  # Cursor de mão para indicar clicável
    )
    tecla_label.pack(side=tk.RIGHT)

    # Torna TODO o item clicável
    item_frame.bind("<Button-1>", lambda e, cb=callback: cb())
    nome_label.bind("<Button-1>", lambda e, cb=callback: cb())
    tecla_label.bind("<Button-1>", lambda e, cb=callback: cb())

# Rodapé informativo
footer = tk.Label(
    root,
    text="Clique no item ou use as teclas para acionar\nJanela minimiza automaticamente durante a automação",
    font=("Segoe UI", 8),
    bg='#2d2d2d',
    fg='#999999',
    pady=6
)
footer.pack(fill=tk.X)

# =====================================================#
## Configuração do Listener de Teclado ##
# =====================================================#
hotkeys_para_ouvir = {}
for atalho, chave in MAPEAMENTO_ATALHOS.items():
    if ',' in chave:
        hotkeys_para_ouvir[atalho] = criar_callback_sequencia(chave)
    else:
        hotkeys_para_ouvir[atalho] = criar_callback(chave)


# Inicia o listener em thread separada
def iniciar_listener():
    with keyboard.GlobalHotKeys(hotkeys_para_ouvir) as listener:
        print("✅ Listener de atalhos iniciado com sucesso")
        print("✅ Interface gráfica carregada - Pronto para uso")
        print("\nAtalhos configurados:")
        for atalho, chave in MAPEAMENTO_ATALHOS.items():
            nome = NOMES_AMIGAVEIS.get(chave.split(',')[0] if ',' in chave else chave, chave[:30])
            print(f"  {atalho:20} → {nome}")
        print("\n➡️  Pressione os atalhos ou CLIQUE nos itens para usar")
        listener.join()


listener_thread = threading.Thread(target=iniciar_listener, daemon=True)
listener_thread.start()


# Configura fechamento seguro
def on_closing():
    print("\n🛑 Encerrando aplicação...")
    root.destroy()
    sys.exit(0)


root.protocol("WM_DELETE_WINDOW", on_closing)

# Mensagem de inicialização
print("=" * 60)
print("🚀 SISTEMA DE ATALHOS CRT-02 INICIADO")
print("=" * 60)
print("Interface gráfica carregada na tela")
print("Aguardando interação do usuário...")

# Inicia o loop principal
root.mainloop()