This project implements an Attitude Control System (ACS) designed to calculate and apply the necessary rotations to adjust a satellite's orientation. 
The system simulates real-world behavior by introducing random error during each rotation and checks whether the current orientation reaches within a given tolerance of the target. 
The code consists of a function, calculate_rotation(), that determines the rotation required to achieve a desired orientation, and an AttitudeControlSystem class that manages the satellite's state. 
The class tracks the current orientation, applies calculated rotations with random error, checks for alignment within a specified tolerance, and uses file I/O to save and load orientation states for persistence.
The script defines target orientations and iteratively adjusts the satellite to align with each target. 
It logs progress to the console, showing the current orientation, the rotation applied, and confirmation when the target is reached. 
The state of the satellite is saved in a file called current_state.txt, ensuring that progress is recoverable between runs. 
Random error is added during rotations to mimic real-world inaccuracies, requiring multiple adjustments before alignment is achieved.
To execute the code, ensure Python 3.x is installed, and run the script. 
The program will automatically create current_state.txt if it does not exist, initializing the satellite's orientation to (0, 0, 0). The script iterates through a list of target orientations—(100, 200, 300), (0, 0, 0), and (3, 30, 300)—and applies corrections until the satellite's orientation is within ±0.1 of the target. 
Progress and adjustments are displayed in the console, providing a clear step-by-step view of the system's operation.
This project was developed with references from Stack Overflow and online tutorials for Python programming concepts, such as tuples, file handling, and iteration. 
AI-assisted tools were used to troubleshoot errors and refine the code’s formatting and functionality. 
Overall, the system provides a functional simulation of satellite attitude control with persistent state tracking and realistic adjustment behavior.
