

class RideRequest:

    def __init__(self, start: tuple[int, int], end: tuple[int, int]):
        if type(start) != tuple or type(end) != tuple or len(start) != 2 or len(end) != 2:
            raise TypeError('Must provide two tuples of length 2')
        self._pos = start
        self._dest = end
        
    def get_pos(self) -> tuple[int, int]:
        return self._pos
    
    def get_dest(self) -> tuple[int, int]:
        return self._dest
    
    def __str__(self):
        
        return f'Drive request: from {self._pos.__str__()} to {self._dest.__str__()}'