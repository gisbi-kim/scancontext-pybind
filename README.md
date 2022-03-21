# scancontext-pybind
- Goal of this repo: 
  - For fast python support for lidar-based place recognition 
    - ps. the native python version (see https://github.com/gisbi-kim/PyICP-SLAM) was already supported, but it was slow.  
  - Original C++ code: see https://github.com/irapkaist/scancontext

## Build 
- Dependency: eigen and pybind11 (for details, see CMakeLists.txt)
- for the build, follow these lines,  
  ```
   $ mkdir build
   $ cd build
   $ cmake ..
   $ make
  ```
- You also need to add path. 
  ```
   $  export PYTHONPATH=$PYTHONPATH:{YOUR_PATH}/build/python
  ```
## Use examples  
  ```
   $ cd tests 
   $ python3 test_make_desciptor.py
  ```

## Applications 
### PyICP-SLAM2 
- TBA ... 
