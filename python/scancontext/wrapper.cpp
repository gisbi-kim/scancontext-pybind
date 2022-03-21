#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "scancontext/Scancontext.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

PYBIND11_MODULE(pyscancontext, m) {

    py::class_<SCManager>(m, "SCManager")
        .def(py::init<>())
        .def("print_parameters", &SCManager::printParameters, py::return_value_policy::copy)
        .def("make_scancontext", &SCManager::makeScancontext, py::return_value_policy::copy);
    // .def("add_node", &SCManager::makeAndSaveScancontextAndKeys, py::return_value_policy::copy);
    // .def("test_print")
    // .def("get_corner_points", &kcp::keypoint::MultiScaleCurvature::get_corner_points, py::return_value_policy::copy)
    // .def("get_plane_points", &kcp::keypoint::MultiScaleCurvature::get_plane_points, py::return_value_policy::copy)
    // .def("get_corner_point_indices", &kcp::keypoint::MultiScaleCurvature::get_corner_point_indices, py::return_value_policy::copy)
    // .def("get_plane_point_indices", &kcp::keypoint::MultiScaleCurvature::get_plane_point_indices, py::return_value_policy::copy)
    // .def("get_curvature", &kcp::keypoint::MultiScaleCurvature::get_curvature, py::return_value_policy::copy);

//   py::class_<kcp::KCP::TEASER::Params>(m, "TEASERParams")
//       .def(py::init<>())
//       .def_readwrite("noise_bound", &kcp::KCP::TEASER::Params::noise_bound)
//       .def_readwrite("cbar2", &kcp::KCP::TEASER::Params::cbar2)
//       .def_readwrite("estimate_scaling", &kcp::KCP::TEASER::Params::estimate_scaling)
//       .def_readwrite("rotation_gnc_factor", &kcp::KCP::TEASER::Params::rotation_gnc_factor)
//       .def_readwrite("rotation_estimation_algorithm", &kcp::KCP::TEASER::Params::rotation_estimation_algorithm)
//       .def_readwrite("rotation_max_iterations", &kcp::KCP::TEASER::Params::rotation_max_iterations)
//       .def_readwrite("rotation_cost_threshold", &kcp::KCP::TEASER::Params::rotation_cost_threshold)
//       .def_readwrite("kcore_heuristic_threshold", &kcp::KCP::TEASER::Params::kcore_heuristic_threshold)
//       .def_readwrite("use_max_clique", &kcp::KCP::TEASER::Params::use_max_clique)
//       .def_readwrite("max_clique_exact_solution", &kcp::KCP::TEASER::Params::max_clique_exact_solution)
//       .def_readwrite("max_clique_time_limit", &kcp::KCP::TEASER::Params::max_clique_time_limit);

//   py::class_<kcp::KCP::Params>(m, "KCPParams")
//       .def(py::init<>())
//       .def_readwrite("k", &kcp::KCP::Params::k)
//       .def_readwrite("teaser", &kcp::KCP::Params::teaser);

//   py::class_<kcp::KCP>(m, "KCP")
//       .def(py::init<kcp::KCP::Params>())
//       .def("get_params", &kcp::KCP::get_params, py::return_value_policy::reference)
//       .def("get_initial_correspondences", &kcp::KCP::get_initial_correspondences)
//       .def("get_inlier_correspondence_indices", &kcp::KCP::get_inlier_correspondence_indices)
//       .def("solve", &kcp::KCP::solve)
//       .def("get_solution", &kcp::KCP::get_solution);

}