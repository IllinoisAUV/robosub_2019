#! /bin/bash

set -x

path_to_dir="~/ros/auv/src/robosub_2019"

source echo $path_to_dir/devel/setup.bash

roslaunch robosub_2019 start_simulation.launch &

sleep 5

roslaunch robosub_2019 start_thrusters.launch &

wait
