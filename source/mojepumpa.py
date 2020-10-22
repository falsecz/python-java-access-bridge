_isPumpPending = False
import queueHandler
import watchdog
import wx
import JABHandler
import threading
    
PUMP_MAX_DELAY = 10


_pump = None
_isPumpPending = False

#: The thread identifier of the main thread.
mainThreadId = threading.get_ident()

def createPump():
    class NonReEntrantTimer(wx.Timer):
        """
        Before WXPython 4, wx.Timer was nonre-entrant, 
        meaning that if code within its callback pumped messages (E.g. called wx.Yield) and this timer was ready to fire again, 
        the timer would not fire until the first callback had completed.
        However, in WXPython 4, wx.Timer is now re-entrant.
        Code in NVDA is not written to handle re-entrant timers, so this class provides a Timer with the old behaviour.
        This should be used in place of wx.Timer and wx.PyTimer where the callback will directly or indirectly call wx.Yield or some how process the Windows window message queue. 
        For example, NVDA's core pump or other timers that run in NVDA's main thread.
        Timers on braille display drivers for key detection don't need to use this as they only queue gestures rather than actually executing them.  
        """

        def __init__(self, run=None):
            if run is not None:
                self.run = run
            self._inNotify = False
            super(NonReEntrantTimer,self).__init__()

        def run(self):
            """Subclasses can override or specify in constructor.
            """
            raise NotImplementedError

        def Notify(self):
            if self._inNotify:
                return
            self._inNotify = True
            try:
                self.run()
            finally:
                self._inNotify = False


    



    class CorePump(NonReEntrantTimer):
        "Checks the queues and executes functions."
        def run(self):
            global _isPumpPending
            _isPumpPending = False
            # print("pumpujuuu")
            watchdog.alive()
            try:
                # if touchHandler.handler:
                #     touchHandler.handler.pump()
                JABHandler.pumpAll()
                # IAccessibleHandler.pumpAll()
                queueHandler.pumpAll()
                # mouseHandler.pumpAll()
                # braille.pumpAll()
                # vision.pumpAll()
            except Exception as e:

                print("errors in this core pump cycle", e)
                # raise
            # baseObject.AutoPropertyObject.invalidateCaches()
            # print("spinkam")
            watchdog.asleep()
            # print("vstalsem")
            if _isPumpPending and not _pump.IsRunning():
                # #3803: Another pump was requested during this pump execution.
                # As our pump is not re-entrant, schedule another pump.
                _pump.Start(PUMP_MAX_DELAY, True)
    global _pump
    _pump = CorePump()

def requestPump():
    """Request a core pump.
    This will perform any queued activity.
    It is delayed slightly so that queues can implement rate limiting,
    filter extraneous events, etc.
    """
    global _isPumpPending
    global _pump

    # print("#### rp", _isPumpPending, _pump)
    if not _pump or _isPumpPending:
        return
    _isPumpPending = True
    if threading.get_ident() == mainThreadId:
        _pump.Start(PUMP_MAX_DELAY, True)
        return
    # This isn't the main thread. wx timers cannot be run outside the main thread.
    # Therefore, Have wx start it in the main thread with a CallAfter.
    import wx
    wx.CallAfter(_pump.Start,PUMP_MAX_DELAY, True)

# requestPump()
