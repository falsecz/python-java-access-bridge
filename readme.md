- Pozor potrebuje to python 3.7
- Zdrojaky jsou aktualne hroznej mess.
```
git clone git@github.com:falsecz/python-java-access-bridge.git
cd python-java-access-bridge
git submodule update --init
cd source
python fh.py
```
asi je potreba doinstalovat pres pip, tak 2-3 zavislosti, podle toho na cem to spadne


fh.py inicializuje JABHandler, vytvori se wx.App a pripravi se pumpa na udalosti kterej vybira frontu z JABHandleru a odbavuje na jinym threadu (viz. mujeventhandler.py)
