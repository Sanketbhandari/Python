import math
def number_of_cans(wall_height, wall_width, coverage_per_can):
    cans_required = (wall_height * wall_width)/coverage_per_can
    print(f"Cans required will be {math.ceil(cans_required)}")

height= int(input("Height of wall: "))
width= int(input("Width of wall: "))
number_of_cans(wall_height=height,wall_width=width,coverage_per_can=5)