from enum import Enum
from RideRequest import RideRequest
import Constants


class TaxiState(Enum):
    DRIVING = 1
    STANDING = 2


class Taxi:
    
    def __init__(self, x: int, y: int, id: int, speed:int = 20):
        self.__id = id
        self.__speed = speed 
        self._destination = None
        self._request: RideRequest = None
        self._pos = (x, y)
        self._state = TaxiState.STANDING
        
    
    def __str__(self):
        return f'Taxi-{self.__id}: {self._pos[0]}Km, {self._pos[1]}Km ({self._state})'
    
    def move(self):
        if self._state == TaxiState.STANDING or not self._destination:
            return
        
        total_distance = self.__speed * Constants.TICK
        while total_distance > 0:
            self._pos += self._interval_move(total_distance)
            # self._pos += self._calculate_move()
            
            if self._pos == self._destination:
                if self._destination == self._request.get_pos():
                    self._destination = self._request.get_dest()
                else:
                    self._request = self._destination = None
                    self._state = TaxiState.STANDING
            
            
    def assign_ride(self, req : RideRequest):
        self._request = req
        self._destination = req.get_pos()
        self._state = TaxiState.DRIVING
        

    def get_state(self) -> TaxiState:
        return self._state
    
    
    def calculate_distance(self, x: int, y: int):
        return abs(x - self._pos[0]) + abs(y - self._pos[1])

    
    def _interval_move(self, total_distance):
        # total_distance = self.__speed * Constants.TICK

        x = self._next_interval_move(self._destination[0] - self._pos[0], total_distance)
        y = self._next_interval_move(self._destination[1] - self._pos[1], total_distance)
        # x_dist = self._destination[0] - self._pos[0]
        # x += min(abs(x_dist), total_distance)
        # total_distance -= x
        # if x_dist < 0:
        #     x *= -1
        
        # if total_distance > 0:
        #     y_dist = self._destination[1] - self._pos[1]
        #     y += min(abs(y_dist), total_distance)
        #     total_distance -= y
        #     if y_dist < 0:
        #         y *= -1
        
        return (x, y)
    
    def _next_interval_move(self, distance, total_distance):
        move = min(abs(distance), total_distance)
        total_distance -= move
        return move * (-1 if distance < 0 else 1)
      

    
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
