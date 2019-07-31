#! /bin/bash

# Make sure Port is accessible by mavros
sudo chmod 777 /dev/ttyACM0

# Initialize roscore
roscore &

# Launch mavros script
roslaunch robosub_2019 mavros.launch &

# Launch either joystick or autonomous control

# Launch the state machine
rosrun robosub_2019 state_machine.py &

# Launch RC Override node
rosrun robosub_2019 mavrosrc.py &

trap 'kill $BGPID; killall rosmaster; killall roscore; exit' SIGINT SIGTERM

wait
