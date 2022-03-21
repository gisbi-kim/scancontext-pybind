project(scancontext_python_wrapper)

pybind11_add_module(pyscancontext scancontext/wrapper.cpp)

target_link_libraries(pyscancontext PUBLIC Scancontext::scancontext)

# # https://github.com/pybind/pybind11/issues/1818
if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
  target_compile_options(pyscancontext PUBLIC -fsized-deallocation)
endif()