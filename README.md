# scancontext-pybind

## News 
- Currently (Apr. 2022), not a set of full features are made yet. For checking the features currently supported, see `wrapper.cpp`.

## Purpose
- Goal of this repo is 
  - For fast python support for lidar-based place recognition 
    - ps. the native python version (see https://github.com/gisbi-kim/PyICP-SLAM) was already supported, but it was slow.  
  - Original C++ code: see https://github.com/irapkaist/scancontext

## Build
- Please ensure eigen3 is installed (e.g., via `sudo apt install libeigen3-dev`)
- Other dependencies (nanoflann and pybind11) are downloaded automatically (for details, see `CMakeLists.txt`)
- Use the following commands to build:
  ```
   $ mkdir build
   $ cd build
   $ cmake ..
   $ make
  ```
- CMake doesn’t detect the right Python version
The CMake-based build system will try to automatically detect the installed version of Python and link against that. When this fails, or when there are multiple versions of Python and it finds the wrong one, delete CMakeCache.txt and then add -DPYTHON_EXECUTABLE=$(which python) to your CMake configure line. (Replace $(which python) with a path to python if your prefer.)

You can alternatively try -DPYBIND11_FINDPYTHON=ON, which will activate the new CMake FindPython support instead of pybind11’s custom search. Requires CMake 3.12+, and 3.15+ or 3.18.2+ are even better. You can set this in your CMakeLists.txt before adding or finding pybind11, as well.



- Install the Python package via `pip` with
  ```
  $ cd build
  $ make pip-install
  # or install manually with
  $ cd build/python
  $ pip install .
  ```

## Use examples  
- For the hands-on exploration of the supported features, for example (you need `numpy` and `open3d`),
  ```
   $ python3 examples/test_make_desciptor.py
   $ python3 examples/test_compare_scd.py
   $ # to be added ...
  ```

## Docker support 
- see `docker/docker_run.sh`. Modify the REPOSITORY_PATH with your own path.
  - For the docker-based test tutorial, see this [video (TBA)](TBA)

## Application: PyICP-SLAM2
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
