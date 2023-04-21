# dropbox #

* Autores: Patrick ZAJDA <patrick@zajda.fr>, Filaos e outros colaboradores
* NVDA compatibility: NVDA 2019.1 or later
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]

Este plug-in adiciona um atalho para anunciar o status do Dropbox ou abrir o
menu dele na área de notificação quando pressionado uma ou duas vezes,
respectivamente. Ele também melhora as listas de itens do Dropbox.

* Atalho: NVDA+Alt+D


## Changes for 4.6 ##

* Specify NVDA 2021.1 compatibility

## Mudanças na 4.4 ##

* Compatibilidade com Python 3
* Usa o modelo mais recente de complemento
* Mudança no repositório para ser compilado com Appveyor
* Corrigido um atalho errado e removido um não usado da documentação
* Atualizada a descrição na documentação, que ainda referenciava o anúncio
  da versão

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
