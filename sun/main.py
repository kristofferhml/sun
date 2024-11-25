import rclpy
import os
from . import lamp
from rclpy.node import Node
from std_msgs.msg import String

DAY = 'day'
NIGHT = 'night'
PIN = int(os.getenv('PIN',14))

class Sun(Node):

    def __init__(self):
        super().__init__('sun')
        self.lamp = lamp.Lamp(PIN)
        self.subscription = self.create_subscription(
            String,
            'day',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):

        self.get_logger().info('Getting: "%s"' % msg.data)
        
        if msg.data == DAY:
            self.lamp.light()
        
        elif msg.data == NIGHT:
            self.lamp.dark()

def main(args=None):
    rclpy.init(args=args)

    sun_subscriber = Sun()

    rclpy.spin(sun_subscriber)

    sun_subscriber.sun.shutdown()
    sun_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()