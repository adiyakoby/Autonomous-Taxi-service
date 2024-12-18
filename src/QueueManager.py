from collections import deque
from RideRequest import RideRequest

MIN_VAL = 0
MAX_VAL = 20000

class QueueManager:
    
    def __init__(self):
        self._que: list[RideRequest] = deque()
    
    
    def add_request(self, req: RideRequest) -> None:
        pos, dest = req.get_pos(), req.get_dest()
        if not (MIN_VAL <= pos[0] <= MAX_VAL and MIN_VAL <= pos[1] <= MAX_VAL) or \
           not (MIN_VAL <= dest[0] <= MAX_VAL and MIN_VAL <= dest[1] <= MAX_VAL):
               raise ValueError(f'Values of position and destination must be between {MIN_VAL} to {MAX_VAL}.')
        self._que.append(req)
    
    def is_empty(self) -> bool:
        return not self._que
    
    def get_next_request(self):
        return self._que.popleft()