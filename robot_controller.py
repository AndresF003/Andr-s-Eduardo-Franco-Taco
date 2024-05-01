class RobotController:
    def __init__(self, robot_model, robot_view):
        self.robot_model = robot_model
        self.robot_view = robot_view

    def process_user_command(self):
        elevation, rotation, length = self.robot_view.get_user_input()
        self.robot_model.move_elevation(elevation)
        self.robot_model.move_rotation(rotation)
        self.robot_model.move_length(length)

    def run(self):
        while True:
            self.process_user_command()
            stop_movement = input("¿Desea detener el movimiento? (s/n): ")
            if stop_movement.lower() == "s":
                self.robot_model.stop_movement()
                break
