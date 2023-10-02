# dropbox #

* Auteurs : Patrick ZAJDA <patrick@zajda.fr>, Filaos et d'autres
  contributeurs
* Compatibilité NVDA : 2019.1 et ultérieurs
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Cette extension ajoute un raccourci permettant d'annoncer le statut ou la
version de Dropbox, mais aussi d'ouvrire le menu contextuel de l'icône
Dropbox dans la zone de notification.  Elle rends également possible
d'utiliser les onglets de la boîte de dialogue préférences avec Ctrl+tab /
Ctrl+Maj+Tab et Ctrl+PagePréc/Suiv.  Pour conclure, ajoute échapp pour
activer le bouton Annuler.

* Raccourci : NVDA+Alt+D


## Changements pour la version 4.6 ##

* Spécifie la compatibilité avec NVDA 2021.1

## Changements pour la version 4.4 ##

* Compatibilité Python 3
* Utilisation du dernier modèle d'extension
* Changement de dépôt pour être compatible avec Appveyor
* Correction de raccourcis inutilisés ou incorrects et supprimés dans la
  documentation
* Mise à jour de la description dans la documentation qui faisait encore
  référence à l'annonce de la version

## Changements pour la version 4.0 ##

* L'aide de l'extension est disponible à partir du Gestionnaire
  d'Extensions.
* Le raccourci pour obtenir le statut de Dropbox a été changé par Alt+NVDA+D
  pour éviter tout conflit avec le support d'atténuation audio.

## Changements pour la version 3.1 ##

* - Le bouton échappe et les onglets fonctionne même si le bouton Annulé/la
  liste d'onglets n'a jamais eu le focus.
* Lorsque l'on change d'onglet, le premier élément de celui-ci a le focus
  comme dans une fenêtre Windows standard.
* Dans le dialogue des préférences de Dropbox, il est maintenant possible
  d'utiliser control+page prec/suiv en plus de Ctrl+Tab/Ctrl+Shift+tab pour
  changer d'onglet.
* Tous les fichiers Manifest sont corrigés.
* Corrections mineures.

## Changements pour la version 3.0 ##

* Corrections mineures dans le fichier manifest.ini principal (les auteurs
  sont correctement affichés)
* Amélioration de la détection du menu contextuel lorsqu'on appui trois fois
  sur maj+NVDA+D.
* Le bouton échapp fonctionne maintenant (seulement si Dropbox est dans la
  même langue que NVDA).
* De nombreuses corrections dans le code.
* Ajout/mise à jours de la documentation de tous les scripts.
* Nouvelles langues: Arabe, Portugais Brésilien, Tchèque, Néerlandais,
  Finnois, Galicien, Allemand, Hongrois, Japonais, Népalais, Polonais,
  Russe, Espagnol, Slovak, Tamoul, Turc.

## Changements pour la version 2.0 ##

* Nouvelles langues : Italien
* Faire trois fois le raccourci pour ouvrire le menu contextuel lorsque
  celui-ci est déjà ouvert ne le refermera plus ni ne le fera buguer
  autrement.

## Changements pour la version 1.0 ##

* Première version.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=dropbox

[2]: https://www.nvaccess.org/addonStore/legacy?file=dx-dev
