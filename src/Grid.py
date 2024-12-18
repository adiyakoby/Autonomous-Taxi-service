


class Grid:
   
    def __init__(self):
        self._grid = {} 
    
    def add_taxis(self, taxis: list) -> None:
        for taxi in taxis:
            self._grid[taxi.get_coordinates()] = taxi
    
    def get_taxis(self) -> list:
        return self._grid.values()
    
    
    
    