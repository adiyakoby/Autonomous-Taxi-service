from Taxi import Taxi, TaxiState
from QueueManager import QueueManager
from RideRequest import RideRequest
import Constants
import random
import time

class Controller:
    
    def __init__(self, tick = Constants.TICK, total_time = Constants.TOTAL):
        self._tick = tick
        self._total_time = 0
        self._taxis: list[Taxi] = []
        self._que_manager = QueueManager()
        self._generate_taxis()
        self._print_taxi_locations()
        
    
    def simulate_step(self):
        self._generate_request()
        self._allocate_taxis()
        self._update_taxis()
        self._total_time += self._tick
        self._print_status()
        time.sleep(2)
            
        
    
    def _generate_taxis(self):
        x_values = random.sample(range(Constants.GRID_LENGTH), Constants.AMOUNT_OF_TAXIS)
        y_values = random.sample(range(Constants.GRID_LENGTH), Constants.AMOUNT_OF_TAXIS)
        
        for i in range(Constants.AMOUNT_OF_TAXIS):
            self._taxis.append(Taxi(x_values[i], y_values[i], i))
        
            
    
    def _generate_request(self):
        start = random.sample(range(Constants.GRID_LENGTH), 2)
        end = random.sample(range(Constants.GRID_LENGTH), 2)
        
        self._que_manager.add_request(RideRequest((start[0], start[1]), (end[0], end[1])))
       
    
    def _allocate_taxis(self):
        while not self._que_manager.is_empty():
            request = self._que_manager.get_next_request()
            
            taxi = self._get_closest_taxi(request, request[0])
            
            if taxi:
                taxi.assign_ride(request)
            else:
                self._que_manager.add_request(request)
    
    
    def _get_closest_taxi(self, start):
        distance = Constants.GRID_LENGTH * 2
        closest_taxi = None
        for taxi in self._taxis:
            if taxi.get_state() == TaxiState.STANDING:
                if taxi.calculate_distance(start) <= distance:
                    closest_taxi = taxi
        return closest_taxi
                
    def _update_taxis(self):
        for taxi in self._taxis:
            taxi.move()
    
    def _print_status(self):
        print(f'After {self._total_time} seconds: \n Order Queue: {self._que_manager.__str__()} ')
        self._print_taxi_locations
    

    def _print_taxi_locations(self):
        print("Taxi locations:")
        for taxi in self._taxis:
            print(taxi.__str__())
            