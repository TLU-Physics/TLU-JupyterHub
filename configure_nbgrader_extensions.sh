#!/usr/bin/env bash

set -e

source utils.sh

# Install global extensions, and disable them globally. We will re-enable
# specific ones for different user accounts in each demo.
# jupyter labextension develop --overwrite .
jupyter labextension disable --level=sys_prefix nbgrader:assignment-list
jupyter labextension disable --level=sys_prefix nbgrader:formgrader
jupyter labextension disable --level=sys_prefix nbgrader:course-list
jupyter labextension disable --level=sys_prefix nbgrader:create-assignment
jupyter server extension disable --sys-prefix --py nbgrader

# Enable extensions for instructors.
instructors = (cberggren@tlu.edu tsauncy@tlu.edu)
for instructor in ${instructors[@]}; do
    enable_assignment_list "${instructor}"
    enable_course_list "${instructor}"
done

# Enable extensions for formgraders.
# List course IDs in lower case
courses = (coursephys371 coursephys241l)
for course in ${courses[@]}; do
    enable_create_assignment "grader-${course}"
    enable_formgrader "grader-${course}"
done

# Enable extensions for students.
students = (stud1@tlu.edu aarcsalinas@tlu.edu ajsilva@tlu.edu hhernandez@tlu.edu adrimartinez@tlu.edu tmharrison@tlu.edu jasacastro@tlu.edu)
for student in ${students[@]}; do
    enable_assignment_list "${student}"
done
