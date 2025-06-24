# [ATUALIZAÇÕES:](./UPDATES.md#vers%C3%A3o-10---26022024)
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
* ✅COMPORTAMENTO DOS CAMPOS E BOTÕES:
    * 🔸**Campos "CAMINHO" e "ARQUIVO":** Iniciam vazios e ativam "INICIAR" quando preenchidos. "LIMPAR" habilita-se quando ambos estão preenchidos.
    * 🔸**Botões:** "INICIAR" ativa script e desabilita campos. "REINICIAR" e "PARAR" controlam execução. "LIMPAR" reativa-se após "PARAR".
---

## VERSÃO 1.0 - 26/02/2024:
* ✅O aplicativo foi lançado para oferecer uma maneira fácil e conveniente de executar comandos e scripts Python a partir de uma interface gráfica amigável.
* ✅Permite aos usuários especificar o caminho do arquivo e o nome do arquivo Python que desejam executar, oferecendo a opção de iniciar ou reiniciar a execução do script conforme necessário.
* ✅Eu criei o aplicativo para facilitar a execução de bots Python diretamente pelo console, seguindo o conceito do "nodemon", evitando a necessidade de reinicialização manual após modificações no código.
