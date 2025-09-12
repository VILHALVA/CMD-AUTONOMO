# [ATUALIZAÇÕES:](./UPDATES.md#vers%C3%A3o-10---26022024)
## VERSÃO 1.4 - 12/09/2025:
* ✅Agora o log é criado dentro de um **subdiretório `LOG`** na **mesma pasta do arquivo selecionado pelo usuário**, em vez de ser no diretório onde o aplicativo está rodando.
* ✅**Botão de LOG desabilitado até a seleção do arquivo:**
  * O switch inicia **desabilitado**.
  * Só é habilitado após o usuário selecionar um arquivo usando o botão **SELECIONAR**.
  * Ao clicar **LIMPAR**, o switch é novamente desabilitado e retorna para a posição OFF, evitando inconsistências.
* ✅**Comportamento do botão LIMPAR:** Além de limpar o campo de arquivo e a textbox, o switch `LOG`:
  * É **desligado (lado esquerdo / OFF)**.
  * É **desabilitado** até que um novo arquivo seja selecionado.
  * Mantém a cor consistente (`progress_color="transparent"`).
* ✅**Atualização do `.gitignore` ao ativar o log pela primeira vez:**
  * Se **não existir** um `.gitignore` na pasta do arquivo selecionado, ele é criado contendo a linha `LOG`.
  * Se **existir**, mas não contiver a linha `LOG`, a linha é adicionada **ao final do arquivo**.
* ✅Agora foi criado um **instalador** para o aplicativo (antes havia apenas o executável).
---

## VERSÃO 1.3 - 13/06/2025:
* ✅Interface agora desenvolvida com `CustomTkinter`, substituindo o uso do `Tkinter`.
* ✅O aplicativo inicia automaticamente em tela maximizada.
* ✅Título principal destacado na parte superior.
* ✅Campo dedicado para seleção de arquivos `.py`, com botão "SELECIONAR", permitindo escolher o script de forma prática e rápida.
* ✅Textbox dedicado à exibição dos eventos e saídas do terminal.
* ✅Área de status integrada no Textbox, permitindo acompanhar a execução.
* ✅Os botões organizados lado a lado: "INICIAR", "PARAR", "COPIAR"(substituindo o antigo botão "REINICIAR") e "LIMPAR".
* ✅O uso do arquivo `CONFIG.json` foi completamente removido.
* ✅A seção do footer foi removida.
* ✅O instalador foi retirado, permanecendo apenas o executável.
* ✅**Novo botão Switch de log:** Alterna de "LOG OFF" para "LOG ON", criando automaticamente o arquivo "LOG/CMD AUTONOMO_{DATA}_{HORA}.txt", com todas as saídas exibidas na CTkTextbox.
---

## VERSÃO 1.2 - 29/06/2024:
* ✅Seguindo o [tutorial](https://youtu.be/5U-nBAfbSek?si=XlaCHY8Rw8gWXzX_),  utilizei o programa [Inno Setup Copiler](https://jrsoftware.org/isdl.php#stable) para criar o instalador para o app.
---

## VERSÃO 1.1 - 15/03/2024:
* ✅Agora, os campos "CAMINHO" e "ARQUIVO" são automaticamente salvos no arquivo "CONFIG.json" ao fechar o aplicativo, garantindo que as configurações sejam preservadas para sessões futuras.
* ✅Introduzir o botão "LIMPAR", permitindo aos usuários limpar rapidamente os campos de entrada, facilitando a remoção de dados anteriores sem afetar as configurações salvas no "CONFIG.json".
* ✅**COMPORTAMENTO DOS CAMPOS E BOTÕES:**
    * 🔸**Campos "CAMINHO" e "ARQUIVO":** Iniciam vazios e ativam "INICIAR" quando preenchidos. "LIMPAR" habilita-se quando ambos estão preenchidos.
    * 🔸**Botões:** "INICIAR" ativa script e desabilita campos. "REINICIAR" e "PARAR" controlam execução. "LIMPAR" reativa-se após "PARAR".
---

## VERSÃO 1.0 - 26/02/2024:
* **✅ O aplicativo foi desenvolvido utilizando `tkinter`:**
    * 🔹Ele possui os botões `INICIAR`, `REINICIAR` e `PARAR`, posicionados abaixo dos campos de entrada: um para o caminho do script (`CAMINHO`) e outro para o nome do arquivo (`ARQUIVO`). 
    * 🔹Logo abaixo dos botões, é exibido o campo de `STATUS`, que pode mostrar as mensagens: **"PARADO"**, **"EM EXECUÇÃO!"** ou **"REINICIANDO..."**.
    * 🔹A seção do `footer` foi adicionada logo abaixo do campo de `STATUS`, exibindo o nome do criador e o username do GitHub.

