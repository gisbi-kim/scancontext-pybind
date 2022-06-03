add_library(scancontext SHARED
  include/scancontext/Scancontext.cpp
)

target_include_directories(scancontext PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/include>
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

set_target_properties(scancontext PROPERTIES VERSION ${PROJECT_VERSION})
target_compile_definitions(scancontext PUBLIC PROJECT_VERSION="${PROJECT_VERSION}")

target_link_libraries(scancontext 
  Eigen3::Eigen
  nanoflann::nanoflann
)

add_library(Scancontext::scancontext ALIAS scancontext)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
  DESTINATION include
)
