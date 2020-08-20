.. activecode:: functMath_sinPi
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-mathfunctions
    :topics: 04-functions/04-mathfunctions
    :from_source: T
    :coach:
    :caption: This example demonstrates the use of the math module's sin and pi functions.

    import math

    degrees = 45
    radians = degrees / 360.0 * 2 * math.pi
    result = math.sin(radians)
    print(result)