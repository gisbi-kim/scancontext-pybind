cmake_minimum_required(VERSION 3.11)
project(Scancontext VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 14)

if(CMAKE_VERSION VERSION_LESS "3.15")
  include("${CMAKE_CURRENT_SOURCE_DIR}/cmake/ListPrepend.cmake")
  list_prepend(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
else()
  list(PREPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
endif()

# bind
option(SC_BUILD_PYTHON_BINDING "Build Python binding for Scancontext" ON)

# other libs 
find_package(nanoflann REQUIRED QUIET)
find_package(Eigen3 3.3 REQUIRED NO_MODULE)

# sc lib
add_subdirectory(scancontext)

if (SC_BUILD_PYTHON_BINDING)
  include(pybind11)
  add_subdirectory(python)
endif()
