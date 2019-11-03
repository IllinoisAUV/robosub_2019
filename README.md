# About

All the code that runs in the submarine.



# Dev Environment Setup

### Ros Setup

Go to ROS' website or use the following commands:

``` bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full
```

Then get dependencies

``` bash
rosdep update
```

Set up your environment variables

``` bash
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
source /opt/ros/melodic/setup.bash
```

Install python tools

``` bash
sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
```

### Catkin Workspace

Make a directory for the project

```bash
mkdir sigbot
cd sigbot/
```

Install catkin tools

``` bash
sudo apt install python-catkin-tools
```

Internalize the workspace

``` bash
catkin_init_workspace
```

### Creating a src directory for the repositories

Make a src folder

``` bash
mkdir src
cd src
```

Clone all the necessary repositories 

* Make sure to use SSH to make your life easier

```bash
git clone git@github.com:IllinoisAUV/robosub_2019.git
git clone git@github.com:IllinoisAUV/uuv_simulator.git
git clone git@github.com:IllinoisAUV/darknet_ros.git
git clone git@github.com:IllinoisAUV/zed-ros-wrapper.git
git clone git@github.com:IllinoisAUV/ardupilot.git
```

### Miscellaneous Dependencies

Gazebo

``` bash
sudo apt install gazebo9
```

Nvidia - Make sure to install version 10.0, which can be found [here](https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804).

Mavros

``` bash
sudo apt install ros-melodic-mavros
sudo apt install ros-melodic-mavros-extras
```

ZED SDK

- Go to [ZED's website](https://www.stereolabs.com/developers/release/#sdkdownloads_anchor) and follow their installation instructions

### Building

Build using:

- Use -jx where x is the number of threads you want to run on
- Do this in the main sigbot directory

```bash
catkin build -j4
```

Run local setup (You should add this to your `~/.bashrc`)

```bash
source ~/sigbot/devel/setup.bash
```



# Usage

### Run simulator with manual controls
```bash
rosrun robosub_2019 start_sim.sh
```

See a list of the current topics

```bash
rostopic list
```

To publish topics, use `rostopic pub`

```bash
rostopic pub /rexrov/cmd_vel geometry_msgs/Twist "linear:
  x: 1.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0" 
```



### Run simulation with code as controls
```bash
rosrun robosub_2019 state_machine.py --sim
```



### See a graph of everything that is happening
```bash
rqt_graph
```

### Development Notes

state_machine.py has a ton of code for both turning and states. Ideally it would just use states.
We use controller overrides to control the robot. 