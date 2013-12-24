#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx


class MainId (object):
    """
    Коллекция ID для меню и панели главного окна
    С появлением Actions эти константы становятся ненужными. В идеале от них нужно избавиться.
    """
    ID_RELOAD = wx.NewId()
    ID_ABOUT = wx.ID_ABOUT
    ID_HELP = wx.ID_HELP_COMMANDS
    ID_VIEW_TREE = wx.NewId()
    ID_VIEW_ATTACHES = wx.NewId()
    ID_VIEW_TAGSCLOUD = wx.NewId()
    ID_VIEW_FULLSCREEN = wx.NewId()
    ID_UNDO = wx.ID_UNDO
    ID_REDO = wx.ID_REDO
    ID_CUT = wx.ID_CUT
    ID_COPY = wx.ID_COPY
    ID_PASTE = wx.ID_PASTE
    ID_ADD_TAGS_TO_BRANCH = wx.NewId()
    ID_REMOVE_TAGS_FROM_BRANCH = wx.NewId()
    ID_RENAME_TAG = wx.NewId()
