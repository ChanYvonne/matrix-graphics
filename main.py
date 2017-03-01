from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 0, 255 ]
matrix = new_matrix()

print "To show add_edge works: points (0,0) to (10,10)"
add_edge(matrix, 0, 0, 0, 10, 10, 0)
print_matrix(matrix)

print "To show matrix multiplication works:"
matrix = new_matrix()
m = new_matrix()
add_edge(matrix, random.randint(0,9), random.randint(0,9), 0, random.randint(0,9), random.randint(0,9), 0)
add_edge(matrix, random.randint(0,9), random.randint(0,9), 0, random.randint(0,9), random.randint(0,9), 0)
add_edge(matrix, random.randint(0,9), random.randint(0,9), 0, random.randint(0,9), random.randint(0,9), 0)
add_edge(matrix, random.randint(0,9), random.randint(0,9), 0, random.randint(0,9), random.randint(0,9), 0)
add_edge(m, random.randint(0,9), random.randint(0,9), 0, random.randint(0,9), random.randint(0,9), 0)
add_edge(m, random.randint(0,9), random.randint(0,9), 0, random.randint(0,9), random.randint(0,9), 0)
add_edge(m, random.randint(0,9), random.randint(0,9), 0, random.randint(0,9), random.randint(0,9), 0)
add_edge(m, random.randint(0,9), random.randint(0,9), 0, random.randint(0,9), random.randint(0,9), 0)
print "m1:"
print_matrix(matrix)
print "m2:"
print_matrix(m)
print "m1*m2:"
print_matrix(matrix_mult(matrix,m))

m1 = new_matrix()
m2 = new_matrix()
m3 = new_matrix()
m4 = new_matrix()

add_edge(m1, XRES/2-50, YRES/2, 1.0, XRES/2, YRES/2-50, 1.0)
add_edge(m2, XRES/2, YRES/2-50, 1.0, XRES/2+50, YRES/2, 1.0)
add_edge(m3, XRES/2, YRES/2+50, 1.0, XRES/2+50, YRES/2, 1.0)
add_edge(m4, XRES/2-50, YRES/2, 1.0, XRES/2, YRES/2+50, 1.0)

color = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
draw_lines( m1, screen, color )
color = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
draw_lines( m2, screen, color )
color = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
draw_lines( m3, screen, color )
color = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
draw_lines( m4, screen, color )
save_ppm(screen, "pic.ppm")
