from Taxi import Taxi, TaxiState
from QueueManager import QueueManager
from RideRequest import RideRequest
import Constants
import random
import time

class Controller:
    
    def __init__(self, tick = Constants.TICK):
        """
        Initialize the controller with a specified tick interval.
        Args:
            tick (int): The time interval for each simulation step (in seconds).
        """
        self._tick = tick
        self._total_time = 0
        self._taxis: list[Taxi] = []
        self._que_manager = QueueManager()
        self._generate_taxis()
        self._print_taxi_locations()
        
    
    def simulate_step(self):
        """
        Simulate one step of the simulation:
        - Generate a new ride request.
        - Allocate taxis to pending requests.
        - Update the state of all taxis.
        - Print the current status.
        """
        self._generate_request()
        self._allocate_taxis()
        self._update_taxis()
        self._total_time += self._tick
        self._print_status()
        time.sleep(2)
            
           
    def _generate_taxis(self):
        """
        Randomly generate taxi locations and initialize Taxi objects.
        """
        x_values = random.sample(range(Constants.GRID_LENGTH), Constants.AMOUNT_OF_TAXIS)
        y_values = random.sample(range(Constants.GRID_LENGTH), Constants.AMOUNT_OF_TAXIS)
        
        for i in range(Constants.AMOUNT_OF_TAXIS):
            self._taxis.append(Taxi(x_values[i], y_values[i], i+1))
             
    
    def _generate_request(self):
        """
        Generate a random ride request and add it to the queue.
        """
        try:
            start = random.sample(range(Constants.GRID_LENGTH), 2)
            end = random.sample(range(Constants.GRID_LENGTH), 2)
            
            self._que_manager.add_request(RideRequest((start[0], start[1]), (end[0], end[1])))        
        except (ValueError, TypeError) as e:
            print(e)
        except e:
            print("unknown error ", e)
       
    
    def _allocate_taxis(self):
        """
        Allocate the nearest available taxi to each ride request in the queue.
        """
        while not self._que_manager.is_empty() and self._is_available_taxi():
            request = self._que_manager.get_next_request()
            taxi = self._get_closest_taxi(request.get_pos())
            
            if taxi:
                taxi.assign_ride(request)
            else:
                self._que_manager.add_request(request, False)


    def _is_available_taxi(self):
        """
        Check if there are any standing (idle) taxis available.
        """
        return any(t.get_state() == TaxiState.STANDING for t in self._taxis)
        
    
    def _get_closest_taxi(self, start: tuple):
        """
        Find the closest available taxi to a given start location.
        Args:
            start (tuple): The pickup location (x, y).
        Returns:
            Taxi: The closest available taxi or None if no taxis are available.
        """
        distance = Constants.GRID_LENGTH * 2
        closest_taxi = None
        for taxi in self._taxis:
            if taxi.get_state() == TaxiState.STANDING:
                taxi_distance = taxi.calculate_distance(start[0], start[1])
                if taxi_distance <= distance:
                    closest_taxi = taxi
                    distance = taxi_distance
        return closest_taxi
             
                
    def _update_taxis(self):
        """
        Update the state of all taxis, moving them towards their destinations.
        """
        for taxi in self._taxis:
            taxi.move()
    
    
    def _print_status(self):
        """
        Print the current status of the simulation, including the queue and taxi locations.
        """
        print(f'----------------------------------------------------\nAfter {self._total_time} seconds: \nOrder Queue:\n{self._que_manager.__str__()} ')
        self._print_taxi_locations()
    

    def _print_taxi_locations(self):
        """
        Print the current locations and states of all taxis.
        """
        print("Taxi locations:")
        for taxi in self._taxis:
            print(taxi.__str__())
            