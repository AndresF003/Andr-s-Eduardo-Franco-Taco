class RobotModel:
    def __init__(self):
        self.elevation = 0
        self.rotation = 0
        self.length = 0
        self.is_moving = False

    def move_elevation(self, new_elevation):
        if new_elevation >= 0 and new_elevation <= 100:
            self.elevation = new_elevation
            print(f"Elevación del robot actualizada a: {self.elevation}")
        else:
            print("Valor de elevación no válido. Debe estar entre 0 y 100.")

    def move_rotation(self, new_rotation):
        if -180 <= new_rotation <= 180:
            self.rotation = new_rotation
            print(f"Rotación del robot actualizada a: {self.rotation}")
        else:
            print("Valor de rotación no válido. Debe estar entre -180 y 180.")

    def move_length(self, new_length):
        if new_length >= 0 and new_length <= 100:
            self.length = new_length
            print(f"Longitud del robot actualizada a: {self.length}")
        else:
            print("Valor de longitud no válido. Debe estar entre 0 y 100.")

    def stop_movement(self):
        self.is_moving = False
        print("Movimiento del robot detenido.")

class RobotController:
    def __init__(self, robot_model, robot_view):
        self.robot_model = robot_model
        self.robot_view = robot_view

    def process_user_command(self):
        elevation, rotation, length = self.robot_view.get_user_input()
        self.previous_elevation = self.robot_model.elevation
        self.previous_rotation = self.robot_model.rotation
        self.previous_length = self.robot_model.length
        self.robot_model.move_elevation(elevation)
        self.robot_model.move_rotation(rotation)
        self.robot_model.move_length(length)

    def run(self):
        while True:
            self.process_user_command()
            self.robot_view.display_robot_status(self.robot_model.elevation, self.robot_model.rotation, self.robot_model.length)
            stop_movement = input("¿Desea detener el movimiento? (s/n): ")
            if stop_movement.lower() == "s":
                self.robot_model.stop_movement()
                break
            use_previous_values = input("¿Desea usar los valores del movimiento anterior? (s/n): ")
            if use_previous_values.lower() == "s":
                self.robot_model.move_elevation(self.previous_elevation)
                self.robot_model.move_rotation(self.previous_rotation)
                self.robot_model.move_length(self.previous_length)
