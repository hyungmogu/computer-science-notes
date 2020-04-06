class Rectangle:
    """A rectangle is defined by its top-left coordinates as well as its width
    and height."""

    def __init__(self, x, y, width, height):
        """ Initialize this Rectangle

        @type self: Rectangle
        @type x: int
            The x coordinate of top-left corner of this rectangle
        @type y: int
            The y coordinate of top-left corner of this rectangle
        @type width: int
            The width of this rectangle
        @type height: int
            The height of this rectangle
        """

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def translate_left(self, num):
        """Translate Rectangle to left by <num>
        @type self: Rectangle
        @type num: int
        @rtype: None
        >>> rect = Rectangle(10,20,300,400)
        >>> rect.translate_left(10)
        """

        self.x -= num

    def translate_right(self, num):
        """Translate Rectangle to right by <num>
        @type self: Rectangle
        @type num: int
        @rtype: None
        >>> rect = Rectangle(10,20,300,400)
        >>> rect.translate_right(10)
        """

        self.x += num

    def translate_up(self, num):
        """Translate Rectangle to up by <num>
        @type self: Rectangle
        @type num: int
        @rtype: None
        >>> rect = Rectangle(10,20,300,400)
        >>> rect.translate_up(10)
        """

        self.y += num

    def translate_down(self, num):
        """Translate Rectangle to down by <num>
        @type self: Rectangle
        @type num: int
        @rtype: None
        >>> rect = Rectangle(10,20,300,400)
        >>> rect.translate_down(10)
        """

        self.y -= num

    def is_equal(self, rect):
        """Return whether <rect> and <self> have the same coordinate and size
        @type self: Rectangle
        @type rect: Rectangle
        @rtype: bool
        >>> rect_1 = Rectangle(10,20,300,400)
        >>> rect_2 = Rectangle(10,20,300,400)
        >>> rect_3 = Rectangle(15,25,300,400)
        >>> rect_1.is_equal(rect_2)
        True
        >>> rect_1.is_equal(rect_3)
        False
        """

        if (self.x == rect.x and
            self.y == rect.y and
            self.width == rect.width and
            self.height == rect.height):
            return True

        return False


    def is_falling_within_another_rectangle(self, rect):
        """Return whether <self> is inside <rect>
        @type self: Rectangle
        @type rect: Rectangle
        @rtype: bool
        >>> rect_1 = Rectangle(10,20,300,400)
        >>> rect_2 = Rectangle(15,15,100,50)
        >>> rect_2.is_falling_within_another_rectangle(rect_1)
        True
        """

        if (self.x < rect.x and
            rect.x + rect.width < self.x + self.width and
            self.y < rect.y and
            rect.y + rect.height < self.y + self.height):

            return True

        if (rect.x < self.x and
            self.x + self.width < rect.x + rect.width and
            rect.y < self.y and
            self.y + self.height < rect.y + rect.height):

            return True

        return False

    def is_overlapping(self, rect):
        """Returns whether <self> has overlapping region with <rect>
        @type self: Rectangle
        @type rect: Rectangle
        @rtype: bool
        >>> rect_1 = Rectangle(10,20,300,400)
        >>> rect_2 = Rectangle(0,0,300,400)
        >>> rect_1.is_overlapping(rect_2)
        True
        """

        overlaps_in_x = (
            (rect.x <= self.x) and
            (self.x <= rect.x + rect.width) or
            (self.x <= rect.x) and
            (rect.x <= self.x + self.width))

        overlaps_in_y = (
            (rect.y <= self.y) and
            (self.y <= rect.y + rect.height) or
            (self.y <= rect.y) and
            (rect.y <= self.y + self.height))

        if overlaps_in_x and overlaps_in_y:
            return True

        return False