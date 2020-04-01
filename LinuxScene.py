from manimlib.imports import *

class LinuxScene(Scene):
    def getGroupFromList(self, lobj_list):
        text_group = VGroup()
        for lobj in lobj_list:
            text_group.add(lobj.title)
        return text_group

    def arrangeObjs(self, lobj_list):
        text_group = self.getGroupFromList(lobj_list)
        text_group.arrange()
        for i in range(len(lobj_list)):
            current = lobj_list[i]
            if i != 0:                
                current.prevObj = lobj_list[i-1]
            if i < len(lobj_list)-1:
                current.nextObj = lobj_list[i+1]
            current.arrangeArrowDesc() 
        return text_group

    def doIntro(self, prompt, lobj_list):
        text_group = self.getGroupFromList(lobj_list[1:])
        self.wait(1)
        self.play(Write(prompt))
        self.wait(1)
        self.play(FadeOut(text_group))

    def playAll(self, lobj_list):
        for lobj in lobj_list:
            lobj.playNext()