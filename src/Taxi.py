from enum import Enum
from RideRequest import RideRequest
import Constants


class TaxiState(Enum):
    """
    Enumeration for the states of a taxi.
    """
    DRIVING = 1
    STANDING = 2


class Taxi:
    """
    A class that represents a taxi, including its state, position, and assigned ride.
    """
    
    def __init__(self, x: int, y: int, id: int, speed:int = Constants.TAXI_SPEED):
        """
        Initialize a taxi.

        Args:
            x (int): Initial x-coordinate of the taxi.
            y (int): Initial y-coordinate of the taxi.
            id (int): Unique identifier for the taxi.
            speed (int): Speed of the taxi in meters per second.
        """
        self.__id = id
        self.__speed = speed 
        self._destination = None
        self._request: RideRequest = None
        self._pos = (x, y)
        self._state = TaxiState.STANDING
        
    
    def __str__(self):
        """
        Represent the taxi as a string.

        Returns:
            str: A string representation of the taxi's state and location.
        """
        return f'Taxi-{self.__id}: {self._pos[0]}Km, {self._pos[1]}Km ({self._state})'
    
    
    def move(self):
        """
        Move the taxi towards its destination, accounting for the speed and time tick.
        Updates the taxi's state when it reaches the pickup or destination point.
        """
        if self._state == TaxiState.STANDING or not self._destination:
            return None
        
        total_distance = self.__speed * Constants.TICK
        while total_distance > 0 and self._state == TaxiState.DRIVING:
            x_add, y_add = self._interval_move(total_distance)
            
            self._pos = (self._pos[0] + x_add, self._pos[1] + y_add)
            total_distance -= abs(x_add) + abs(y_add)
            
            if self._pos == self._destination:
          
                if self._destination == self._request.get_pos():
                    self._destination = self._request.get_dest()
                else:
                    self._request = self._destination = None
                    self._state = TaxiState.STANDING
            
            
            
    def assign_ride(self, req : RideRequest):
        """
        Assign a new ride request to the taxi.

        Args:
            req (RideRequest): The ride request to assign.
        """
        self._request = req
        self._destination = req.get_pos()
        self._state = TaxiState.DRIVING
        

    def get_state(self) -> TaxiState:
        """
        Get the current state of the taxi.

        Returns:
            TaxiState: The state of the taxi (DRIVING or STANDING).
        """
        return self._state
    
    
    
    def calculate_distance(self, x: int, y: int):
        """
        Calculate the Manhattan distance from the taxi's current position to a target position.

        Args:
            x (int): X-coordinate of the target position.
            y (int): Y-coordinate of the target position.

        Returns:
            int: The Manhattan distance to the target.
        """
        return abs(x - self._pos[0]) + abs(y - self._pos[1])


    
    def _interval_move(self, total_distance):
        """
        Calculate the next movement interval for the taxi within the given distance.

        Args:
            total_distance (int): The remaining distance the taxi can travel.

        Returns:
            tuple[int, int]: The x and y movement components.
        """
        x = self._next_interval_move(self._destination[0] - self._pos[0], total_distance)
        y = self._next_interval_move(self._destination[1] - self._pos[1], total_distance)
  
        return (x, y)
    
    
    
    def _next_interval_move(self, distance, total_distance):
        """
        Calculate the movement along one axis.

        Args:
            distance (int): The distance remaining along the axis.
            total_distance (int): The total distance the taxi can travel.

        Returns:
            int: The movement along the axis.
        """
        move = min(abs(distance), total_distance)
        total_distance -= move
        return move * (-1 if distance < 0 else 1)
      