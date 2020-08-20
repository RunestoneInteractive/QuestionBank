.. activecode:: functMath_logSin
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-mathfunctions
    :topics: 04-functions/04-mathfunctions
    :from_source: T
    :coach:
    :caption: This example demonstrates the use of the math module's log and sin functions.

    import math

    signal_power = 10
    noise_power = 10
    ratio = signal_power / noise_power
    decibels = 10 * math.log10(ratio)
    print(decibels)

    radians = 0.7
    height = math.sin(radians)
    print(height)