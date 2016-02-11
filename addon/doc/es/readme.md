# dropbox #

* Autores: Patrick ZAJDA <patrick@zajda.fr>, Filaos y otros colaboradores
* Descarga [versión estable][1]

Este plugin añadirá un atajo de teclado para anunciar el estado de Dropbox,
la versión o abrirá el menú de Dropbox de la bandeja del sistema.  También
funcionan las pestañas en el diálogo preferencias con Ctrl+tab /
Ctrl+Shift+Tab y Ctrl+rePág/avPág.  Para concluir, hace que funcione el
botón cancelar con escape.

* Atajo de teclado: NVDA+Alt+D
* Ctrl+Alt+T anuncia la pestaña activa.

## Problemas conocidos ##

* Si cambias entre las pestañas utilizando los atajos de teclado, cuando cierres la ventana preferencias, NVDA no podrá saber si las ventanas ya no existen.
Es un problema conocido en NVDA y no puede corregirse.


## Cambios para 4.0 ##

* La ayuda está disponible desde el Administrador de complementos.
* El atajo de teclado para obtener el estado de Dropbox ha sido cambiado a
  Alt+NVDA+D para evitar conflictos con el soporte de atenuación de audio.

## Cambios para 3.1 ##

* Utiliza otro modo para conseguir el botón de cancelar y de  pestaña. Ahora
  no tenemos que enfocarlos antes de utilizar atajos de teclado.
* Cuando se cambia la pestaña activa, el foco se mueve a la pestaña así que
  pulsando tab, el primer elemento de la pestaña se activa en lugar de
  permanecer en la pestaña utilizada anteriormente aún si no se activó
  nunca.
* En el diálogo preferencias, ahora es posible pulsar control+Retroceso y
  avance  de página para cambiar entre pestañas. Control+tab y
  control+shift+tab todavía funcionan.
* Todos los ficheros manifest traducidos ahora deberían estar correctos.
* Correcciones menores

## Cambios para 3.0 ##

* Corrección Menor en el fichero manifest principal (los autores se muestran
  correctamente).
* Mejorada la detección del menú de contexto cuando se pulsa Shift+NVDA+D
  tres veces.
* El botón escape ahora funciona (sólo cuando se utiliza Dropbox en el mismo
  idioma que utiliza NVDA).
* Muchas correcciones en el código.
* Añadidas y actualizadas las documentaciones de todos los scripts.
* Nuevos idiomas: alemán, Árabe, checo, eslovaco, español, Finlandés,
  Gallego, holandés, Húngaro, Japonés, Nepalí, Polaco, portugués del Brasil,
  Ruso, Tamil, Turco.

## Cambios para 2.0 ##

* Nuevos idiomas: Italiano
* Pulsar el atajo de teclado tres veces o más cuando ya se está en el menú
  de contexto no causa ningún problema.

## Cambios para 1.0 ##

* Versión Inicial

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=dx
