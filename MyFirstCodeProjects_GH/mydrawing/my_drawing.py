"""
File: my_drawing.py
Name: 陳名娟 Jenny Chen
----------------------
My favorite animal.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=500, height=400)

    ear = GPolygon()
    ear.add_vertex((120, 150))
    ear.add_vertex((130, 90))
    ear.add_vertex((180, 115))
    ear.color = 'black'
    ear.filled = True
    ear.fill_color = 'black'
    window.add(ear)

    ear_i = GPolygon()
    ear_i.add_vertex((130, 140))
    ear_i.add_vertex((135, 100))
    ear_i.add_vertex((175, 120))
    ear_i.color = 'pink'
    ear_i.filled = True
    ear_i.fill_color = 'pink'
    window.add(ear_i)

    ear2 = GPolygon()
    ear2.add_vertex((320, 115))
    ear2.add_vertex((370, 90))
    ear2.add_vertex((380, 150))
    ear2.color = 'black'
    ear2.filled = True
    ear2.fill_color = 'black'
    window.add(ear2)

    ear2_i = GPolygon()
    ear2_i.add_vertex((325, 120))
    ear2_i.add_vertex((365, 100))
    ear2_i.add_vertex((373, 145))
    ear2_i.color = 'pink'
    ear2_i.filled = True
    ear2_i.fill_color = 'pink'
    window.add(ear2_i)

    face = GOval(300, 200, x=100, y=100)
    face.fill_color = 'black'
    face.color = 'black'
    face.filled = True
    window.add(face)

    eye_o = GOval(40, 40, x=190, y=150)
    eye_o.fill_color = 'white'
    eye_o.color = 'white'
    eye_o.filled = True
    window.add(eye_o)

    eye = GOval(20, 20, x=195, y=155)
    eye.fill_color = 'yellowgreen'
    eye.color = 'yellowgreen'
    eye.filled = True
    window.add(eye)

    eye2_o = GOval(40, 40, x=275, y=150)
    eye2_o.fill_color = 'white'
    eye2_o.color = 'white'
    eye2_o.filled = True
    window.add(eye2_o)

    eye2 = GOval(20, 20, x=280, y=155)
    eye2.fill_color = 'yellowgreen'
    eye2.color = 'yellowgreen'
    eye2.filled = True
    window.add(eye2)

    nose = GOval(10, 10, x=245, y=210)
    nose.fill_color = 'pink'
    nose.color = 'pink'
    nose.filled = True
    window.add(nose)

    one = GArc(15, 15, 0, -180, x=255, y=215)
    one.color = 'white'
    window.add(one)

    one2 = GArc(15, 15, 0, -180, x=230, y=215)
    one2.color = 'white'
    window.add(one2)

    line1 = GLine(145, 200, 180, 205)
    line1.color = 'white'
    window.add(line1)

    line2 = GLine(145, 210, 180, 215)
    line2.color = 'white'
    window.add(line2)

    line3 = GLine(145, 220, 180, 225)
    line3.color = 'white'
    window.add(line3)

    line4 = GLine(325, 205, 360, 200)
    line4.color = 'white'
    window.add(line4)

    line5 = GLine(325, 215, 360, 210)
    line5.color = 'white'
    window.add(line5)

    line6 = GLine(325, 225, 360, 220)
    line6.color = 'white'
    window.add(line6)

    label = GLabel('Meow ~ <3')
    window.add(label, x=400, y=300)


if __name__ == '__main__':
    main()
