import os
os.chdir("z:\\bender\\Develop\\sbks\\nvda\\source")
import sourceEnv
import JABHandler
JABHandler.initialize()

import wx

from pynput import mouse
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
# with mouse.Listener(
#         on_move=on_move,
        
#         ) as listener:
#     listener.join()


listener = mouse.Listener(
    on_move=on_move,
)
listener.start()

import threading
def thread_function():
    
    # internalFunctionQueue
    # print('.')
    while True:
        print(JABHandler.internalFunctionQueue.qsize())
        # a = 3


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()
# class App(wx.App):
#     def OnAssert(self,file,line,cond,msg):
#         message="{file}, line {line}:\nassert {cond}: {msg}".format(file=file,line=line,cond=cond,msg=msg)
#         log.debugWarning(message,codepath="WX Widgets",stack_info=True)

# app = App(redirect=False)
# app.Bind(wx.EVT_QUERY_END_SESSION, onQueryEndSession)
# print("loop")
# app.MainLoop()

# x = threading.Thread(target=thread_function, args=(), daemon=True)
# x.start()
# x.join()