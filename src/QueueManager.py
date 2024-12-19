from collections import deque
from RideRequest import RideRequest
import Constants

MIN_VAL = 0
MAX_VAL = Constants.GRID_LENGTH

class QueueManager:
    """
    A class that manages the queue of ride requests.
    """
    
    def __init__(self):
        """
        Initialize the queue manager with an empty deque for ride requests.
        """
        self._que: deque[RideRequest] = deque()
    
    
    def add_request(self, req: RideRequest, newReq: bool = True) -> None:
        """
        Add a ride request to the queue.
        Validates that the position and destination coordinates are within valid bounds.
        By default, adds the request to the end of the queue, but can prioritize it by adding it to the front.

        Args:
            req (RideRequest): The ride request to be added.
            newReq (bool): If True, add the request to the end of the queue.
                        If False, prioritize the request by adding it to the front.

        Raises:
            ValueError: If the position or destination is out of bounds.
        """
        pos, dest = req.get_pos(), req.get_dest()
        if not (MIN_VAL <= pos[0] <= MAX_VAL and MIN_VAL <= pos[1] <= MAX_VAL) or \
           not (MIN_VAL <= dest[0] <= MAX_VAL and MIN_VAL <= dest[1] <= MAX_VAL):
               raise ValueError(f'Values of position and destination must be between {MIN_VAL} to {MAX_VAL}.')
        if newReq:
            self._que.append(req)
        else:
            self._que.appendleft(req)
    
    
    
    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self._que
    
    
    
    def get_next_request(self):
        """
        Retrieve the next ride request from the queue.

        Returns:
            RideRequest: The next ride request in the queue.
        """
        return self._que.popleft()
    
    
    
    def __str__(self):
        """
        Represent the queue as a string for debugging or display.

        Returns:
            str: A formatted string representation of all pending requests.
        """
        if not self._que:
            return 'Empty'
        requsts = []
        for req in self._que:
            requsts.append(req.__str__() + '\n')
        return ''.join(requsts)
        
        