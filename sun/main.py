import rclpy
from . import lamp
from rclpy.node import Node
from std_msgs.msg import String

SUN_RISE = 'sun-rise'
SUN_SET = 'sun-set'

class Sun(Node):

    def __init__(self):
        super().__init__('sun')
        self.lamp = lamp.Lamp()
        self.subscription = self.create_subscription(
            String,
            'day',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):

        self.get_logger().info('Getting: "%s"' % msg.data)
        if msg.data == SUN_RISE:
            self.lamp.light()
        elif msg.data == SUN_SET:
            self.lamp.dark()
        else:
            self.get_logger().error('Unknown day topic event "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    sun_subscriber = Sun()

    rclpy.spin(sun_subscriber)

    sun_subscriber.sun.shutdown()
    sun_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()