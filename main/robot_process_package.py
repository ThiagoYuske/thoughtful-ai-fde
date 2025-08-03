# main.py
CRITERIA_BULKY_VOLUME_LIMIT = 1000000    # cm3
CRITERIA_BULKY_DIMENSION_LIMIT = 150     # cm
CRITERIA_HEAVY_MASS_LIMIT = 20            # kg

PACKAGE_STANDARD = "STANDARD"
PACKAGE_SPECIAL = "SPECIAL"
PACKAGE_REJECTED = "REJECTED"

WIDTH = 10
HEIGHT = 20
LENGTH = 30
MASS = 5

def check_package_criteria(width, height, length, mass):
    is_bulky = False
    is_heavy = False

    volume = width * height * length

    if volume >= CRITERIA_BULKY_VOLUME_LIMIT or width >= CRITERIA_BULKY_DIMENSION_LIMIT or height >= CRITERIA_BULKY_DIMENSION_LIMIT or length >= CRITERIA_BULKY_DIMENSION_LIMIT:
        is_bulky = True
    if mass >= CRITERIA_HEAVY_MASS_LIMIT:
        is_heavy = True

    return is_bulky, is_heavy


def classify_package_type(is_bulky, is_heavy):
    if is_bulky and is_heavy:
        return PACKAGE_REJECTED
    elif is_bulky or is_heavy:
        return PACKAGE_SPECIAL
    else:
        return PACKAGE_STANDARD


def sort_packages(width, height, length, mass) -> str:
    is_bulky, is_heavy = check_package_criteria(width, height, length, mass)
    
    return classify_package_type(is_bulky, is_heavy)


def process_package(width, height, length, mass):
    package_type = sort_packages(width, height, length, mass)

    return package_type


package_type = process_package(width=WIDTH, height=HEIGHT, length=LENGTH, mass=MASS)

print(f"The package is: {package_type}")