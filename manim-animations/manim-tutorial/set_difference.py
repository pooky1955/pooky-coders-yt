from manim import *
class SetDifference(Scene):
    def construct(self):
        circle = Circle()
        circle2 = Circle()
        circle2.next_to(circle,LEFT)
        circle2
        self.play(Create(circle),Create(circle2))
        
        
        
