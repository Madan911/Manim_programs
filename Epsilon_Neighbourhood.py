from manim import *
from manim import XKCD
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080
config.background_color = XKCD.DARKBROWN

class c(Scene):
    def construct(self):
        text = Tex(
                       r"In topology, an \(\epsilon\)-neighborhood of a point $a$ is the set of all points that are at a distance less than \(\epsilon\) from $a$.\\",
                       r"Here we are working with the topology of $\mathbb{R}$, so the distance is given by the absolute value function.\\",
                       r"Hence the definition of \(\epsilon\)-neighborhood of a point $a \in \mathbb{R}$, $V_\epsilon(a)$, goes as follows:\\",
                       r"$V_\epsilon(a)$ := \{$x \in \mathbb{R}$ $|$ $|x-a|<\epsilon$\} = \{$x \in \mathbb{R}$ $|$ $a-\epsilon<x<a+\epsilon$\}",
                       font_size = 25,
                       color = WHITE,
                       tex_environment="flushleft"
        )
        Header = MathTex(r"{\epsilon}-neighborhoods", font_size = 60,color = BLUE)
        def f(char_index,c):
            text[0][char_index].set_color(c)
        text[0].next_to(Header,DOWN)
        
        
        f(35,RED)
        f(86,RED)
        vt = ValueTracker(0)
        epsilon = ValueTracker(0)
        nl = NumberLine(
            x_range=[-6,6],
            length=12,
            color = WHITE,
            include_numbers = True,
            label_direction = DOWN,
            tick_size = 0.05 
        ).set_color(WHITE)
        text[1].next_to(nl,3*UP)
        text[2:].next_to(nl,2*DOWN)
        pointer = nl.get_tick(vt.get_value(),size = 0.2).set_color(RED)
        ape = nl.get_tick(vt.get_value()+epsilon.get_value(),size = 0.2).add_updater(
            lambda m : m.move_to(
                nl.n2p(vt.get_value()+epsilon.get_value())
            )
        ).set_color(YELLOW)
        ame = nl.get_tick(vt.get_value()-epsilon.get_value(),size = 0.2).add_updater(
            lambda m : m.move_to(
                nl.n2p(vt.get_value()-epsilon.get_value())
            )
        ).set_color(YELLOW)
        label = MathTex("a",color = RED,font_size = 25).add_updater(lambda m: m.next_to(pointer,UP))
        set = MathTex(r"V_\epsilon(a)",font_size = 30,color = BLUE).add_updater(lambda m: m.next_to(pointer,1.5*DOWN))
        labelp = MathTex(r"a + \epsilon",font_size = 25,color = YELLOW).add_updater(lambda m: m.next_to(ape,0.5*(UP + RIGHT)))
        labeln = MathTex(r"a - \epsilon",font_size = 25,color = YELLOW).add_updater(lambda m: m.next_to(ame,0.5*(UP + LEFT)))
        pointer.add_updater(
            lambda m: m.move_to(
                nl.n2p(vt.get_value())
            )
        )

        def interval(a,p):
            highlight = Rectangle(width= abs(2*a), height = 0.3, stroke_width = 0, fill_color = BLUE, fill_opacity = 0.5).move_to(p)
            highlight.add_updater(
                lambda m : m.move_to(p)
            )
            return highlight
        
        
        highlighter = interval(epsilon.get_value(),pointer).add_updater(lambda m : m.become(interval(epsilon.get_value(),pointer)))
        def create_interval(val , eps, rtlabel = labelp, ltlabel = labeln):
            if(eps>=0.1):
                if(rtlabel not in self.moving_mobjects):
                    self.play(FadeIn(rtlabel,ltlabel),vt.animate.set_value(val),epsilon.animate.set_value(eps))
                else:
                    self.play(vt.animate.set_value(val),epsilon.animate.set_value(eps))
            else:
                 self.play(vt.animate.set_value(val),epsilon.animate.set_value(eps),FadeOut(rtlabel,ltlabel))
            self.wait(1)
        self.play(DrawBorderThenFill(Header))
        self.wait(1)
        self.play(Write(text[0]))
        self.wait(2)
        self.play(Header.animate.shift(UP*3),FadeOut(text[0]))
        self.play(FadeIn(nl),Write(text[1]))
        self.wait(3)
        self.play(Write(text[2]))
        self.wait(2)
        self.play(Write(text[3]),Create(pointer),Create(highlighter),FadeIn(label),FadeIn(set),FadeIn(ape,ame))
        create_interval(0,1.5)
        create_interval(-2,1.5)
        create_interval(-2,0)
        create_interval(1,1)
        self.wait(1)
    