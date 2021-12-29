from manim import *
import itertools
r = 0.4
font_size = 20

def create_seq(obj):
    return [Create(obj_i) for obj_i in obj]

class NeuralNet(Scene):
    def create_circles(self,count: int,radius: int=r,color: str=WHITE,fill_color: str=GREY):
        circles = VGroup(*[
            Circle(radius=r,color=WHITE) for _ in range(count)
        ])
        for circle in circles:
            circle.set_fill(GREY,opacity=0.5)
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

    def construct(self):
        # creating the layers
        input_obj, input_nodes = self.create_layer("Input Layer",LEFT*3,3)
        output_obj, output_nodes = self.create_layer("Output Layer",RIGHT,1)
        weight_lines = self.link_layers(input_nodes,output_nodes)
        big_obj = VGroup(input_obj,output_obj,weight_lines)
        big_obj.move_to(ORIGIN)
        # animating the input layer
        self.play(*create_seq(input_obj))
        self.wait()
        # animating the output layer
        self.play(*create_seq(output_obj))
        self.wait()
        # centering it
        self.play(*create_seq(weight_lines))
        self.wait()
        



    
