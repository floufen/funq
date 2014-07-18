About Funq
==========

funq is a tool for creating FUNctional tests for Qt applications using python.
Please be patient, english translation is coming soon !

Description de Funq
===================

`Funq` est un utilitaire de tests fonctionnels d'ihm écrites en QT. Il est
distribué sous la licence CeCILL v2.1 (proche de la GPL 2). Voir le fichier
LICENCE-fr.txt pour plus de détails.

Il est séparé en deux parties, serveur et client.

Documentation pour les utilisateurs du framework de test (les testeurs)
-----------------------------------------------------------------------

La doc doit être générée, et l'outil sphinx est requis pour cela.

.. code-block:: bash
  
  cd client/doc
  make html
  # ouvrir le fichier _build/html/index.html

.. note::
  
  La documentation pour l'installation est décrite dans cette doc générée.

Tests unitaires du framework (python)
-------------------------------------

.. code-block:: bash
  
  cd client
  nosetests

Tests unitaires du framework (cpp)
----------------------------------

.. code-block:: bash
  
  cd server/tests
  qmake && make check