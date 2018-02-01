# dropbox #

* Autores: Patrick ZAJDA <patrick@zajda.fr>, Filaos e outros colaboradores.
* Baixar [versão estável][1]

Este extra adicionará um atalho para anunciar o status, a versão ou o menu
do Dropbox. Também adiciona separadores da página trabalhando na caixa de
diálogo de preferências com a guia Ctrl + / Ctrl + Shift + Tab e Ctrl +
PageUp / Down. Para concluir, faça com que o botão Cancelar funcione com
escape.

* Atalho: NVDA+Alt+D
* Ctrl + Alt + T anuncia o separador activo.

## Problemas conhecidos ##

* Se alternar entre separadores usando os atalhos, quando fechar a janela de preferências, o NVDA não saberá que essa janela não existe mais.
É um problema conhecido no NVDA e não pode ser resolvido.


## Alterações para 4.0 ##

* A ajuda adicional do extra está, agora,  disponível no gestor de extras.
* O atalho para obter o status do Dropbox foi alterado para Alt + NVDA + D
  para evitar conflitos com o suporte de ducking de áudio.

## Mudanças para 3.1 ##

* Use outra maneira de obter o botão Cancelar e o separador da
  página. Agora, não precisamos acessá-los antes de usar atalhos.
* Ao mudar o separador activo, o foco move-se para a página de registo,
  então, ao pressionar o separador, o primeiro item é activado em vez de
  permanecer no separador usado anteriormente, mesmo que não seja mais
  activado.
* Na caixa de diálogo de preferências, agora é possível pressionar o control
  + página para cima / baixo para alternar entre tabs. Control + tab e
  control + shift + tab ainda funcionam.
* Todos os ficheiros manifest localizados agora estão OK.
* Correcções menores.

## Alterações para 3.0 ##

* Correção menor no ficheiro manifest principal (os autores são mostrados
  correctamente).
* Detecção melhorada do menu de contexto ao pressionar Shift + NVDA + D três
  vezes.
* O botão de escape agora funciona (somente quando se usa o Dropbox na mesma
  língua que o NVDA usa).
* Muitas correções no código.
* Documentações de todos os scripts adicionadas / actualizadas.
* Novos idiomas: árabe, brasileiro, checo, holandês, finlandês, galego,
  alemão, húngaro, japonês, nepalês, polaco, russo, espanhol, eslovaco,
  tamil, turco.

## Mudanças para 2.0 ##

* Novo idioma: Italiano.
* Pressionar o atalho três vezes ou mais quando já está no menu de contexto
  não causa mais problema.

## Alterações para 1.0 ##

* Lançamento inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=dx
