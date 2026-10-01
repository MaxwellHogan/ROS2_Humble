import cv2
import rclpy

from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image


class WebcamPublisher(Node):

    def __init__(self):
        super().__init__("webcam_publisher")

        self.publisher = self.create_publisher(
            Image,
            "/camera/image_raw",
            10
        )

        self.bridge = CvBridge()

        self.camera = cv2.VideoCapture(
            "http://host.docker.internal:8080/video"
        )

        if not self.camera.isOpened():
            self.get_logger().error(
                "Unable to connect to webcam stream"
            )
        else:
            self.get_logger().info(
                "Connected to webcam stream"
            )

        self.timer = self.create_timer(
            1.0 / 30.0,
            self.publish_frame
        )

    def publish_frame(self):

        success, frame = self.camera.read()

        if not success:
            self.get_logger().warning(
                "Failed to read webcam frame"
            )
            return

        msg = self.bridge.cv2_to_imgmsg(
            frame,
            encoding="bgr8"
        )

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "camera"

        self.publisher.publish(msg)

    def destroy_node(self):
        self.camera.release()
        super().destroy_node()


def main(args=None):

    rclpy.init(args=args)

    node = WebcamPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()