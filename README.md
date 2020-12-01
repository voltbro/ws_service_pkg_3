### Installation

```
cd ~/ros_catkin_ws/src/
git clone https://github.com/voltbro/ws_service_pkg_3.git
```

### Compilation

```
cd ~/ros_catkin_ws/
sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/melodic --pkg=ws_service_pkg_3
```


### Usage  

Just run configure.launch
  
```
roslaunch ws_service_pkg_3 configure.launch
```
