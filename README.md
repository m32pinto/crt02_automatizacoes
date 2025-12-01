# crt02_automatizacoes
Utilidades para o atendimento

# Introdução (Atualizações)

1.0 - 30/11/2025

• Vamos iniciar mencionando as utilidades:

Apresentações: Apresentação de técnico que faz.

Textos rápidos personalizáveis: Saudações, textos guias.

Envio de imagens: Envio de 3 folders (imagens)

As utilidades acima são acionadas por combinações de teclas, nesse primeiro momento sempre a primeira tecla contará com **shift** seguida de outra tecla do alfabeto.



# Desenvolvimento (Explicação do código)

 Teremos dois arquivos duas*telas*teste.py e duas*telas*listener.py.

  duas*telas*teste é um dicionário e contém as variáveis: textos para colar, a mesma contém "chaves" que são os títulos (strings) do texto que deseja-se enviar (solicitacao*de*registro*profissional, solicitacao*de*interrupcao*de*registro...), as chaves podem ter títulos sequênciais (texto*1.1, texto_1.2...) indicando uma conjunto de texto para serem enviados.
 Contém as **funções** : **colar*texto **que recebe o argumento** chave*do*texto ** imprimiremos qual a chave foi ativada e tentamos clicar na barra de texto, esperamos 0.1 segundos, copiaremos o texto final que será pegar (get) do textos*para*colar a chave do texto (busca do dicionário), se não encontrar ** texto*final **imprima a** chave*do*texto **não foi encontrada, após clicamos na posição da barra de texto espere 0.1 segundos cole o** texto_final **(naquela posição), imprima que a** chave*do*texto foi** colada com sucesso, se ocorrer alguns erro inesperado (e) imprima ele.
 Aqui temos um teste com **if** para colar uma chave somente se executamos duas*telas*teste.py, contamos 3 segundos, no ponto onde clicamos se houver opção de digitar texto, será colado o conteúdo de solicitacao_de_registro_profissional, contamos 2 segundos e será colado o conteúdo de **saudacao,** 

Usaremos as bibliotecas: pyautogui, pyperclip, pynput


