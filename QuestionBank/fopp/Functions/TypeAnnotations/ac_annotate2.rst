.. activecode:: ac_annotate2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Functions
    :subchapter: TypeAnnotations
    :topics: Functions/TypeAnnotations
    :from_source: T

    def add(x: int, y: int) -> int:
        """Returns the sum of `x` and `y`"""

        return x + y

    def get_number(msg: str) -> float:
        """Prompts with `msg` for input; returns numeric response."""

        return float(input(msg))

    def display_msg(msg: str):
        """Displays `msg` with dashed line underneath"""

        print(msg)
        print('-------------------------------------')