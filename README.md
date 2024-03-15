# CMD AUTONOMO
🎈INICIE E REINICIE SEU SCRIPT.PY.

<img src="FOTO.png" align="center" width="400"> <br>

## DESCRIÇÃO:
### GERAL:
O CMD AUTÔNOMO é uma aplicação desenvolvida em Python e interface gráfica utilizando a biblioteca Tkinter. Seu propósito principal é permitir que os usuários executem comandos e scripts Python de forma simples e intuitiva, diretamente de uma interface gráfica.

### RECURSOS:
1. **Campos de entrada "CAMINHO" e "ARQUIVO"**: Os usuários podem inserir o caminho do diretório onde o arquivo Python está localizado e o nome do arquivo a ser executado.
2. **Botões de controle**: Os botões "INICIAR", "REINICIAR", "PARAR" e "LIMPAR" oferecem funcionalidades para iniciar, reiniciar, parar a execução do script Python e limpar os campos de entrada, respectivamente.
3. **Status de execução**: Uma área de status exibe informações sobre o estado atual da execução do script, como "PARADO" ou "EM EXECUÇÃO!".
4. **Salvamento automático de configurações**: As configurações de "CAMINHO" e "ARQUIVO" são automaticamente salvas em um arquivo JSON chamado "CONFIG.json" no mesmo diretório do código. Isso permite que as configurações sejam carregadas automaticamente na próxima execução do aplicativo.
5. **Gerenciamento seguro de processos**: O aplicativo utiliza a biblioteca `psutil` para garantir o encerramento seguro do processo Python em execução.

### COMPORTAMENTO DOS CAMPOS E BOTÕES:
1. **Campos "CAMINHO" e "ARQUIVO"**:
   - Os campos estão inicialmente vazios e habilitados para entrada.
   - Quando ambos os campos estão preenchidos, o botão "INICIAR" é habilitado, permitindo ao usuário iniciar a execução do script.
   - O botão "LIMPAR" é habilitado quando ambos os campos estão preenchidos, permitindo ao usuário limpar os campos de entrada.
2. **Botões de controle**:
   - O botão "INICIAR" inicia a execução do script Python, desabilitando os campos de entrada e habilitando os botões "REINICIAR", "PARAR" e "LIMPAR".
   - O botão "REINICIAR" reinicia a execução do script Python, mantendo os campos de entrada inalterados.
   - O botão "PARAR" interrompe a execução do script Python em andamento, habilitando novamente os campos de entrada e desabilitando os botões "REINICIAR", "PARAR" e "LIMPAR".
   - O botão "LIMPAR" limpa os campos de entrada "CAMINHO" e "ARQUIVO", desabilitando-o novamente.

## PORQUE CRIEI ESSE APP?
- O aplicativo CMD AUTÔNOMO foi desenvolvido para simplificar a execução de bots Python diretamente pelo console, inspirado no conceito do "nodemon", eliminando a necessidade de reinicialização manual após modificações no código.
- Foi criado com o objetivo de proporcionar uma maneira fácil e conveniente de executar comandos e scripts Python através de uma interface gráfica amigável.
- Os usuários podem especificar o caminho do arquivo e o nome do script Python que desejam executar, com a opção de iniciar ou reiniciar a execução do script conforme necessário.

## OBSERVAÇÃO:
1. **Limitações da Ferramenta**:
   - O CMD AUTÔNOMO não substitui um ambiente de desenvolvimento integrado (IDE) ou outras ferramentas mais avançadas para desenvolvimento e execução de código.
   - Não oferece suporte para a execução de comandos complexos do sistema operacional diretamente pelo aplicativo.

2. **Requisitos de Instalação e Configuração**:
   - Os usuários devem ter o Python instalado e configurado corretamente em seus sistemas para que o aplicativo funcione corretamente.

3. **Suporte de Linguagem**:
   - Atualmente, o aplicativo suporta apenas a execução de scripts Python e não oferece suporte para outras linguagens de programação.

## COMO USAR?
### BAIXANDO O PROJETO:
**Passo 1:** Clone o repositório para o seu sistema local.

```bash
git clone https://github.com/VILHALVA/CMD-AUTONOMO.git
```

**Passo 2:** Navegue até o diretório do projeto.

```bash
cd CMD-AUTONOMO
```

**Passo 3:** Descompacte o arquivo ZIP (se você baixou manualmente):

```bash
unzip CMD-AUTONOMO.zip
```

### EXECUTANDO O EXECUTAVEL:
1. **Localize o Arquivo:** Após o download, localize o arquivo executável no seu sistema. Geralmente, os downloads são salvos na pasta "Downloads" do seu computador, mas você pode tê-lo salvo em outro local.

2. **Duplo Clique:** Para executar o arquivo, basta dar um duplo clique sobre ele. Isso abrirá o programa associado ao arquivo. Se o arquivo for um instalador, ele iniciará o processo de instalação. Se for um programa independente, ele será iniciado.

3. **Permissões de Administrador:** Dependendo do programa e das configurações do seu computador, você pode precisar de permissões de administrador para executá-lo. Se solicitado, clique com o botão direito do mouse no arquivo executável e selecione "Executar como administrador".

4. **Compatibilidade:** Certifique-se de que o executável seja compatível com a versão do seu sistema operacional. Se você estiver usando um sistema operacional Windows x64, o executável deve ser compilado para x64 para funcionar corretamente. Isso é importante porque o sistema operacional x64 não pode executar aplicativos compilados apenas para x86 (32 bits).

### EXECUTANDO O SCRIPT PYTHON:
- Para executar o código Python `(CODIGO.py)` em um PC zerado, ou seja, em um computador onde o Python não está instalado, você precisará seguir alguns passos adicionais para configurar o ambiente de execução. Aqui está um guia básico para isso:

1. **Baixe e Instale o Python:**
   - A primeira etapa é baixar o instalador do Python para o seu sistema operacional. Você pode encontrar o instalador oficial em [python.org](https://www.python.org/downloads/).
   - Se você estiver usando o Windows, certifique-se de baixar a versão adequada para o seu sistema operacional (32 bits ou 64 bits).
   - Siga as instruções do instalador para instalar o Python no seu PC.

2. **Configuração das Variáveis de Ambiente (opcional):**
   - No Windows, é uma boa prática adicionar o diretório de instalação do Python ao PATH do sistema. Isso permite que você execute comandos Python de qualquer diretório no prompt de comando.
   - Para fazer isso, após a instalação, procure "Variáveis de Ambiente" nas configurações do sistema, e adicione o caminho para o diretório de instalação do Python (normalmente algo como C:\PythonXX, onde XX é a versão do Python).

4. **Executando o Script:**
   - Abra um prompt de comando (no Windows, pressione `Win + R`, digite "cmd" e pressione Enter).
   - Navegue até o diretório onde o `nome-do-arquivo.py` está localizado usando o comando `cd` (por exemplo, `cd C:\Caminho\Para\O\nome-do-arquivo.py`).
   - Execute o script digitando `python nome-do-arquivo.py` e pressionando Enter.

5. **Instalando Dependências (se necessário):**
   - Se o seu script Python depende de pacotes ou módulos externos, você precisará instalá-los manualmente.
   - Use o comando `pip install nome-do-pacote` para instalar os pacotes necessários. Certifique-se de estar conectado à internet para que o pip possa baixar e instalar os pacotes.

Seguindo esses passos, você poderá executar o seu script Python em um PC zerado, mesmo sem ter o Python instalado anteriormente. Certifique-se de que todas as dependências do script estejam instaladas e que o Python esteja configurado corretamente no seu sistema. Se você não estiver familiarizado com esses passos, confira nosso [curso completo sobre o Python](https://github.com/VILHALVA/CURSO-DE-PYTHON) para obter orientações detalhadas.

### USANDO O APP:
- Para utilizar o CMD AUTÔNOMO, basta fornecer o caminho do arquivo e o nome do script Python que deseja executar. Após preencher esses campos, clique no botão "INICIAR" para iniciar a execução. Se você fizer alguma alteração no seu código, basta clicar em "REINICIAR" para atualizar seu projeto com as novas modificações:
* **LABEL `CAMINHO`:** É um campo de entrada onde você deve inserir o caminho do diretório onde está o script Python.
* **LABEL `ARQUIVO`:** É um campo de entrada onde você deve inserir o nome do arquivo Python.
* **BOTÃO `INICIAR:`** Quando clicado, inicia a execução do script Python especificado.
* **BOTÃO `REINICIAR:`** Quando clicado, reinicia a execução do script Python. Isso primeiro para o processo em execução e então inicia novamente.
* **BOTÃO `PARAR:`** Quando clicado, apenas interrompe a execução do script Python. 
* **BOTÃO `LIMPAR:`** Ao ser clicado, o botão "LIMPAR" tem a função de limpar todos os campos de entrada, fornecendo uma maneira rápida e conveniente de remover dados inseridos anteriormente. É importante observar que essa ação não afeta os dados salvos no arquivo "CONFIG.json", garantindo a preservação das configurações previamente inseridas.

## SAIBA MAIS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)
- [FAÇA OS NOSSOS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)


