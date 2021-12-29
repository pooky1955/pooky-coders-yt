from manim import *
import numpy as np
import itertools
r = 0.4
font_size = 20
input_nodes_values = np.array([
    0.32,
    0.82,
    0.51
])
weights = np.array([
    0.5,
    0.23,
    -0.3
])
def create_seq(obj):
    return [Create(obj_i) for obj_i in obj]

class NeuralNet(Scene):
    def create_circles(self,count: int,radius: int=r,color: str=WHITE,fill_color: str=GREY):
        circles = VGroup(*[
            Circle(radius=r,color=WHITE) for _ in range(count)
        ])
        head = circles[0]
        circles.arrange(DOWN,buff=0.5)
        return circles


    def create_layer(self,name: str,pos: np.array,count: int,radius: int=r,color:str=WHITE,fill_color: str=GREY):
        layer_nodes = self.create_circles(count,radius,color,fill_color)
        head = layer_nodes[0]
        layer_text = MarkupText(name,font_size=font_size).next_to(head, UP)
        layer_objs = [*layer_nodes,layer_text]
        layer = VGroup(*layer_objs)
        layer.shift(pos)
        return layer, layer_nodes

    def link_layers(self,layer1,layer2):
        lines = VGroup(*[
            Line(node1,node2) for node1, node2 in itertools.product(layer1,layer2)
        ])
        return lines
    
    def label_nodes(self,nodes,values):
        text = VGroup()
        for node,value in zip(nodes,values):
            dc = DecimalNumber(value)
            dc.next_to(node,LEFT)
            text.add(dc)
        return text

    def animate_nodes(self,nodes,values):
        return [node.animate.set_opacity(value) for node, value in zip(nodes,values)]

    def highlight_lines(self,lines,values):
        colored_values = values / 2 +0.5
        return [line.animate.set_color(interpolate_color(RED, GREEN, value)) for line,value in zip(lines,colored_values)]

    def morph_line_to_number(self,lines: List[Line],weights: np.ndarray):
        for index, (line,weight) in enumerate(zip(lines,weights)):
            line, weight = lines[index], weights[index]
            l2 = line.copy()
            mathtex = MathTex(fr"w_{index}={weights[index]}")
            mathtex.set_stroke_color(RED)
            mathtex.shift(RIGHT*3,UP*(2-index/1.2))
            self.play(ReplacementTransform(l2,mathtex))
            # return ReplacementTransform(l2,mathtex), mathtex

    def construct(self):
        # creating the layers
        input_obj, input_nodes = self.create_layer("Input Layer",LEFT*3,3)
        output_obj, output_nodes = self.create_layer("Output Layer",RIGHT,1)
        weight_lines = self.link_layers(input_nodes,output_nodes)
        decimal_annotations = self.label_nodes(input_nodes,input_nodes_values)
        big_obj = VGroup(input_obj,decimal_annotations,output_obj,weight_lines)
        # centering it
        big_obj.move_to(ORIGIN)
        # INPUT LAYER NODES APPEAR
        self.play(*create_seq(input_obj))
        # INPUT LAYER VALUES APPEAR
        input_layer_fill_anims = self.animate_nodes(input_nodes,input_nodes_values)
        self.play(FadeIn(decimal_annotations),*input_layer_fill_anims)
        # INPUT LAYER FILL APPEAR
        self.wait()
        # animating the lines
        self.play(*create_seq(output_obj))
        # showing the weight lines
        self.play(*create_seq(weight_lines))
        # show the value of these weights
        lines_anim = self.highlight_lines(weight_lines, weights)
        self.play(*lines_anim)
        self.wait()
        self.play(big_obj.animate.shift(LEFT*2))
        self.morph_line_to_number(weight_lines,weights)
        self.wait()


        



    
