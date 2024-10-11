'''
Gouravjeet Student Id 100920691
TPRG 2131 Fall 2024 Assignment 1, Test file template.
oct, 2024

This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving.
credit to the original author(s)


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''
import math
from A_V_calc1 import area_circle, vol_cylinder, area_rectangular, vol_sphere, area_triangle
def test_area_circle():# Test function for area of a circle
    assert area_circle(6) ==  113.1
    assert area_circle(0) == 0
def test_vol_cylinder():# Test function for volume of a cylinder
    assert vol_cylinder(4,6) == 301.8
    assert vol_cylinder(0,6) == 0
def test_area_rectangular():# Test function for area of a rectangular surface
    assert area_rectangular(3,7) == 21.0
    assert area_rectangular(0,7) == 0
def test_vol_sphere():# Test function for volume of a sphere
    assert vol_sphere(9) == 3053.6
    assert vol_sphere(0) == 0
def test_area_triangle():# Test function for area of a triangle
    assert area_triangle(5,8) == 20.0
    assert area_triangle(0,8) == 0