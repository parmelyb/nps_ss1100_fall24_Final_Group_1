This project implements a Thruster class for the Reaction Control Subsystem (RCS) of a spacecraft, refactored from procedural code into object-oriented programming (OOP). 
The class defines limits for thrust, flow rate, and exhaust velocity to ensure safe operation.
The detect_malfunction() method checks if input values exceed these limits and prints any errors.
The calculate_delta_v() method computes the change in velocity (delta v) based on flow rate, exhaust velocity, and firing duration.
The main function tests the Thruster class with three cases. It calculates delta v for each and detects malfunctions when limits are exceeded. Outputs are printed to the console, showing errors and results.
To run the code, save it as a Python file and execute it with Python 3.x. The script verifies that the thruster works correctly under different scenarios.
This code was based off of a code found in Stack overflow and then written and then rewritten using AI into OOP
This project highlights how OOP improves code organization and makes systems like the RCS easier to test and expand.
