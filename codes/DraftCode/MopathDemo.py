
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.directutil.Mopath import Mopath
from direct.interval.IntervalGlobal import *

class Application(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)

        self.smiley = self.loader.loadModel("/e/models/smiley")
        self.smiley.reparentTo(self.render)

        self.mopath = Mopath()
        self.mopath.loadFile("/e/models/path")

        self.ival = MopathInterval(self.mopath,
                                   self.smiley,
                                   duration = 10)
        self.ival.loop()

        self.cam.setPos(0, -20, 0)

app = Application()
app.run()
