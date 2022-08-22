from .time_floor import time_floor

# Add new functions to this list.
# WARNING: Always define new functions with lowercase names, otherwise postgres will not be able to find them.
functions = [time_floor]