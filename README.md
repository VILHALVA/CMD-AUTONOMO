# CMD AUTONOMO
👨‍🏫CMD AUTÔNOMO É UM APP EM PYTHON COM INTERFACE GRÁFICA (CUSTOMTKINTER) PARA EXECUTAR SCRIPTS PYTHON DE FORMA SIMPLES, SEM USAR O TERMINAL.

<img src="FOTO.png" align="center" width="400"> <br>

## DESCRIÇÃO:
### GERAL:
**CMD AUTÔNOMO** é uma aplicação desenvolvida em Python com interface gráfica utilizando a biblioteca `customtkinter`. Seu objetivo é permitir a execução fácil e visual de scripts Python diretamente a partir de um ambiente gráfico, sem a necessidade de abrir o terminal.

### RECURSOS:
1. **Seleção de arquivos Python**: O usuário pode selecionar qualquer arquivo `.py` do sistema por meio de um botão que abre o explorador de arquivos.

2. **Botões de controle**:
   * **INICIAR**: Executa o script Python selecionado.
   * **PARAR**: Interrompe a execução do script em andamento.
   * **COPIAR**: Copia a saída gerada (stdout) para a área de transferência.
   * **LIMPAR**: Limpa o campo de seleção de arquivo e a área de status.

3. **Área de status**: Exibe a saída do script em tempo real, além de mensagens informativas, avisos e erros.

4. **Log de execução (opcional)**: O usuário pode ativar um modo de log, que salva toda a saída gerada em um arquivo `.txt` com data e hora.

5. **Gerenciamento seguro de processos**: Utiliza a biblioteca `psutil` para encerrar processos Python de forma segura, incluindo subprocessos filhos.

### COMPORTAMENTO DOS CAMPOS E BOTÕES:
1. **Campo de seleção de arquivo**:
   * Inicialmente desabilitado para edição direta e vazio.
   * Habilita os botões "INICIAR" e "LIMPAR" após um arquivo válido ser selecionado.

2. **Botões de controle**:
   * **INICIAR**:
     * Inicia a execução do script.
     * Desabilita o botão de seleção de arquivo.
     * Habilita os botões "PARAR" e "COPIAR".
   * **PARAR**:
     * Interrompe a execução do script em andamento.
     * Reabilita o botão de seleção de arquivo.
     * Habilita os botões "INICIAR", "COPIAR" e "LIMPAR".
   * **LIMPAR**:
     * Limpa o campo de seleção de arquivo e a área de status.
     * Desabilita todos os botões, exceto o de seleção de arquivo.
   * **COPIAR**:
     * Copia a saída da execução para a área de transferência.
     * Exibe uma mensagem de confirmação temporária ("TEXTO COPIADO!").

3. **Switch de LOG**:
   * Ao ativar, inicia um novo arquivo de log na pasta atual, nomeado com a data e hora.
   * Toda a saída posterior é salva automaticamente nesse arquivo.
   * Pode ser desativado a qualquer momento.

## PORQUE CRIEI ESSE APP?
- O aplicativo CMD AUTÔNOMO foi desenvolvido para simplificar a execução de bots Python diretamente pelo console, inspirado no conceito do "nodemon", eliminando a necessidade de reinicialização manual após modificações no código.
- Foi criado com o objetivo de proporcionar uma maneira fácil e conveniente de executar comandos e scripts Python através de uma interface gráfica amigável.

## OBSERVAÇÃO:
1. **Limitações da Ferramenta**:
   - O CMD AUTÔNOMO não substitui um ambiente de desenvolvimento integrado (IDE) ou outras ferramentas mais avançadas para desenvolvimento e execução de código.
   - Não oferece suporte para a execução de comandos complexos do sistema operacional diretamente pelo aplicativo.

2. **Requisitos de Instalação e Configuração**:
   - Os usuários devem ter o Python instalado e configurado corretamente em seus sistemas para que o aplicativo funcione corretamente.

3. **Suporte de Linguagem**:
   - Atualmente, o aplicativo suporta apenas a execução de scripts Python e não oferece suporte para outras linguagens de programação.

## COMO USAR O APLICATIVO?
1. **Instale as Dependências:**
Antes de iniciar o aplicativo, é necessário instalar as bibliotecas utilizadas no projeto. No terminal, execute:

```bash
pip install -r requirements.txt
```

> 💡 O arquivo `requirements.txt` está localizado dentro da pasta `./CODIGO`.

2. **Executando o Aplicativo:**
   Navegue até o diretório `./CODIGO` e execute o script com o comando:

   ```bash
   python CODIGO.py
   ```

3. **Interface e Funcionalidades:**
Após abrir o aplicativo, utilize os seguintes recursos:

* **Botão `SELECIONAR`:** Abre o explorador de arquivos para escolher um script Python (`.py`) a ser executado.
* **Botão `INICIAR`:** Inicia a execução do script selecionado. Esse botão só é ativado após um arquivo válido ser escolhido.
* **Botão `PARAR`:** Interrompe a execução atual do script Python de forma segura.
* **Botão `COPIAR`:** Copia toda a saída exibida na área de status para a área de transferência.
* **Botão `LIMPAR`:** Limpa o campo de seleção de arquivo e a saída exibida, retornando a aplicação ao estado inicial.
* **Switch `LOG OFF / LOG ON`:** Ao ativar, inicia o registro automático de toda a saída gerada durante a execução em um arquivo de log (`LOG_DATAHORA.txt`) criado na mesma pasta do aplicativo.

4. **Campo de Seleção de Arquivo:**
* Exibe o caminho do script Python escolhido.
* Este campo é somente leitura e atualizado automaticamente após a seleção via o botão `SELECIONAR`.
* A escolha de um arquivo válido ativa os botões "INICIAR" e "LIMPAR".

## SOBRE O EXECUTAVEL E O INSTALADOR:
### 1. EXECUTANDO O INSTALADOR:
   * O instalador está localizado no diretório `./APP` e está disponível apenas para sistemas **Windows x64**. Para realizar a instalação, basta **dar dois cliques no arquivo** e seguir as instruções exibidas na tela.

   * É importante explicar que ao executar o arquivo executável deste programa, é possível que o antivírus dispare um alerta de segurança. Isso ocorre porque o programa executa comandos do sistema operacional e pode abrir outros aplicativos ou acessar a rede.

   **Para lidar com isso, há 2 alternativas:**

   1. **Adicionar exceção ao antivírus:** Você pode optar por adicionar uma exceção ao antivírus para permitir que o programa execute comandos do sistema sem disparar alertas. Isso geralmente pode ser feito acessando as configurações do antivírus e adicionando o arquivo executável do programa à lista de exceções.

   2. **Executar apenas o `./CODIGO/CODIGO.py`:** Uma alternativa é optar por executar apenas o arquivo de código-fonte Python (`CODIGO.py`). Isso evita que o antivírus dispare alertas, já que você e o sistema podem inspecionar o código fonte diretamente.

### 2. GERANDO O EXECUTAVEL:
> **IMPORTANTE:** Antes de criar o instalador, é necessário gerar o arquivo `CMD AUTONOMO.exe`. Para isso, siga os passos abaixo:

   **1. Instalação do PyInstaller:**
   * Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   * No diretório `./CODIGO`, utilize o comando abaixo para gerar o executável:

   ```bash
   pyinstaller EXECUTAVEL.spec
   ```

   * O executável `CMD AUTONOMO.exe` será criado na pasta `./CODIGO/dist`.
   * Após a geração, você pode excluir a pasta `./CODIGO/build`.

### 3. GERANDO O INSTALADOR:
#### PASSO 1: BAIXAR E INSTALAR O INNO SETUP:
1. **Download**: Baixe o Inno Setup do site oficial: [Inno Setup](http://www.jrsoftware.org/isdl.php).
2. **Instalação**: Siga o assistente de instalação para instalar o Inno Setup no seu sistema.

#### PASSO 2: CRIAR O INSTALADOR:
> **IMPORTANTE:** Antes de criar o novo instalador, certifique-se de excluir o arquivo `./APP/CMD AUTONOMO.exe`.

1. **Editar o arquivo do instalador:**
   * No diretório `./CODIGO`, abra o arquivo `INSTALADOR.iss` e atualize o seguinte trecho:

   * Localize a diretiva `#define Diretorio` e substitua pelo caminho correto do diretório do projeto. Exemplo:

     ```ini
     #define Diretorio "C:\Users\HP\Downloads\GITHUB\REPOSITORIO\02-PROJETOS PUBLICOS\02-APLICATIVOS\CMD AUTONOMO\CODIGO"
     ```

2. **Gerar o instalador no Inno Setup:**
   * Abra o arquivo `./CODIGO/INSTALADOR.iss` com o **Inno Setup**.
   * Clique em **"Compile"** para gerar o instalador.

3. **Limpar arquivos temporários:**
   * Após a criação do instalador, você pode excluir o executável temporário: `./CODIGO/dist/CMD AUTONOMO.exe`.

4. **Instalando o Aplicativo:**
   * Se o `Aplicativo` não iniciar automaticamente a instalação, você pode executar manualmente o arquivo `./APP/CMD AUTONOMO.exe` clicando duas vezes sobre ele.
   * O assistente de instalação será iniciado e, por padrão, o aplicativo será instalado no seguinte caminho: `C:\Program Files\CMD AUTONOMO`.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens e tecnologias, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos e alguns subsídios:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE CUSTOMTKINTER](https://github.com/VILHALVA/CURSO-DE-CUSTOMTKINTER)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)
* [DOCUMENTAÇÃO OFICIAL DO PYINSTALLER](https://pyinstaller.org/en/stable/)
* [DOCUMENTAÇÃO OFICIAL DO INNO SETUP](http://www.jrsoftware.org/isinfo.php)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)


