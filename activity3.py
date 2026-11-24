# Programmed By: █████
# Date Programmed: 9/25/2024
# Date Submitted: 9/25/2024
# Activity Title: Activity 3 - Operators

print("GETTING THE PERIMETER OF DIFFERENT SHAPES\n")

radius = 10
tri_a, tri_b, tri_c = 28, 10, 30
square_x = 27
rect_length, rect_width = 15, 24
quad_a, quad_b, quad_c, quad_d = 14, 25, 19, 38

text_circle = "radius = " + str(radius)
text_triangle = "a = " + str(tri_a)
text_triangle += ", b = " + str(tri_b)
text_triangle += ", c = " + str(tri_c)
text_square = "x = " + str(square_x)
text_rectangle = "length = " + str(rect_length)
text_rectangle += "width = " + str(rect_width)
text_quadrilateral = "a = " + str(quad_a)
text_quadrilateral += ", b = " + str(quad_b)
text_quadrilateral += ", c = " + str(quad_c)

print("Given values (cm):")
print("\tCircle:\t\t", text_circle )
print("\tTriangle:\t", text_triangle)
print("\tSquare:\t\t", text_square)
print("\tRectangle:\t", text_rectangle)
print("\tQuadrilateral:\t", text_quadrilateral)

print()
print("CIRCUMFERENCE:\t", str(2 * 3.1416 * radius) + "cm")
print("TRIANGLE:\t", str(tri_a + tri_b + tri_c) + "cm")
print("SQUARE:\t\t", str(4 * square_x) + "cm")
print("RECTANGLE:\t", str((2 * rect_length) + (2 * rect_width)) + "cm")
print("QUADRILATERAL:\t", str(quad_a + quad_b + quad_c + quad_d)+ "cm")
