################################
#Command and Data Handling
################################

import re

# Dictionary to map subsystem codes to their full names and commands
subsystem_dict = {
    "RCS": {"name": "Reaction Control System", "commands": {
        "CMD01": ("THRUST_X", (0, 100)),
        "CMD02": ("THRUST_Y", (0, 100)),
        "CMD03": ("THRUST_Z", (0, 100)),
        "CMD04": ("SAFE_MODE", True),
    }},
    "TCS": {"name": "Thermal Control System", "commands": {
        "CMD01": ("HEATER_ON", True),
        "CMD02": ("HEATER_OFF", True),
        "CMD03": ("VENT_OPEN_RADIATOR", True),
        "CMD04": ("TEMP_SETPOINT", (-200, 150)),
    }},
    "ACS": {"name": "Attitude Control System", "commands": {
        "CMD01": ("ROTATE_X", (-180, 180)),
        "CMD02": ("ROTATE_Y", (-180, 180)),
        "CMD03": ("ROTATE_Z", (-180, 180)),
        "CMD04": ("SAFE_MODE", True),
    }},
    "CDH": {"name": "Command & Data Handling", "commands": {
        "CMD01": ("TRANSMIT_HIGH", True),
        "CMD02": ("TRANSMIT_LOW", True),
        "CMD03": ("RECEIVE_MODE", True),
        "CMD04": ("SAFE_MODE", True),
    }},
    "TTC": {"name": "Telemetry, Tracking & Command", "commands": {
        "CMD01": ("TRANSMIT_MODE", True),
        "CMD02": ("RECEIVE_MODE", True),
        "CMD03": ("TRACKING_MODE", True),
        "CMD04": ("SAFE_MODE", True),
    }},
    "EPS": {"name": "Electrical Power System", "commands": {
        "CMD01": ("BATTER_CHARGE_MODE", True), 
        "CMD02": ("POWER_ON_MODULE", True),
        "CMD03": ("POWER_OFF_MODULE", True),  
        "CMD04": ("VOLTAGE_SETPOINT", (0, 120)) 
    }},
    "PL1/PL2": {"name": "Payload system (and number)", "commands": {
        "CMD01": ("START_DATA_ACQUISITION", True),
        "CMD02": ("STOP_DATA_ACQUISITION", True),
        "CMD03": ("CALIBRATE_SENSOR", True),
        "CMD04": ("SAFE_MODE", True),
    }}
}

# Function to validate numeric values based on command tolerance
def is_valid_parameter(subsystem_code, command_code, param_value):
    """Check if the parameter value is valid based on the command's tolerance."""
    subsystem_info = subsystem_dict.get(subsystem_code)
    if subsystem_info:
        command_info = subsystem_info["commands"].get(command_code)
        if command_info:
            tolerance = command_info[1]
            if tolerance is True:
                return isinstance(param_value, bool)  # Expecting a boolean value (True/False)
            if isinstance(tolerance, tuple) and len(tolerance) == 2:
                min_val, max_val = tolerance
                return min_val <= param_value <= max_val
    return False

# Function to parse and route the command
def parse_command(command_string):
    try:
        # Split command into blocks
        blocks = command_string.split(":")
        if len(blocks) != 3:
            raise ValueError("Command format is incorrect. Must be 'Subsystem:CommandCode:Parameter'.")

        subsystem_code = blocks[0].upper()  # Make subsystem code case-insensitive
        command_code = blocks[1].upper()  # Make command code case-insensitive
        param_value_str = blocks[2].strip()

        # Check if subsystem exists
        if subsystem_code not in subsystem_dict:
            raise ValueError(f"Invalid subsystem code: {subsystem_code}")

        subsystem_info = subsystem_dict[subsystem_code]
        subsystem_name = subsystem_info["name"]

        # Check if command exists
        if command_code not in subsystem_info["commands"]:
            raise ValueError(f"Invalid command code: {command_code}")

        # Get command description and tolerance
        command_description, tolerance = subsystem_info["commands"][command_code]

        # Try to handle the parameter as either boolean or numeric
        param_value = None
        if tolerance is True:  # Boolean Value
            param_value_str_lower = param_value_str.lower()
            if param_value_str_lower == 'true':
                param_value = True
            elif param_value_str_lower == 'false':
                param_value = False
            else:
                raise ValueError(f"Invalid parameter value: {param_value_str}. Expected 'True' or 'False'.")
        else:  # Numeric Value
            try:
                param_value = float(param_value_str)
            except ValueError:
                raise ValueError(f"Invalid parameter value: {param_value_str}. Must be numeric.")

        # Validate parameter within acceptable range if applicable
        if not is_valid_parameter(subsystem_code, command_code, param_value):
            raise ValueError(f"Parameter value {param_value} out of tolerance for command {command_code}.")

        # Return the tuple as requested
        return (subsystem_name, command_description, param_value)

    except ValueError as ve:
        return f"Error: {ve}"

# Interactive Input:
while True:
    # Take user input
    command_input = input("Enter command (Subsystem:CommandCode:Parameter) or type 'q' to quit: ").strip()

    # Check for exit condition
    if command_input.lower() == 'q':
        print("Exiting the program.")
        break

    # Parse the command and display the result
    result = parse_command(command_input)
    print(f"Result: {result}\n")
