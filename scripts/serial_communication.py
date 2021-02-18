#!/usr/bin/env python
import sys
import serial
import rospy
import traceback
from std_msgs.msg import String

serialPort = serial.Serial()

def main(nodeName, inputTopic, outputTopic, serialPortName, baudRate, encoding):
    serialPort.baudrate = baudRate
    serialPort.port = serialPortName
    serialPort.open()

    publisher = rospy.Publisher(outputTopic, String, queue_size=1)

    rospy.Subscriber(inputTopic, String, ProcessToicInput)
    rospy.init_node(nodeName)

    rospy.loginfo("node serial_communication started")

    rospy.loginfo("connected to port" + serialPortName)

    while not rospy.is_shutdown():
        if serialPort.in_waiting > 0:
            try:
                serialString = serialPort.readline().decode(encoding)
                publisher.publish(String(serialString))
            except Exception as e:
                rospy.logerr(traceback.format_exc())


def ProcessToicInput(data):
    serialPort.write(data.data.encode(encoding))


if __name__ == '__main__':
    try:
        if sys.argv.count() < 7 :
            rospy.logerr("Not enough arguments provided!")
        else:
            main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    except rospy.ROSInterruptException as e:
        rospy.logerr(e.msg)
        pass
