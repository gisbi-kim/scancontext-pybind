# scancontext-pybind

## News 
- Currently (Apr. 2022), not a set of full features are made yet. For checking the features currently supported, see `wrapper.cpp`.

## Purpose
- Goal of this repo is 
  - For fast python support for lidar-based place recognition 
    - ps. the native python version (see https://github.com/gisbi-kim/PyICP-SLAM) was already supported, but it was slow.  
  - Original C++ code: see https://github.com/irapkaist/scancontext

## Build 
- Dependency: eigen, nanoflann, and pybind11 (for details, see CMakeLists.txt)
  - ps. this [KCP](https://github.com/StephLin/KCP) repo kindly explains how to install them.  
- for the build, follow these lines,  
  ```
   $ mkdir build
   $ cd build
   $ cmake ..
   $ make
  ```
- NOTE: You also need to add path before the use. 
  ```
   $  export PYTHONPATH=$PYTHONPATH:{YOUR_PATH}/build/python
  ```

## Use examples  
- For the hands-on exploration of the supported features, for example (you need `numpy` and `open3d`),
  ```
   $ python3 tests/test_make_desciptor.py
  ```

## Docker support 
- see `docker/docker_run.sh`. Modify {YOUR_PATH} to the your path.
- For the docker-based test tutorial, see this [video (TBA)](TBA)

## Applications 
### PyICP-SLAM2 
- TBA ... 


## Cite
```
  @ARTICLE { gskim-2021-tro,
      AUTHOR = { Giseop Kim and Sunwook Choi and Ayoung Kim },
      TITLE = { Scan Context++: Structural Place Recognition Robust to Rotation and Lateral Variations in Urban Environments },
      JOURNAL = { IEEE Transactions on Robotics },
      YEAR = { 2021 }
  }

  @INPROCEEDINGS { gkim-2018-iros,
    author = {Kim, Giseop and Kim, Ayoung},
    title = { Scan Context: Egocentric Spatial Descriptor for Place Recognition within {3D} Point Cloud Map },
    booktitle = { Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems },
    year = { 2018 },
    month = { Oct. },
    address = { Madrid }
  }
```
## Ack 
- Thanks to the author of [KCP](https://github.com/StephLin/KCP). The pybind wrapper src and the directory structures were borrowed from [KCP](https://github.com/StephLin/KCP).
