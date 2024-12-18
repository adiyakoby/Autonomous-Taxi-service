from enum import Enum

class TaxiState(Enum):
    DRIVING = 1
    STANDING = 2



class Taxi:
    
    def __init__(self, x: int, y: int, id: int, speed:int = 20):
        self.__id = id
        self.__speed = speed # meter per second
        self._destination = (-1, -1)
        self._pos = (x, y)
        self._state = TaxiState.STANDING
        
    
    def __str__(self):
        return f'Taxi-{self.__id}: {self._pos[0]}Km, {self._pos[y]}Km ({self._state})'
    
    def move(self):
        if self.__destination[0] != -1 and self.__destination[1] != -1:
            self._pos += self._calculate_move()
            
            
    
    def update_state(self, state: TaxiState, dest_x: int = -1, dest_y: int = -1):
        self._state = state
        self.pos = (dest_x, dest_y)
    
    
    def calculate_distance(self, x: int, y: int):
        return abs(x - self._pos[0]) + abs(y - self._pos[1])
    
    def _calculate_move(self):
        x = y = 0
        x_dist = self._destination[0] - self._pos[0] 
        
        if x_dist != 0:
            x += self._next_move(x_dist)
        else:
            y += self._next_move(self._destination[1] - self._pos[1])
            
        return (x, y)
    
    def _next_move(self, distance: int):        
        if distance > 0:
            return min(self.__speed, distance)
        else:
           return min(self.__speed, -distance) * (-1)
