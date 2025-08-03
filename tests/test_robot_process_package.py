from main import robot_process_package

from main.robot_process_package import (
    PACKAGE_REJECTED,
    PACKAGE_SPECIAL,
    PACKAGE_STANDARD
)


# Tests for type of packages
def test_classify_package_type_rejected():
    result = robot_process_package.classify_package_type(True, True)
    assert result == PACKAGE_REJECTED

def test_classify_package_type_special_bulky():
    result = robot_process_package.classify_package_type(True, False)
    assert result == PACKAGE_SPECIAL

def test_classify_package_type_special_heavy():
    result = robot_process_package.classify_package_type(False, True)
    assert result == PACKAGE_SPECIAL

def test_classify_package_type_standart():
    result = robot_process_package.classify_package_type(False, False)
    assert result == PACKAGE_STANDARD


# Testing if the package is bulky or heavy
def test_check_package_criteria_not_bulky_and_heavy():
    result = robot_process_package.check_package_criteria(10, 10, 10, 10)
    assert result == (False, False)

def test_check_package_criteria_bulky_volume():
    result = robot_process_package.check_package_criteria(1000, 1000, 1000, 10)
    assert result == (True, False)

def test_check_package_criteria_bulky_dimension():
    result = robot_process_package.check_package_criteria(200, 10, 10, 10)
    assert result == (True, False)

def test_check_package_criteria_bulky_heavy():
    result = robot_process_package.check_package_criteria(10, 10, 10, 30)
    assert result == (False, True)


# Testing sort packages
def test_sort_packages_standard():
    result = robot_process_package.sort_packages(10, 10, 10, 10)
    assert result == PACKAGE_STANDARD

def test_sort_packages_special():
    result = robot_process_package.sort_packages(200, 10, 10, 10)
    assert result == PACKAGE_SPECIAL

def test_sort_packages_rejected():
    result = robot_process_package.sort_packages(1000, 1000, 1000, 30)
    assert result == PACKAGE_REJECTED