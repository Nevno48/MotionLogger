Paste the folder of code in the /home/pi/Desktop directory.
This program currently uses a bash command "MotionLogger" to 
execute python scripts.
The user can take a time lapse of pictures or videos in seconds.
To add the command MotionLogger, use the following commands:
1. "sudo nano /usr/local/bin/MotionLogger"
2. in the file type:
!/bin/bash
python3 /home/pi/Desktop/pyCameraMotion/motionLogger.py
3. "sudo chmod 755 /usr/local/bin/MotionLogger"


