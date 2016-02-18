# dropbox #

* Autores: Patrick ZAJDA <patrick@zajda.fr>, Filaos e outros colaboradores
* Baixe a [versão estável][1]

Este plug-in adiciona um atalho para anunciar o status ou a versão do
Dropbox ou abrir o menu dele na área de notificação. Também torna possível
alternar entre as guias da janela de preferências com
Ctrl+Tab/Ctrl+Shift+Tab e Ctrl+PageUp/Down. Finalmente, faz com que o botão
cancelar seja ativado com escape.

* Atalho: NVDA+Alt+D
* Ctrl+Alt+T anuncia a guia ativa

## Problemas conhecidos ##

* Se você mudar de guia usando os atalhos, quando fechar a janela de preferências o NVDA não saberá que a janela deixou de existir.
Isso é um problema do NVDA que não tem como corrigir.


## Mudanças na 4.0 ##

* A ajuda do complemento está disponível pelo gestor de complementos.
* O atalho para ler o status do Dropbox foi alterado para Alt+NVDA+D para
  evitar conflito com o suporte a prioridade de áudio.

## Mudanças na 3.1 ##

* Usa-se outro jeito de capturar o botão cancelar e a guia de página. Agora
  não se precisa mais focá-los antes de usar os atalhos.
* Ao trocar a guia ativa, o foco vai para a guia de página de modo que ao
  pressionar tab, ativa-se o primeiro item da guia ao invés de permanecer na
  guia anteriormente usada mesmo que esta não esteja mais ativada.
* Na janela de preferências, pode-se agora pressionar control+page up/down
  para alternar entre guias. Control+tab e control+shift+tab continuam
  funcionando.
* Todos os arquivos de manifesto traduzidos devem agora estar OK.
* Correções menores

## Mudanças na 3.0 ##

* Pequena correção no arquivo principal de manifesto (os autores são
  exibidos corretamente).
* Melhorada detecção do menu de contexto ao pressionar três vezes
  shift+NVDA+b.
* Agora o botão escape funciona (somente ao usar o Dropbox no mesmo idioma
  que está o NVDA).
* Uma série de correções no código.
* Adicionada/atualizada documentação de todos os scripts.
* Novos idiomas: Alemão, Árabe, Tcheco, Eslovaco, Espanhol, Finlandês,
  Galego, Holandês, Húngaro, Japonês, Nepalês, Polonês, Português do Brasil,
  Russo, Tâmil, Turco.

## Mudanças na 2.0 ##

* Novo idioma: Italiano
* Pressionar o atalho três vezes ou mais quando já está no menu de contexto
  não dá mais problema.

## Mudanças na 1.0 ##

* Primeira versão pública

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=dx
