 

import sys
import os

import globalVars
appDir = os.path.normpath(os.path.dirname(__file__))
appDir = os.path.abspath(appDir)
print(appDir)
os.chdir(appDir)
globalVars.appDir = appDir



import sourceEnv
# from pynput import mouse
# from pynput import keyboard
# sys.path.append(os.path.join('c:\\','RPA', 'NVDA', 'source'))
import JABHandler

import core
import wx


import addonHandler
JABHandler.initialize()
# import gui



# handle = int(0x0000000000030A04)

# handle = int(0x0000000000030322)
# # handle = int(0x0001042c)

# # kontext = JABHandler.JABContext(handle)
# kontext = JABHandler.JABContext(vmID=4408)

# # kontext_info = kontext.getAccessibleContextInfo()

# # kontext_info.name

# JABHandler.event_enterJavaWindow(handle)



app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.

import mojepumpa
mojepumpa.createPump()
mojepumpa.requestPump()

app.MainLoop()


# class App(wx.App):
#     def OnAssert(self,file,line,cond,msg):
#         message="{file}, line {line}:\nassert {cond}: {msg}".format(file=file,line=line,cond=cond,msg=msg)
#         log.debugWarning(message,codepath="WX Widgets",stack_info=True)

# app = App(redirect=False)
# # app.Bind(wx.EVT_QUERY_END_SESSION, onQueryEndSession)
# print("loop")
# app.MainLoop()




# def on_move(x, y):
#     print(x,y)
# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0}'.format((x, y)))

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))    
# def on_click(x, y, button, pressed):
#     if pressed:
#         print(x,y)
# def on_release(key):
# #    print('{0} released'.format(key))
#     if key == keyboard.Key.esc:
#         k_listener.stop()
#         m_listener.stop()
#         # Stop listener
#         return False 


# print("pump")
# core.requestPump()
# with keyboard.Listener(on_release=on_release) as k_listener, mouse.Listener(on_click=on_click) as m_listener:
    
#     k_listener.join()
#     m_listener.join()   
