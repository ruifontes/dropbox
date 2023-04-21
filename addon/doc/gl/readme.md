# dropbox #

* Autores: Patrick ZAJDA <patrick@zajda.fr>, Filaos e outros colaboradores
* Compatibilidade con NVDA: NVDA 2019.1 ou posterior
* Descarga [versión estable][1]
* Descarga [versión de desenvolvemento][2]

Este plugin engadirá un atallo de teclado para anunciar o estado do Dropbox
ou abrir o menú do Dropbox na bandexa do sistema cando se preme unha ou dúas
veces respectivamente.  Tamén mellora as listas de elementos de Dropbox.

* Atallo de teclado: NVDA+alt+D


## Cambios para 4.6 ##

* Expecificar compatibilidade con NVDA 2021.1

## Cambios para 4.4 ##

* Compatibilidade con Python 3
* Utilízase a última plantilla de complemento
* Troco no repositorio para que se constrúa con Appveyor
* Arranxadas ordes incorrectas e eliminadas aquelas sen uso na documentación
* Actualizada a descripción na documentación que aínda referenciaba o
  anunciado da versión

## Cambios para 4.0 ##

* A axuda do complemento está dispoñible dende o Administrador de
  complementos.
* O atallo de teclado para obter o estado de Dropbox cambiouse a Alt+NVDA+D
  para evitar confrictos co soporte da atenuación do audio.

## Cambios para 3.1 ##

* Utiliza outra maneira para obter o botón cancelar e pestana. Agora non
  temos que enfocalo antes de utilizar atallos de teclado.
* Cando se cambia á pestana activa, o foco móvese á pestana así cando se
  preme tab, o primeiro elemento da pestana actívase en lugar de quedar na
  pestana utilizada con anterioridade aínda se non se activou nunca.
* No diálogo preferencias, agora é posible premer control+retroceso ou
  avance de páxina para cambiar entre pestanas. Control+tab e
  control+shift+tab aínda funcionan.
* Todos os ficheiros manifest traducidos agora deberían estár correctos.
* Ccorreccións menores.

## Cambios para 3.0 ##

* Corrección menor no ficheiro principal manifest (os autores amósanse
  correctamente).
* Mellorada a detección do menú de contexto cando se preme Shift+NVDA+D tres
  veces.
* O botón escape agora funciona (só cando se utiliza Dropbox na mesma lingua
  que usa NVDA).
* Un lote de correccións no código.
* Engadida/actualizada a documentación de todos os scripts.
* Novas linguas: Árabe, Portugués do Brasil, Checo, Holandés, Finlandés,
  Galego, Alemán, Húngaro, Xaponés, Nepalí, Polaco, Ruso, Español, Eslovaco,
  Tamil, Turco.

## Cambios para 2.0 ##

* Novas linguas: Italiano
* Premendo o atallo de teclado tres veces ou máis cando xa se está no menú
  de contexto non causa problemas nunca máis.

## Cambios para 1.0 ##

* Versión Inicial

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
