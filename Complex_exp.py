from manim import *
from manim.opengl import *



class new(Scene):

    def construct(self):
        ax = ComplexPlane().add_coordinates().set_opacity(0.25)
        point1 = Dot(ax.n2p(0.5),radius=0.05*DEFAULT_DOT_RADIUS,color=RED)
        point2 = Dot(ax.n2p(1),radius=0.05*DEFAULT_DOT_RADIUS,color=BLUE)
        circle1 =   Circle(
            radius=0.5,
            color=WHITE,
            stroke_opacity = 0.25,
            stroke_width = 1
            )

        circle2 = Circle(
            radius=0.5,
            color=WHITE,
            stroke_opacity = 0.25,
            stroke_width = 1 
            )
        
        def Circle2_update(mobj:Circle):
            mobj.move_to(point1.get_center())
        circle2.add_updater(Circle2_update)
        circle2.update()
        
        def rate_negative(x):
            return 1-x

        point2.move_to(circle2.get_start())

        vector1 = Arrow(start = ax.n2p(0),end = point1.get_center(),buff=0.01,color = RED,max_tip_length_to_length_ratio=0.2,
                        max_stroke_width_to_length_ratio=DEFAULT_STROKE_WIDTH)
        def vector1_update(mobj:Vector):
            mobj.put_start_and_end_on(start = vector1.get_start(),end = point1.get_center())
        vector1.add_updater(vector1_update)

        vector2 = Arrow(start = point1.get_center(),end = point2.get_center(),buff=0.01,color=BLUE,max_tip_length_to_length_ratio=0.2,
                        max_stroke_width_to_length_ratio=DEFAULT_STROKE_WIDTH/2)
        
        

        def vector2_update(mobj:Vector):
            mobj.put_start_and_end_on(start = vector1.get_end(),end = point2.get_center())
        vector2.add_updater(vector2_update)

        vector3 = Arrow(start = ax.n2p(0),
                        end = ax.n2p(1),
                        max_tip_length_to_length_ratio=0.1,
                        stroke_width=1,
                        buff= 0.01,
                        color = GREEN
                        )
        def vector3_update(mobj:Vector):
            mobj.put_start_and_end_on(start = ax.n2p(0),end = point2.get_center())
        vector3.add_updater(vector3_update)

        all_mobjects = VGroup(point1,point2,vector1,vector2,circle1,circle2)

        trace = TracedPath(vector2.get_end)
        all_mobjects_with_trace = VGroup(trace,point1,point2,vector1,vector2,circle1,circle2)
        self.play(Create(circle1),
                  FadeIn(vector1),
                  MoveAlongPath(point1,circle1,run_time=5,rate_func=linear)
                  )
        self.play(MoveAlongPath(point1,circle1,run_time=5,rate_func=linear),
                  FadeIn(circle2),
                  FadeIn(vector2),
                  MoveAlongPath(point2,circle2,run_time=5,rate_func=rate_negative),
                  )
        self.play(all_mobjects.animate.rotate(PI/2,about_point=ORIGIN))
        self.add(trace)
        self.play(
            MoveAlongPath(point1,circle1,run_time=5,rate_func=linear),
            MoveAlongPath(point2,circle2,run_time=5,rate_func=rate_negative),
            )
        trace.add_updater(
            lambda mobj,dt: mobj.shift(LEFT*dt)
        )
        self.play(
            MoveAlongPath(point1,circle1,run_time=5,rate_func=linear),
            MoveAlongPath(point2,circle2,run_time=5,rate_func=rate_negative),
            )
        self.play(
            MoveAlongPath(point1,circle1,run_time=5,rate_func=linear),
            MoveAlongPath(point2,circle2,run_time=5,rate_func=rate_negative),
            )
        
        pass