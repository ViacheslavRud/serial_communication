#!/usr/bin/env python
import serial_communication

serial_communication.main("gripper_serial_communication", "/gripper/serial/input", "gripper/serial/output", "/dev/ttyACM0", 9600, "Ascii")