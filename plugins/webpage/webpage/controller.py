# -*- coding: UTF-8 -*-

import os
import os.path
import sys

import wx

from outwiker.core.factoryselector import FactorySelector
from outwiker.core.system import getOS

from webnotepage import WebPageFactory, WebNotePage
from actions.downloadaction import (CreateChildWebPageAction,
                                    CreateSiblingWebPageAction)


class Controller (object):
    """
    Класс отвечает за основную работу интерфейса плагина
    """
    def __init__ (self, plugin, application):
        """
        """
        self._plugin = plugin
        self._application = application


    def initialize (self):
        self._menuName = _(u"Web page")
        self._createGui()

        self._correctSysPath()

        self._application.onPageDialogPageFactoriesNeeded += self.__onPageDialogPageFactoriesNeeded
        FactorySelector.addFactory (WebPageFactory())


    def _correctSysPath (self):
        cmd_folder = unicode (os.path.dirname(os.path.abspath(__file__)),
                              getOS().filesEncoding)
        cmd_folder = os.path.join (cmd_folder, u'libs')

        syspath = [unicode (item, getOS().filesEncoding)
                   if type (item) != type(u"")
                   else item for item in sys.path]

        if cmd_folder not in syspath:
            sys.path.insert(0, cmd_folder)


    def destroy (self):
        self._removeGui()

        self._application.onPageDialogPageFactoriesNeeded -= self.__onPageDialogPageFactoriesNeeded
        FactorySelector.removeFactory (WebPageFactory().getTypeString())


    def _createGui (self):
        if self._application.mainWindow is not None:
            self._createMenu()
            self._createChildWebPageAction()
            self._createSiblingWebPageAction()


    def _removeGui (self):
        mainWindow = self._application.mainWindow
        if (mainWindow is not None and
                mainWindow.PLUGINS_TOOLBAR_STR in mainWindow.toolbars):
            self._application.actionController.removeMenuItem (CreateChildWebPageAction.stringId)
            self._application.actionController.removeToolbarButton (CreateChildWebPageAction.stringId)
            self._application.actionController.removeAction (CreateChildWebPageAction.stringId)

            self._application.actionController.removeMenuItem (CreateSiblingWebPageAction.stringId)
            self._application.actionController.removeToolbarButton (CreateSiblingWebPageAction.stringId)
            self._application.actionController.removeAction (CreateSiblingWebPageAction.stringId)

            index = mainWindow.mainMenu.FindMenu (self._menuName)
            assert index != wx.NOT_FOUND

            mainWindow.mainMenu.Remove (index)


    def __onPageDialogPageFactoriesNeeded (self, page, params):
        if (params.pageForEdit is not None and
                params.pageForEdit.getTypeString() == WebNotePage.getTypeString()):
            params.addPageFactory (WebPageFactory())


    def _createMenu (self):
        self.menu = wx.Menu (u'')
        self._application.mainWindow.mainMenu.Append (self.menu, self._menuName)


    def _createChildWebPageAction (self):
        mainWindow = self._application.mainWindow

        if (mainWindow is not None and
                mainWindow.PLUGINS_TOOLBAR_STR in mainWindow.toolbars):
            action = CreateChildWebPageAction(self._application)
            toolbar = mainWindow.treePanel.panel.toolbar
            image = self.getImagePath (u'create-child.png')

            controller = self._application.actionController

            controller.register (action, hotkey=None)
            controller.appendMenuItem (CreateChildWebPageAction.stringId, self.menu)
            controller.appendToolbarButton (CreateChildWebPageAction.stringId,
                                            toolbar,
                                            image)


    def _createSiblingWebPageAction (self):
        mainWindow = self._application.mainWindow

        if (mainWindow is not None and
                mainWindow.PLUGINS_TOOLBAR_STR in mainWindow.toolbars):
            action = CreateSiblingWebPageAction(self._application)
            toolbar = mainWindow.treePanel.panel.toolbar
            image = self.getImagePath (u'create-sibling.png')

            controller = self._application.actionController

            controller.register (action, hotkey=None)
            controller.appendMenuItem (CreateSiblingWebPageAction.stringId, self.menu)
            controller.appendToolbarButton (CreateSiblingWebPageAction.stringId,
                                            toolbar,
                                            image)


    def getImagePath (self, imageName):
        """
        Получить полный путь до картинки
        """
        imagedir = unicode (os.path.join (os.path.dirname (__file__), "images"), getOS().filesEncoding)
        fname = os.path.join (imagedir, imageName)
        return fname
