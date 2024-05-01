class RobotView:
    def __init__(self):
        pass

    def get_user_input(self):
        elevation = float(input("Ingrese la nueva elevación (0-100): "))
        rotation = float(input("Ingrese la nueva rotación (-180 a 180): "))
        length = float(input("Ingrese la nueva longitud (0-100): "))
        return elevation, rotation, length
