.. activecode:: wvu_image_rotation
    :author: Brian Powell
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: Iteration
    :subchapter: Exercises
    :topics: Iteration/Exercises
    :from_source: F

    Write a program that will rotate an image by any arbitrary degree. Your code must create an output image that is large enough to contain all of the original image without cropping.

    The provided calculate_rotation() function will determine the adjusted location of a pixel after it has been rotated. The function returns a tuple, where the first element is the rotated X coordinate and the second element is the rotated Y coordinate.
    ~~~~
    import math

    def calculate_rotation(x, y, degrees):
        """Returns updated x and y coordinates"""
        
        # Convert degrees to radians
        radians = degrees * (math.pi / 180)
        
        x_rot = round(x * math.cos(radians) - y * math.sin(radians))
        y_rot = round(x * math.sin(radians) + y * math.cos(radians))
        return (x_rot, y_rot)
    ====