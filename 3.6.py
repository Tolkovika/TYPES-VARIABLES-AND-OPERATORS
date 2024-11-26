import math

def calculate_horizon_distance(height):
    """
    Calculate the distance to the horizon based on the observer's height.
    
    Parameters:
    height (float): Height of the observer in meters.
    
    Returns:
    float: Distance to the horizon in kilometers.
    """
    return 3.57 * math.sqrt(height)

# Get height from the user
height = float(input("Enter the height above the ground in meters: "))
distance = calculate_horizon_distance(height)

print(f"The distance to the horizon is approximately {distance:.2f} km.")

# Calculate distances for the specified scenarios
beach_height = 1.7  # Average human eye level in meters
hotel_height = 20.0

beach_distance = calculate_horizon_distance(beach_height)
hotel_distance = calculate_horizon_distance(hotel_height)

print(f"\nDistance to the horizon when standing on the beach (height = {beach_height} m): {beach_distance:.2f} km")
print(f"Distance to the horizon from a hotel window at 20 meters: {hotel_distance:.2f} km")
