from manim import *
class CreateCircle(Scene):
    def construct(self):
        circle = Circle(2)
        circle.set_fill(PINK,opacity=0.6)
        circle2 = Circle(4)
        circle2.set_fill(BLUE, opacity=0.6)
        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.next_to(circle,RIGHT,buff=2)
        self.play(Create(circle),Create(square))
        self.play(Transform(circle,circle2))
        # self.play(FadeOut(circle2))

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(
            ReplacementTransform(square,circle)
        )
        self.play(
            circle.animate.set_fill(PINK,opacity=0.5)
        )

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()