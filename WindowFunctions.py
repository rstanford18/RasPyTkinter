import tkinter as tk
# 
# 
# def _focusNext(widget):
#     '''Return the next widget in tab order'''
#     widget = tk.call('tk_focusNext', widget._w)
#     if not widget: 
#         return None
#     else:
#         return tk.nametowidget(widget.string)
# 
# def OnTextTab(event):
#     '''Move focus to next widget'''
#     widget = event.widget
#     next = _focusNext(widget)
#     next.focus()
#     return "break"