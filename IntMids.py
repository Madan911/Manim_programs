from manim import *

config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080

class problem(Scene):
    def construct(self):
        text1 = Tex(r"Consider 5 distinct points in the xy-plane with positive integer co-ordinates.\\Prove that there is atleast one pair of points whose midpoint of the line\\joining them has integer co-ordinates.",font_size =21,tex_environment="flushleft")
        
        npl = NumberPlane(
            x_length = 6,
            y_length = 6,
            x_range = [0,12.01],
            y_range = [0,12.01],
            axis_config = {
                "include_tip":True,
                "tip_width":0.05,
                "tip_height":0.05
            }
        )
        text1.shift(4*LEFT+2*UP)

        npl.shift(4*RIGHT)
        dots = VGroup(
            *[
                Dot(point=npl.c2p(8,2,0),radius=0.05,color= YELLOW),
                Dot(point=npl.c2p(11,12,0),radius=0.05,color= YELLOW),
                Dot(point=npl.c2p(2,9,0),radius=0.05,color= YELLOW),
                Dot(point=npl.c2p(6,9,0),radius=0.05,color= YELLOW),
                Dot(point=npl.c2p(10,3,0),radius=0.05,color= YELLOW)
                ]
        )
        
        L =[]
        for i in range(5):
            for j in range(i,5):
                if(i == j):
                    continue
                else:
                    line = Line(
                        start=dots[i].get_center(),
                        end=dots[j].get_center(),
                        color = YELLOW,
                        stroke_width = 2
                    )
                    L.append(line)
        lines = VGroup(*L)
        self.play(FadeIn(npl))
        self.play(Write(text1[0][:68]),Create(dots),run_time = 2)
        M = []
        self.play(Write(text1[0][68:]),run_time = 2)
        for i in range(10):
            dots.z_index=2
            lines.z_index=-1
            self.play(Create(lines[i]),run_time = 0.5)
            c = np.around(npl.p2c(lines[i].get_center()),2)
            print(c[0],c[1])
            mp = Dot(lines[i].get_center(),color = BLUE,radius = 0.04)
            M.append(mp)
            mp.z_index=1
            self.play((Create(mp)),run_time = 0.5)
            if(c[0].is_integer()==False or c[1].is_integer()==False):
                self.play(LaggedStart(
                    mp.animate.set_color(RED),
                    lines[i].animate.set_color(RED),
                    lag_ratio = 0.1,
                    run_time = 0.3
                    )
                    )
            else:
                self.play(LaggedStart(
                    lines[i].animate.set_color(GREEN),
                    mp.animate.set_color(GREEN),
                    Flash(mp,line_stroke_width=1,line_length=0.1,num_lines=15,run_time=0.5,rate_func = smooth),
                    lag_ratio = 0.1
                ))
        self.wait()
        midpoints = VGroup(*M)

        self.play(FadeOut(text1),FadeOut(dots),FadeOut(lines),FadeOut(midpoints))
        self.play(npl.animate.shift(4*LEFT+2*UP).scale(0.75))

        text = Tex(
                r"Consider two points $(x_i,y_i)$ and  $(x_j,y_j)$,then their mid point is ($x_i+x_j \over 2$,$y_i+y_j \over 2$).\\",
                r"For the co-ordinates to be integers, both $x_i + x_j$ , $y_i + y_j$ must be even.\\",
                r"This only happens when $x_i$ and $x_j$ share the same parity, same for $y_i$ and $y_j$.\\",
                r"For a point there are only four possibilities: (odd,odd), (even,odd), (odd,even), (even,even).\\",
                r"Since we choose 5 distinct points and only 4 possible parities, there must be atleast 1 pair of points which share the same parity.",
                font_size = 30,
                tex_environment="flushleft",
                tex_to_color_map={"odd":RED,"even":BLUE,"parity":GREEN,"parities":GREEN},
                )
        new_points = VGroup(*[Dot(point=npl.c2p(3,10,0),radius=0.04,color = YELLOW),Dot(point=npl.c2p(7,2,0),radius=0.04,color = YELLOW)])
        new_line = Line(
            start = new_points[0].get_center(),
            end = new_points[1].get_center(),
            stroke_width = 2,
            color = YELLOW
        )
        dashedL = []
        for i in range(2):
            q = new_points[i].get_center()
            hline1 = npl.get_horizontal_line(q,line_func = DashedLine,color = YELLOW,stroke_width = 1.7)
            vline1 = npl.get_vertical_line(q,line_func = DashedLine,color = YELLOW,stroke_width = 1.7)
            dashedL.append(vline1)
            dashedL.append(hline1)
        dashedLwlabel = []
        for i in range(4):
            e = MathTex(r"even",color = BLUE,font_size = 20)
            o = MathTex(r"odd",color = RED,font_size = 20)
            if(i%2==0):
                v = VGroup(dashedL[i],e.next_to(dashedL[i],1/5*LEFT))
            else:
                v = VGroup(dashedL[i],o.next_to(dashedL[i],1/5*UP))
            dashedLwlabel.append(v)

        new_mp = Dot(new_line.get_center(),color = RED,radius=0.04)
        mpv = npl.get_vertical_line(new_mp.get_center(),line_func = DashedLine,color = RED,stroke_width = 3)
        mph = npl.get_horizontal_line(new_mp.get_center(),line_func = DashedLine,color = RED,stroke_width = 3)
        MID = VGroup(mpv,mph)
        hlinemp = npl.get_horizontal_line(new_mp.get_center(),line_func = DashedLine,color = RED,stroke_width = 1.7)
        vlinemp = npl.get_vertical_line(new_mp.get_center(),line_func = DashedLine,color = RED,stroke_width = 1.7)
        text[0][54:71].set_color(YELLOW)
        text.next_to(npl,DOWN)
        self.play(Create(text[0]),Create(new_points),Create(new_line))
        self.play(Circumscribe(text[0][54:72],color = RED),Create(new_mp),run_time=1)
        self.wait(1)
        self.play(Create(text[1:4]),run_time = 2)
        self.wait(1)
        self.play(Create(text[4:7]),run_time = 2)
        self.wait(2)
        self.play(FadeIn(VGroup(*dashedLwlabel)),run_time = 1)
        self.wait(2)
        self.play(Transform(VGroup(*dashedLwlabel),MID))
        self.wait(2)
        self.play(Create(text[7:29]),run_time=3)
        self.wait(3)
        self.play(FadeOut(VGroup(*dashedLwlabel)),FadeOut(new_points),FadeOut(new_mp),FadeOut(npl),FadeOut(text),FadeOut(new_line))
        