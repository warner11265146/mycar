from donkeycar.parts.controller import LocalWebController, JoystickController, WebFpv,JoyStickPub

import os
import time
import numpy

joystick_message = JoyStickPub()
while True:
  time_data = int(time.time())
  message_data=joystick_message.run()
  print("message_data=",message_data)
