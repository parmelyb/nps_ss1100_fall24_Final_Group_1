################################
#Command and Data Handling
################################

command_dict = {
    "Reaction Control Subsystem": {
        "Code": "RCS",
        "Commands": {
            "CMD01": ['THRUST_X', (0, 60)],
            "CMD02": ['THRUST_Y', (0, 60)],
            "CMD03": ['THRUST_Z', (0, 60)],
            "CMD04": ['SAFE_MODE', {0, 1}]
        }
    },
    "Thermal Control Subsystem": {
        "Code": "TCS",
        "Commands": {
            "CMD01": ['HEATER_ON', {0, 1}],
            "CMD02": ['HEATER_OFF', {0, 1}],
            "CMD03": ['VENT_OPEN_RADIATOR', {0, 1}],
            "CMD04": ['TEMP_SETPOINT', (-30, 60)]
        }
    },
    "Attitude Control Subsystem": {
        "Code": "ACS",
        "Commands": {
            "CMD01": ['ROTATE_X', (-360, 360)],
            "CMD02": ['ROTATE_Y', (-360, 360)],
            "CMD03": ['ROTATE_Z', (-360, 360)],
            "CMD04": ['SAFE_MODE', {0, 1}]
        }
    },
    "Command & Data Handling": {
        "Code": "CDH",
        "Commands": {
            "CMD01": ['TRANSMIT_HIGH', {0, 1}],
            "CMD02": ['TRANSMIT_LOW', {0, 1}],
            "CMD03": ['RECEIVE_MODE', {0, 1}],
            "CMD04": ['SAFE_MODE', {0, 1}]
        }
    },
    "Telemetry, Tracking, & Command": {
        "Code": "TTC",
        "Commands": {
            "CMD01": ['TRANSMIT_MODE', {0, 1}],
            "CMD02": ['RECEIVE_MODE', {0, 1}],
            "CMD03": ['TRACKING_MODE', {0, 1}],
            "CMD04": ['SAFE_MODE', {0, 1}]
        }
    },
    "Electrical Power Subsystem": {
        "Code": "EPS",
        "Commands": {
            "CMD01": ['BATTERY_CHARGE_MODE', {0, 1}],
            "CMD02": ['POWER_ON_MODULE', {0, 1, 2, 3, 4}],
            "CMD03": ['POWER_OFF_MODULE', {0, 1, 2, 3, 4}],
            "CMD04": ['VOLTAGE_SETPOINT', (0, 120)]
        }
    },
    "Payload System 1": {
        "Code": "PL1",
        "Commands": {
            "CMD01": ['START_DATA_ACQUISITION', {0, 1}],
            "CMD02": ['STOP_DATA_ACQUISITION', {0, 1}],
            "CMD03": ['CALIBRATE_SENSOR', {0, 1}],
            "CMD04": ['SAFE_MODE', {0, 1}]
        }
    },
    "Payload System 2": {
        "Code": "PL2",
        "Commands": {
            "CMD01": ['START_DATA_ACQUISITION', {0, 1}],
            "CMD02": ['STOP_DATA_ACQUISITION', {0, 1}],
            "CMD03": ['CALIBRATE_SENSOR', {0, 1}],
            "CMD04": ['SAFE_MODE', {0, 1}]
        }
    }
}


def parse_command(command_str):
    # Parse the input string into parts
    try:
        subsystem_code, command_code, param_value = command_str.split(':')
    except ValueError:
        raise ValueError("Invalid command format. Expected 'Subsystem:CommandCode:Parameter'.")

    # Convert to uppercase to handle case-insensitive input
    subsystem_code = subsystem_code.strip().upper()
    command_code = command_code.strip().upper()

    # Validate and find the corresponding subsystem
    subsystem_name = None
    for subsystem, details in command_dict.items():
        if details['Code'].upper() == subsystem_code:
            subsystem_name = subsystem
            break

    if not subsystem_name:
        raise ValueError(f"Invalid subsystem code: {subsystem_code}")

    # Validate the command code
    commands = command_dict[subsystem_name]["Commands"]
    if command_code not in commands:
        raise ValueError(f"Invalid command code: {command_code}")

    # Check if param_value is valid and convert to float
    param_value = param_value.strip()  
    if not param_value:
        raise ValueError(f"Invalid parameter value: '{param_value}' (must not be empty).")

    try:
        param_value = float(param_value)
    except ValueError:
        raise ValueError(f"Invalid parameter value: '{param_value}' (must be a numeric type).")

###############################################################################################################
# Check if the parameter is within the allowed range/set
# Used ChatGPT to enhance my code to derive this check
    
    command_name, param_range = commands[command_code]
    if isinstance(param_range, tuple):
        min_val, max_val = param_range
        if not (min_val <= param_value <= max_val):
            raise ValueError(
                f"Parameter {param_value} is out of range for command '{command_code}'. Expected range: ({min_val}, {max_val}).")
    elif isinstance(param_range, set):
        if param_value not in param_range:
            raise ValueError(
                f"Parameter {param_value} is not an acceptable value for command '{command_code}'. Allowed values: {param_range}.")
    return (subsystem_name, command_name, param_value)
    
###############################################################################################################

# Test the function with predefined test cases
def test_predefined_inputs():
    test_inputs = [
        "EPS:CMD01:0",  # Valid 
        "ACS:CMD04:-1",  # Invalid
        "RCS:INVALID:0",  # Invalid
    ]

    print("Testing predefined inputs:")
    for test_input in test_inputs:
        try:
            result = parse_command(test_input)
            print(f"Command '{test_input}' parsed successfully: {result}")
        except ValueError as e:
            print(f"Error parsing command '{test_input}': {e}")
    print("\n")

# Get user input
def get_user_input():
    print("Enter a command in the format 'Subsystem:CommandCode:Parameter' (e.g., 'EPS:CMD01:0'). Type 'exit' to quit.")
    while True:
        user_input = input("Enter command: ")
        if user_input.lower() == "exit":
            print("Exiting...")
            break

        try:
            result = parse_command(user_input)
            print(f"Command '{user_input}' parsed successfully: {result}")
        except ValueError as e:
            print(f"Error parsing command '{user_input}': {e}")

# Run predefined tests
test_predefined_inputs()

# Allow user input
get_user_input()
