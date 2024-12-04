from manim import *

'''
This is an example for how Circles, Lines and Vectors may be animated:


class createCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class createLine(Scene):
    def construct(self):
        line = Line()  # create a line
        line.set_fill(PINK, opacity=0.5) # set the color and transperency
        self.play(Create(line))  # show the line on screen

class createVector(Scene):
    def construct(self):
        vector = Vector()
        self.play(Create(vector))

These following examples showcase how you can use manim classes to your advantage:


'''

'''
What to implement next:

- better labels (on the tip of the vector + move accordingly)
- show resulting vector
'''

class Vectors(VectorScene):
    def construct(self):

        plane = self.add_plane(animate=True).add_coordinates() # Koordinatensystem mit Achsen zeichnen
        vector1 = self.add_vector([3,0], color = YELLOW) # Vektor 1 zeichnen
        # coordsVec1Label = self.get_vector_label(vector1, label=MathTex("+3"),at_tip=True, direction=UP)
        # self.add(coordsVec1Label)
        # self.write_vector_coordinates(vector= vector1)

        self.wait(0.5)

        # Nur die x-Komponente von vector2 für die Beschriftung extrahieren und darstellen
        xVec1 = vector1.get_end()[0]  # x-Komponente des Vektors
        vec1Label = MathTex(f"{xVec1:.2f}")  # Label nur für die x-Komponente
        vec1Label.next_to(vector1, UP)  # Beschriftung initial über vector2 setzen
        self.add(vec1Label)

        self.wait(0.5)


        # Zielposition (Spitze des ersten Vektors)
        target_position = vector1.get_end()

        # basis = self.get_basis_vectors() # Basisvektoren berechnen
        # self.add(basis) # Basisvektoren zeichnen

        # self.vector_to_coords(vector = vector) # Vektorkoordinaten zeichnen

        vector2 = self.add_vector([-2,0], color= GREEN) # neuen Vektor zeichnen
        # coordsVec2Label = self.get_vector_label(vector2, label=MathTex("-2"),at_tip=True, direction=UP)
        # self.add(coordsVec2Label)
        # self.write_vector_coordinates(vector= vector2) # die Koordinate von welchem Vektor

        self.wait(0.5)

        
        # Nur die x-Komponente von vector2 für die Beschriftung extrahieren und darstellen
        xVec2 = vector2.get_end()[0]  # x-Komponente des Vektors
        vec2Label = MathTex(f"{xVec2:.2f}")  # Label nur für die x-Komponente
        vec2Label.next_to(vector2, UP)  # Beschriftung initial über vector2 setzen
        # self.add(vec2Label)
        
        # Vektor und Label zur neuen Position animieren
        self.play(
            Transform(vector2, vector2.copy().shift(target_position - vector2.get_start()))
        )

        # self.add(vec2Label)

        # self.play(
        #     Transform(vec2Label, vec2Label.animate.move_to(vector2.get_end() + UP * 0.3))
        # )

        self.wait(2)