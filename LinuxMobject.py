
from manimlib.imports import *

class LinuxMobject():
    title = None
    title_color = WHITE 
    scene = None
    desc = None
    desc_group = None 
    nextObj = None
    prevObj = None

    def __init__(self, scene, title, desc=None, title_color=WHITE, nextObj=None, prevObj=None):
        self.scene = scene 
        self.title_color = title_color
        if desc:
            self.desc = desc
        self.title = TextMobject("\\texttt{" + title + "}", color=self.title_color)
        if nextObj:
            self.nextObj = nextObj 
        if prevObj:
            self.prevObj = prevObj

    def arrangeArrowDesc(self):
        if self.desc:
            self.desc_group = self.createArrowAndDesc(self.title, self.desc)

    def createArrowAndDesc(self, mobj_next_to, desc, dir=UP):
        arrow = Vector(direction=dir)
        arrow.next_to(mobj_next_to, dir*-1)
        desc = TextMobject(desc)
        desc.next_to(arrow, dir*-1)
        group = VGroup(arrow, desc)
        return group

    def showAndWriteGroup(self, group):
        arrow = group.submobjects[0] 
        text = group.submobjects[1]
        self.scene.play(GrowArrow(arrow))
        self.scene.wait(1)
        self.scene.play(Write(text))
        self.scene.wait(1)

    def playNext(self):
        if self.prevObj:
            self.scene.play(FadeOut(self.prevObj.desc_group))
            self.scene.play(FadeIn(self.title))
        self.showAndWriteGroup(self.desc_group)
