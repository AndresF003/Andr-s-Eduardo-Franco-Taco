from robot_model import RobotModel
from robot_view import RobotView
from robot_controller import RobotController
robot_model = RobotModel()
robot_view = RobotView()
robot_controller = RobotController(robot_model, robot_view)
robot_controller.run()
