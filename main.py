import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def is_point_inside_my_circle_part(x_position, y_position):
    y = np.sqrt(1 - np.power(x_position, 2))
    return y_position <= y


class Point:

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.is_inside_circle_part = is_point_inside_my_circle_part(x_position=x_position, y_position=y_position)

    def __str__(self) -> str:
        return str(self.x_position) + ", " + str(self.y_position) + ", " + str(self.is_inside_circle_part)


all_hits_list = [50, 100, 200, 500, 800, 1000, 1500, 2125, 3000, 5000, 7000, 9250, 10000, 20000, 25000, 30000, 40000]

hits_ratios_list = []

for j in range(0, len(all_hits_list)):
    points = []
    for i in range(0, all_hits_list[j]):
        point_x_position = round(random.uniform(0, 1), 2)
        point_y_position = round(random.uniform(0, 1), 2)
        points.append(Point(point_x_position, point_y_position))

    x_points_positions = []
    y_points_positions = []
    hits_inside_ellipse = 0

    for point in points:
        if point.is_inside_circle_part:
            hits_inside_ellipse += 1
        x_points_positions.append(point.x_position)
        y_points_positions.append(point.y_position)

    plt.figure(j)
    a = plt.subplot(111, aspect='equal')
    ellipse = Ellipse((0, 0), 2, 2, 0, fill=False)
    ellipse.set_clip_box(a.bbox)
    plt.ylim(0, 1)
    a.add_artist(ellipse)
    plt.scatter(x_points_positions, y_points_positions)
    plt.title(str(all_hits_list[j]) + " random hits")
    hits_ratios_list.append(4 * hits_inside_ellipse / (all_hits_list[j]))
    print(str(hits_inside_ellipse / (all_hits_list[j])),
          str(hits_inside_ellipse))
    plt.xlim(0, 1)
    plt.ylim(0, 1.1)
    plt.savefig(str(all_hits_list[j]) + "_random hits" + '.png')

plt.figure(len(all_hits_list) + 1)
plt.hlines(y=np.pi, xmin=all_hits_list[0], xmax=all_hits_list[-1], color='r', label="pi value")
plt.scatter(all_hits_list, hits_ratios_list)
plt.title("Hits ratios versus amount of hits")
plt.xlim(all_hits_list[0], all_hits_list[-1])
plt.xlabel("Hits amount")
plt.ylabel("Hits ratio (hits inside ellipse / all other hits)")
plt.legend()
plt.savefig("Hits_ratios_versus_amount_of_hits.png")
plt.show()
