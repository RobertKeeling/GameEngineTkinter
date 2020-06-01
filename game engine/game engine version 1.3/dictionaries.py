import importlib
import items
import backgrounds
import sprites
import itemlocales

importlib.reload(items)
importlib.reload(backgrounds)
importlib.reload(sprites)
importlib.reload(itemlocales)
idic = {"sword1":items.sword1,"sword2":items.sword2,"apple":items.apple,"dildo":items.dildo,"rubysword":items.rubysword,"orange":items.orange,"f":items.f,"f":items.f,"r":items.r,"newone":items.newone,"hh":items.hh,"hh":items.hh}
bgdic = {"background1":backgrounds.background1,"background2":backgrounds.background2,"background3":backgrounds.background3}
ildic = {"ilbackground2":itemlocales.ilbackground2,"ilbackground2":itemlocales.ilbackground2,"ilbackground2":itemlocales.ilbackground2,"ilbackground2":itemlocales.ilbackground2,"ilbackground3":itemlocales.ilbackground3,"ilbackground1":itemlocales.ilbackground1,"ilbackground3":itemlocales.ilbackground3}
spritedic = {"play1":sprites.play1}
