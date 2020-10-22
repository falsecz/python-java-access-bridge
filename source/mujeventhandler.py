
def queueEvent(eventName,obj,**kwargs):
    info = obj.getAccessibleContextInfo()
    
    p = obj
    path = []
    while p:
        path.append(p.getAccessibleContextInfo().name)
        p = p.getAccessibleParentFromContext()

    path.reverse()

    print("====> [" + eventName + "] ",">".join(path), info.description, info.role, info.description, "x", info.x, "y", info.y)

    # _trackFocusObject(eventName, obj)
    # with _pendingEventCountsLock:
    # 	_pendingEventCountsByName[eventName]=_pendingEventCountsByName.get(eventName,0)+1
    # 	_pendingEventCountsByObj[obj]=_pendingEventCountsByObj.get(obj,0)+1
    # 	_pendingEventCountsByNameAndObj[(eventName,obj)]=_pendingEventCountsByNameAndObj.get((eventName,obj),0)+1
    # queueHandler.queueFunction(queueHandler.eventQueue,_queueEventCallback,eventName,obj,kwargs)
