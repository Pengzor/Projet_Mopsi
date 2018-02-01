cmake_minimum_required(VERSION 2.6)
file(TO_CMAKE_PATH "$ENV{IMAGINEPP_ROOT}/CMake" p)
list(APPEND CMAKE_MODULE_PATH "${p}") #For old Imagine++
find_package(Imagine REQUIRED)

project(CalculDeterministe)
add_executable(puzzle
               main.cpp
               matrice.h
               matrice.cpp
               piece.h
               piece.cpp
               test.h
               test.cpp
               algo.h
               algo.cpp
               puzzles.h
               puzzles.cpp
               graphique.h
               graphique.cpp
               ecriture.h
               ecriture.cpp)
ImagineUseModules(puzzle Graphics)
