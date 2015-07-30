# dropbox #

* Autores: Patrick ZAJDA, Filaos e outros colaboradores
* Descarga [versión estable][1]
* Descarga [versión de desenvolvemento][2]

Este plugin engadirá un atallo de teclado para anunciar o estado do Dropbox,
a versión ou abrirá o menú do Dropbox na bandexa do sistema.  Tamén
funcionan as pestanas no diálogo preferencias con Ctrl+tab / Ctrl+Shift+Tab
e Ctrl+rePáx/avPáx.  Para concluir, fai funcionar o botón cancelar co
escape.

* Atallo de teclado: NVDA+Shift+D
* Ctrl+Alt+T anuncia a pestana activa.

## Problemas coñecidos ##

* Se cambias entre pestanas utilizando os atallos de teclado, cando peches a ventá de preferencias, NVDA non poderá saber se aínda existe a ventá.
É un problema coñecido no NVDA e non se pode correxir.

## Cambios para 4.0 ##

* Traduccións actualizadas.
* Correxidos problemas ca app de Windows 8 metro.

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
* Ccorreccións menores

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

[1]: http://addons.nvda-project.org/files/get.php?file=dx

[2]: http://addons.nvda-project.org/files/get.php?file=dx-dev
