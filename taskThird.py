class Point:
    """Методы для инициализации координат точки, вычисления расстояния до другой точки, а также для получения и
    изменения координат."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def new_value_for_start_coordinate(self, new_value_x, new_value_y):
        self.x = new_value_x
        self.y = new_value_y
        return f"Вы успешно установили новые координаты точки на: \n x = {self.x} \n y = {self.y} "

    def take_coordinate(self):
        point_coord = (self.x, self.y)
        return point_coord

    def distance_to_another_point(self, new_x, new_y):
        new_point = (new_x, new_y)
        point_coord = self.take_coordinate()
        x = point_coord[0] - new_point[0]
        y = point_coord[1] - new_point[1]
        return f"Расстояние по x = {x}, Расстояние по y = {y}"


point = Point(0, 0)

print(f"Начальные координаты: \n {point.take_coordinate()}")

print(point.new_value_for_start_coordinate(3, 4))


print(f"Измененные координаты: \n {point.take_coordinate()}")


print(f"Расстояние до следующей точки: \n {point.distance_to_another_point(2, 4)}")
