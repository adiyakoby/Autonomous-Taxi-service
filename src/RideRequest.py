

class RideRequest:
    """
    Represents a ride request, specifying a start and end position on the grid.
    """

    def __init__(self, start: tuple[int, int], end: tuple[int, int]):
        """
        Initialize a ride request.

        Args:
            start (tuple[int, int]): The starting position (x, y) of the ride.
            end (tuple[int, int]): The destination position (x, y) of the ride.

        Raises:
            TypeError: If the start or end positions are not tuples of length 2.
        """
        if type(start) != tuple or type(end) != tuple or len(start) != 2 or len(end) != 2:
            raise TypeError('Must provide two tuples of length 2')
        self._pos = start
        self._dest = end
        
        
    def get_pos(self) -> tuple[int, int]:
        """
        Get the starting position of the ride.

        Returns:
            tuple[int, int]: The starting position (x, y).
        """
        return self._pos
    
    
    def get_dest(self) -> tuple[int, int]:
        """
        Get the destination of the ride.

        Returns:
            tuple[int, int]: The destination position (x, y).
        """
        return self._dest
    
    
    def __str__(self):
        """
        Represent the ride request as a string.

        Returns:
            str: A string representation of the ride request, 
                 displaying the start and end positions.
        """
        return f'Drive request: from {self._pos.__str__()} to {self._dest.__str__()}'