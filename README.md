# CMD AUTONOMO
👨‍🏫CMD AUTÔNOMO É UM APP EM PYTHON COM INTERFACE GRÁFICA (CUSTOMTKINTER) PARA EXECUTAR SCRIPTS PYTHON DE FORMA SIMPLES, SEM USAR O TERMINAL.

<img src="FOTO.png" align="center" width="400"> <br>

## DESCRIÇÃO:
**CMD AUTÔNOMO** é uma aplicação desenvolvida em Python com interface gráfica utilizando a biblioteca `customtkinter`. Seu objetivo é permitir a execução fácil e visual de scripts Python diretamente a partir de um ambiente gráfico, sem a necessidade de abrir o terminal.

## RECURSOS:
1. **Seleção de arquivos Python**: O usuário pode selecionar qualquer arquivo `.py` do sistema por meio de um botão que abre o explorador de arquivos.

2. **Botões de controle**:
   * **INICIAR**: Executa o script Python selecionado.
   * **PARAR**: Interrompe a execução do script em andamento.
   * **COPIAR**: Copia a saída gerada (stdout) para a área de transferência.
   * **LIMPAR**: Limpa o campo de seleção de arquivo e a área de status, reseta o switch de **LOG** para OFF e desabilitado, e retorna a aplicação ao estado inicial.

3. **Área de status**: Exibe a saída do script em tempo real, além de mensagens informativas, avisos e erros.

4. **Log de execução (opcional)**: O usuário pode ativar o modo de log, que salva automaticamente toda a saída gerada em um arquivo `CMD AUTONOMO_DATA_HORA.txt` dentro do subdiretório **LOG** da pasta do arquivo selecionado. O sistema também cria ou atualiza o `.gitignore` para incluir a pasta `LOG`, evitando que os arquivos de log sejam versionados.

5. **Gerenciamento seguro de processos**: Utiliza a biblioteca `psutil` para encerrar processos Python de forma segura, incluindo subprocessos filhos.

## COMPORTAMENTO DOS CAMPOS E BOTÕES:
1. **Campo de seleção de arquivo**:
   * Inicialmente desabilitado para edição direta e vazio.
   * Habilita os botões **INICIAR** e **LIMPAR**, além do **switch de LOG**, após a seleção de um arquivo válido.

2. **Botões de controle**:
   * **INICIAR**:
     * Inicia a execução do script.
     * Desabilita o botão de seleção de arquivo.
     * Habilita os botões **PARAR** e **COPIAR**.
   * **PARAR**:
     * Interrompe a execução do script em andamento.
     * Reabilita o botão de seleção de arquivo.
     * Habilita os botões **INICIAR**, **COPIAR** e **LIMPAR**.
   * **LIMPAR**:
     * Limpa o campo de seleção de arquivo e a área de status.
     * Reseta o switch de **LOG** para OFF e desabilitado.
     * Desabilita todos os botões, exceto o de seleção de arquivo.
   * **COPIAR**:
     * Copia a saída da execução para a área de transferência.
     * Exibe uma mensagem temporária de confirmação ("TEXTO COPIADO!").

3. **Switch de LOG**:
   * Inicialmente desabilitado até que um arquivo seja selecionado.
   * Ao ser ativado, cria um novo arquivo de log dentro do subdiretório **LOG** da pasta do arquivo selecionado, usando data e hora no nome para organizar os registros por sessão.
   * Se o `.gitignore` não existir, é criado; caso exista mas não contenha `LOG`, a linha é adicionada ao final.
   * Toda a saída posterior é salva automaticamente nesse arquivo.
   * Pode ser desativado a qualquer momento, voltando para a posição OFF e mantendo consistência visual.

## PORQUE CRIEI ESSE APP?
- O aplicativo `CMD AUTÔNOMO` foi desenvolvido para simplificar a execução de bots Python diretamente pelo console, inspirado no conceito do "nodemon", eliminando a necessidade de reinicialização manual após modificações no código.

## OBSERVAÇÃO:
1. **Limitações da Ferramenta:**
   - O CMD AUTÔNOMO não substitui um ambiente de desenvolvimento integrado (IDE) ou outras ferramentas mais avançadas para desenvolvimento e execução de código.
   - Não oferece suporte para a execução de comandos complexos do sistema operacional diretamente pelo aplicativo.

2. **Requisitos de Instalação e Configuração:**
   - É necessário que o **Python esteja instalado e corretamente configurado** no sistema para que o aplicativo funcione como esperado.
   - Além disso, **todas as dependências do script que será executado devem estar previamente instaladas**. Isso inclui bibliotecas e pacotes utilizados no código Python que você pretende rodar por meio da aplicação.

3. **Suporte de Linguagem:**
   - O aplicativo suporta apenas a execução de scripts Python e não oferece suporte para outras linguagens de programação.

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
   * Clique em **SELECIONAR** → escolha um script `.py`.
   * Clique em **INICIAR** → execute o script escolhido (habilitado só após selecionar arquivo válido).
   * Clique em **PARAR** → interrompa a execução em andamento.
   * Clique em **COPIAR** → copie toda a saída exibida para a área de transferência (mensagem de confirmação aparece).
   * Clique em **LIMPAR** → apague seleção, saída, desative LOG e volte ao estado inicial.
   * Ative o **switch LOG** → grave saída em `LOG/CMD_AUTONOMO_DATA_HORA.txt`, crie/atualize `.gitignore` e evite versionamento.
   * Desative o **switch LOG** → pare o registro mantendo consistência visual.

4. **Campo de Seleção de Arquivo:**
   * Exibe o caminho do script escolhido (somente leitura).
   * Atualiza automaticamente após **SELECIONAR**.
   * Ativa os botões **INICIAR** e **LIMPAR** ao escolher um arquivo válido.

## SOBRE O EXECUTAVEL E O INSTALADOR:
### 1. EXECUTANDO O INSTALADOR:
   - O instalador está localizado no diretório `./APP` e está disponível apenas para sistemas **Windows x64**. Para realizar a instalação, basta **dar dois cliques no arquivo** e seguir as instruções exibidas na tela.

   - Ao executar o **instalador** deste aplicativo, **é possível que seu antivírus exiba um alerta de segurança**. Isso **não significa que o aplicativo é malicioso**, mas sim que o antivírus está reagindo ao comportamento comum de programas que executam comandos do sistema, como é o caso deste projeto.

   **Para lidar com isso, há 2 alternativas:**

   1. **Adicionar uma exceção no antivírus:**
      - Inclua o arquivo `instalador` do aplicativo na **lista de exclusões (exceções)** do seu antivírus. Esse procedimento pode variar conforme o antivírus utilizado, mas normalmente está disponível nas configurações de segurança, na seção de "Exclusões", "Ameaças permitidas" ou "Pastas confiáveis". Isso permitirá que o aplicativo rode normalmente sem gerar bloqueios ou alertas.

   2. **Executar diretamente o código-fonte (`CODIGO.py`):**
      - Caso prefira uma abordagem mais transparente, você pode simplesmente **executar o script Python original** (`CODIGO.py`) utilizando um ambiente Python instalado na sua máquina. Essa abordagem permite verificar o código antes da execução, e **reduz drasticamente a chance de alertas**, pois o antivírus entende que você está executando um script legítimo de forma explícita.

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
   * Após a criação do instalador, você pode excluir o executável temporário `./CODIGO/dist/CMD AUTONOMO.exe`.

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

## CREDITOS E MAIS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)
- [CLIQUE AQUI PARA VER O HISTÓRICO DE ATUALIZAÇÕES](./UPDATES.md)


