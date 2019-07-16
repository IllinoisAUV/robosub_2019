#! /bin/bash

# Launch mavros script
# roslaunch robosub_2019 mavros.launch &

# Launch either joystick or autonomous control

if [[ $1 == "--joy" ]];
then
  echo "joy";
else
  echo "Launch auto control file";
fi

trap 'kill $BGPID; exit' SIGINT SIGTERM

wait
