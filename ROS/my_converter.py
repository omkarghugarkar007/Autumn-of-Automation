import roslib
import numpy as np

roslib.load_manifest('beginner_tutorials')

from beginner_tutorials.msg import quat
from beginner_tutorials.msg import rollpitchyaw

def callback(data):
	x = data.x
	y = data.y
	z = data.z
	w = data.w

	sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x**2 + y**2)
    roll = np.arctan2(sinr_cosp, cosr_cosp)

    sinp = 2 * (w * y - z * x)
    pitch = np.where(np.abs(sinp) >= 1,
                     np.sign(sinp) * np.pi / 2,
                     np.arcsin(sinp))

    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y**2 + z**2)
    yaw = np.arctan2(siny_cosp, cosy_cosp)

	pub = rospy.Publisher('topic2', rollpitchyaw)
	
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
        
    	msg = rollpitchyaw()
        
    	msg.roll = roll
    	msg.pitch = pitch
    	msg.yaw = yaw

    	pub.publish(msg)
    	rate.sleep()

    	rospy.loginfo(rospy.get_name() + " roll =  %s", roll)
    	rospy.loginfo(rospy.get_name() + " pitch = %s", pitch)
    	rospy.loginfo(rospy.get_name() + " yaw = %s", yaw)

def listener():
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber('topic1',quat,callback)

	rospy.spin()

if __name__ == '__main__':
    
    listener()



