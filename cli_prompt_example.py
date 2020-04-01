
from manimlib.imports import *
from LinuxScene import *
from LinuxMobject import *

class cli_prompt_example(LinuxScene):

    def construct(self):
        user = LinuxMobject(scene=self, title="runner", desc="user", title_color=BLUE)
        host = LinuxMobject(scene=self, title=" @ e0bb35481dc9 : ", desc="host", title_color=RED)
        cwd = LinuxMobject(scene=self, title="\\textapprox/LinuxTut-env-1", desc="current directory", title_color=GREEN)
        dollar = LinuxMobject(scene=self, title=" \$ ", desc="user type")
        obj_order = [user, host, cwd, dollar]

        prompt = self.arrangeObjs(obj_order)
        self.doIntro(prompt, obj_order)
        self.playAll(obj_order)

