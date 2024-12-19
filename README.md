# Autonomous Taxi Simulation

## Author : Adi yakoby

## Overview
This project simulates an autonomous taxi service operating within a 20km x 20km grid. The taxis can receive ride requests, calculate the optimal path to the pickup location, and transport passengers to their destinations. The simulation runs in discrete time steps (20 seconds per tick), updating the positions and states of all taxis and handling new ride requests in each step.

---

## Features
- **Dynamic Ride Allocation**: Assigns the nearest available taxi to incoming ride requests.
- **Efficient Taxi Movement**: Implements Manhattan distance logic to simulate movement along the grid.
- **Queue Management**: Maintains a queue for unassigned ride requests and processes them as taxis become available.
- **Simulation Steps**: Updates the system state every 20 seconds, handling:
  - Taxi movement.
  - Ride allocation.
  - Printing the current state of taxis and the queue.

---

## Project Structure
### Code Components
1. **`RideRequest`**:
   - Represents a single ride request with a starting and destination point.

2. **`Taxi`**:
   - Represents an autonomous taxi with attributes like position, state (`STANDING` or `DRIVING`), and the current assigned ride.

3. **`QueueManager`**:
   - Manages a queue of ride requests, ensuring efficient addition, removal, and validation of requests.

4. **`Controller`**:
   - Orchestrates the simulation by:
     - Generating ride requests.
     - Allocating taxis to rides.
     - Updating taxi positions.
     - Printing the system's current status.

5. **`Constants`**:
   - Stores key parameters such as grid size, taxi speed, and the simulation tick interval.

---

## Key Features and Future Enhancements
### Current Features:
- **Taxi Movement**: Taxis follow Manhattan distance rules, moving along X or Y axes only.
- **Nearest Taxi Allocation**: Dynamically finds the nearest taxi to the ride request's start position.
- **Collision-Free Simulation**: The current implementation assumes no collisions between taxis due to controlled grid-based movement.

### Future Considerations:
- **Collision Handling**:
  If collision handling becomes necessary, we could use data structures like:
  - **Arrays** or **Dictionaries** to hold taxi positions.
  - Efficient collision detection algorithms to check for overlapping positions on each tick.
  - For example, a dictionary with keys as grid coordinates (`(x, y)`) and values as taxi IDs could efficiently detect and handle collisions.

---

## Setting Up
### Prerequisites
- Python 3.8 or later

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/adiyakoby/Autonomous-Taxi-service
   cd autonomous-taxi-service
   ```

** There is no requirments or virtual env needed for this project.

### Running the Simulation
Run the main simulation file:
```bash
python3 src/main.py
```

---


## Example Output
```
----------------------------------------------------
After 20 seconds:
Order Queue:
Drive request: from (500, 1000) to (2000, 1500)

Taxi locations:
Taxi-1: 500Km, 1100Km (DRIVING)
Taxi-2: 200Km, 800Km (STANDING)
Taxi-3: 1000Km, 600Km (STANDING)
...
```

---


## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.