cmake_minimum_required(VERSION 3.11)
project(Scancontext VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 14)

if(NOT CMAKE_BUILD_TYPE)
  # Options: Debug, Release, MinSizeRel, RelWithDebInfo
  message(STATUS "No build type selected, default to Release")
  set(CMAKE_BUILD_TYPE "Release" CACHE STRING "Choose build type." FORCE)
endif()

include(FetchContent)

set(PYTHONVERSION "3.10")

# ##############################################################################
# Options
# ##############################################################################
option(SC_BUILD_PYTHON_BINDING "Build Python bindings for Scancontext" ON)

# ##############################################################################
# Dependencies
# ##############################################################################
find_package(Eigen3 3.3 REQUIRED NO_MODULE)

FetchContent_Declare(nanoflann
  GIT_REPOSITORY https://github.com/jlblancoc/nanoflann
  GIT_TAG v1.4.2
)
FetchContent_MakeAvailable(nanoflann)

if(SC_BUILD_PYTHON_BINDING)
  FetchContent_Declare(pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11
    GIT_TAG v2.9.2
  )
  FetchContent_MakeAvailable(pybind11)
endif()

# ##############################################################################
# Targets
# ##############################################################################
add_subdirectory(scancontext)

if(SC_BUILD_PYTHON_BINDING)
  add_subdirectory(python)
endif()
