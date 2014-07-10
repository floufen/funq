# -*- coding: utf-8 -*-

# Copyright: SCLE SFE
# Contributor: Julien Pagès <j.parkouss@gmail.com>
# 
# This software is a computer program whose purpose is to test graphical
# applications written with the QT framework (http://qt.digia.com/).
# 
# This software is governed by the CeCILL v2.1 license under French law and
# abiding by the rules of distribution of free software.  You can  use, 
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info". 
# 
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability. 
# 
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or 
# data to be ensured and,  more generally, to use and operate it in the 
# same conditions as regards security. 
# 
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL v2.1 license and that you accept its terms.

"""
Déclaration des erreur définies par la librarie funq.
"""

class FunqError(Exception):
    """
    Exception levée lorsque le serveur libFunq renvoie une erreur.
    les attributs `classname` et `desc` sont stockés dans l'exception
    et correspondent aux attributs de même nom renvoyés par le serveur
    libFunq.
    """
    def __init__(self, classname, desc):
        self.classname = classname
        self.desc = desc
        Exception.__init__(self, u"{classname}: {desc}".format(
                classname=classname,
                desc=desc))

class TimeOutError(Exception):
    """Levée lors d'un timeout"""

class HooqAliasesInvalidLineError(Exception):
    """
    Exception levée lors d'erreur de parsing du fichier d'alias.
    """
    pass

class HooqAliasesKeyError(KeyError):
    """
    Exception levée lors de doublon d'alias ou d'alias non existant.
    """
    pass
