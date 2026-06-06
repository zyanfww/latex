from manimlib import *

class LatexTest(InteractiveScene):
    def construct(self):
        self.add(Text("LaTeX"))
        self.add(Integer(1).scale(0.4).to_edge(DOWN, buff=MED_SMALL_BUFF))