"""
Program to generate arg labels with point coordinates for launch file.
"""

arg_pn = "<arg name=\"pN\" value=\"{x: XX.0, y: YY.0, z: 0.0}\"/>"

points = ((2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
          (7, 2), (7, 3), (6, 4), (6, 5), (7, 6),
          (8, 6), (9, 7), (9, 8), (8, 9), (7, 9),
          (6, 8), (6, 7), (5, 6), (5, 5), (5, 4),
          (4, 3), (3, 3), (2, 4), (2, 5), (3, 6),
          (4, 6), (5, 7), (5, 8), (4, 9), (3, 9),
          (2, 8), (1, 7), (1, 6), (1, 5), (1, 4),
          (1, 3), (1, 2), (2, 1))

pts = ""
for pxy in range(len(points)):
    x, y = points[pxy]
    pn = 'p' + str(pxy + 1)
    arg = arg_pn.replace("pN", pn).replace("XX", str(x)).replace("YY", str(y))
    pts += ("$(arg " + pn + "),")
    print(arg)

arg_pts = "<arg name=\"pts\" value=\"points: [points]\"/>"
arg_pts = arg_pts.replace("[points]", '[' + pts[0:-1] + ']')
print(arg_pts)

# End of Code
