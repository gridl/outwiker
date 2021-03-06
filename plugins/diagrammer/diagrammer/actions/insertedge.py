# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod

import wx

from outwiker.gui.baseaction import BaseAction

from ..i18n import get_
from ..gui.insertedgedialog import (InsertEdgeDialog,
                                    InsertEdgeControllerNone,
                                    InsertEdgeControllerLeft,
                                    InsertEdgeControllerRight,
                                    InsertEdgeControllerBoth)


class InsertEdgeBaseAction (BaseAction):
    """
    Базовый класс для действий вставки ребер
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def getController (self, dlg):
        """
        Метод должен возвращать контроллер, создающий строку, описывающую создаваемое ребро
        """
        pass


    def run (self, params):
        assert self._application.mainWindow is not None

        with InsertEdgeDialog (self._application.mainWindow) as dlg:
            controller = self.getController (dlg)
            result = controller.showDialog()

            if result == wx.ID_OK:
                codeEditor = self._application.mainWindow.pagePanel.pageView.codeEditor
                codeEditor.replaceText (controller.getResult())



class InsertEdgeNoneAction (InsertEdgeBaseAction):
    """
    Вставить ребро без "головы"
    """
    def __init__ (self, application):
        self._application = application

        global _
        _ = get_()

    stringId = u"Diagrammer_InsertEdgeNone"


    @property
    def title (self):
        return _(u"Insert edge without any arrow")


    @property
    def description (self):
        return _(u"Diagrammer. Insert edge without any arrow")


    def getController (self, dlg):
        return InsertEdgeControllerNone (dlg)



class InsertEdgeRightAction (InsertEdgeBaseAction):
    """
    Вставить ребро со стрелкой направо
    """
    def __init__ (self, application):
        self._application = application

        global _
        _ = get_()

    stringId = u"Diagrammer_InsertEdgeRight"


    @property
    def title (self):
        return _(u"Insert edge with the right arrow")


    @property
    def description (self):
        return _(u"Diagrammer. Insert edge with the right arrow")


    def getController (self, dlg):
        return InsertEdgeControllerRight (dlg)



class InsertEdgeLeftAction (InsertEdgeBaseAction):
    """
    Вставить ребро со стрелкой налево
    """
    def __init__ (self, application):
        self._application = application

        global _
        _ = get_()

    stringId = u"Diagrammer_InsertEdgeLeft"


    @property
    def title (self):
        return _(u"Insert edge with the left arrow")


    @property
    def description (self):
        return _(u"Diagrammer. Insert edge with the left arrow")


    def getController (self, dlg):
        return InsertEdgeControllerLeft (dlg)


class InsertEdgeBothAction (InsertEdgeBaseAction):
    """
    Вставить ребро со стрелками с обоих сторон
    """
    def __init__ (self, application):
        self._application = application

        global _
        _ = get_()

    stringId = u"Diagrammer_InsertEdgeBoth"


    @property
    def title (self):
        return _(u"Insert edge with the both arrows")


    @property
    def description (self):
        return _(u"Diagrammer. Insert edge with the both arrows")


    def getController (self, dlg):
        return InsertEdgeControllerBoth (dlg)
