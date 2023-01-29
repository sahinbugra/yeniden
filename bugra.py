import rospy
from geometry_msgs.msg import Twist
from deneme.msg import bugra

def callback(veri):
    global anlik_konum
    anlik_konum = veri

def hareket():
    rospy.init_node('turtle_controller')

    hiz_publisher = rospy.Publisher('/turtle1/cmd_hiz', Twist, queue_size=10)

    rospy.Subscriber('/turtle1/bugra', bugra, callback)

    rate = rospy.Rate(10)

    hiz_msg = Twist()

    hiz_msg.linear.x = 1.0
    hiz_msg.angular.z = 0.5

    while not rospy.is_shutdown():
        hiz_msg.linear.x = anlik_konum.x + anlik_konum.theta
        hiz_msg.angular.z = anlik_konum.theta

        hiz_publisher.publish(hiz_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        hareket()
    except rospy.ROSInterruptException:
        pass
