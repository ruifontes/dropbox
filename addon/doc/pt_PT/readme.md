# dropbox


## Informações
* Autores: Rui Fontes, Patrick ZAJDA, Filaos e outros colaboradores.
* Compatibilidade com NVDA: NVDA 2019.3 ou posterior
* Descarregar [versão estável][1]


## Apresentação
Este extra adiciona um atalho para anunciar o status do Dropbox ou abrir o menu do Dropbox quando pressionado uma ou duas vezes,
respectivamente.

O comando é NVDA+Alt+D
Como sempre, é possível alterá-lo no diálogo Definir comandos na categoria Dropbox.


## Alterações


### Alterações na 2023.10.01
* Compatibilidade estendida para NVDA 2024.1;
* pequena correção no código de leitura do ícone da barra do sistema, devido à correção pela Microsoft.


### Alterações na 2023.3
* Fixada compatibilidade para NVDA 2023.1;
* A manutenção passou a estar a cargo de Rui Fontes e Equipa portuguesa do NVDA.


### Alterações para 4.6
* Especifica a compatibilidade com o NVDA 2021.1


### Alterações para 4.4
* Compatibilidade com o python 3.
* Usa o último modelo de extras
* mudanças do repositório criadas com o Appveyor
* Corrigidos atalhos errados e removidos da documentação
* Actualiza a descrição na documentação que ainda faz referência ao anúncio da versão


### Alterações para 4.0
* A ajuda adicional do extra está, agora,  disponível no gestor de extras.
* O atalho para obter o status do Dropbox foi alterado para Alt + NVDA + D para evitar conflitos com o suporte à diminuição de áudio.


### Mudanças para 3.1
* Usada outra maneira de obter o botão Cancelar e o separador da
  página. Agora, não precisamos acessá-los antes de usar atalhos.
* Ao mudar o separador activo, o foco move-se para a página de registo, então, ao pressionar o separador, o primeiro item é activado em vez de  permanecer no separador usado anteriormente, mesmo que não seja mais activado.
* Na caixa de diálogo de preferências, agora é possível pressionar o control + página para cima / baixo para alternar entre tabs. Control + tab e control + shift + tab ainda funcionam.
* Todos os ficheiros manifest localizados agora estão OK.
* Correcções menores.


### Alterações para 3.0
* Correção menor no ficheiro manifest principal (os autores são mostrados correctamente).
* Detecção melhorada do menu de contexto ao pressionar Shift + NVDA + D três vezes.
* A tecla Escape agora funciona (somente quando se usa o Dropbox na mesma  língua que o NVDA usa).
* Muitas correções no código.
* Documentações de todos os scripts adicionadas / actualizadas.
* Novos idiomas: árabe, brasileiro, checo, holandês, finlandês, galego,  alemão, húngaro, japonês, nepalês, polaco, russo, espanhol, eslovaco,  tamil, turco.


### Mudanças para 2.0
* Novo idioma: Italiano.
* Pressionar o atalho três vezes ou mais quando já está no menu de contexto não causa mais problema.


### Alterações para 1.0
* Lançamento inicial


[1]: https://github.com/ruifontes/dropbox/releases/download/2023.10.01/dropbox-2023.10.01.nvda-addon
