### Reaction Control Subsystem (RCS): Malfunction detection and velocity change calculation.
Results from running the RCS python code are below.  Go to the RCS subfolder to access the full code with in-line descriptions.
![image](https://github.com/user-attachments/assets/97d7cdb8-ed00-498e-9642-f1dcde02e745)\
### Thermal Control Subsystem (TCS): Temperature control function.
Results for running TCS function with the thermal_control.py code in IDLE Shell . Full code in TCS folder (final_TCS).
![image](https://github.com/user-attachments/assets/cefea652-e929-45e4-b440-80964147639b)

### Attitude Control Subsystem (ACS): Attitude determination and rotation calculations.
Results from running the ADC python code are below.  Go to the ADC subfolder to access the full code with in-line descriptions.
![image](https://github.com/user-attachments/assets/876d8662-8945-41d6-933b-fa5b7cd9bc4e)\

### Command and Data Handling (C&DH): Command parsing and routing.
### Electrical Power Subsystem (EPS): Power budget analysis and battery charging calculations.
Results from running the EPS.mlx file are below.  Go to the EPS subfolder to access the full code with in-line descriptions, and the EPS README file.\
![image](https://github.com/user-attachments/assets/9c4561f0-6da2-4101-8ead-e5824722fed9)\
![image](https://github.com/user-attachments/assets/0a236856-da27-4c25-9a09-11192cf51d4e)\
### Remote Sensing Payload: Data ingestion, radiance to reflectance conversion, and image rescaling.

### Question for Writeup

## 1. What was your experience in collaborating? Talk about what steps you used to ensure the inputs from group members worked - code testing, GitHub branch management, etc. - and how you divided up the workload for the project.

Group members ran each other's code to check basic functionality. After being given the expected inputs, the code was checked for error handling by giving unexpected values as input to see if it was caught. Changes were made accordingly to ensure that the code didn't break with those unexpected inputs. The project was divided up into the following parts.

Ryan - TCS\
Brian - EPS (Satisfies the Matlab requirement)\
Brandon - RCS/ACS\
Joshua - RSP/C&DH

## 2. What was the most challenging section, and why? Feel free to provide more than one response if there is a difference of opinion in the group.

Joshua - The most difficult of the two subsystems was the Payload. It required several functions working together to combine the files, run conversions, generate, output and save the files while getting user input to ensure the correct files were fed into the program in the correct order. Overall, completing both subsystems took me approximately 8 hours to complete.\
Brian - EPS was not a particularly challenging section, but I believe this was due primarily to the fact that Dr. MacDonald allowed some flexibility in the input format of the EPS data.  While I was able to follow the format (Voltage, Current, Time), the Check Plus section had a format [(V,I,T),(V,I,T),(V,I,T)].  Since we opted to do EPS in MATLAB, the tuple format was not ideal.  While I'm sure there was a way to force this data type, it would have been challenging, and likely would have consumed the vast majority of the programming/research time.  In order to meet the intent of the lab, I kept the (V,I,T) format for my EPS functions input variables, and for multiple data sets, I used a n x 3 matrix, where n is the number of inputs, and the 3 columns correspond to the input varible (V,I,T).\
Ryan - The most difficult part of the TCS  subsystem was making sure the function code was in the correct directory to recall the information. After some trial and error, I was able to get the prompts and results that were expected. I learned how to run the code in and IDLE shell instead of my IDE, which gave a "cleaner" result without sending me down a continous loop like a .ipynb file did in PyCharm.

## 3. If you employed Generative AI tools, how did you do so? Discuss which tools you used, theprompts you utilized, how you ensured the results were valid, and how you integrated the code into your tasks.

Joshua - Most of the usage from AI was from ChatGPT, and it was used to enhance the way the code was already written. For C&DH, I needed to verify that the loop that was running to catch if the input was within the parameters accepted values was correct and return an error if not. I tried to incorporate something into the Payload code that I had never used before. I used AI to enhance the image quality of the 8-bit image using the Scipy library.\
Brian - I used copilot a handful of times, but it was done as a way to expedite finding an answer to a question, vice for generating code.  In other words, rather than sift through forums, the Mathworks wesite, or MATLAB documentation, I would ask the AI the question.  When I couldn't remember the proper format for making a MATLAB function with multipe outputs, I asked copilot, "how do i make a matlab function with multiple outputs," and it showed me the proper format without me having to sift through MATLAB documentation.\
Ryan - I used ChatGPT to troubleshoot my code. Originally I struggled with syntax errors because my code was written as pseudocode and I forgot to correct any items that I defined. I also had trouble with not having my results in the correct level of directory. ChatGPT may have led me down a road that I didn't want to go down at that point, which helped because it made me check more thoroughly on what I wrote vs what ChatGPT was suggesting.

## 4. What other resources did you use to find solutions? Online sites, books, references, etc.

Joshua - Any additional information that was used came from previously written code, websites like W3Schools, and some of my Python books that I used to initially learn the language.\
Brian - I used homeworks/labs from this, and other classes, to reference and reuse applicable code.  For example, referenced previous work to remember the format of the "fprintf" function, and to refresh on effective uses of "FOR" loops and "IF/ELSEIF/ELSE" statements.\

## 5. In what way could this project be improved for future quarters?

  Joshua - With six subsystems and four collaborators, maybe come up with two new subsystems so each person could work on two, and require that one be completed using Python and the other in Matlab.\
  Ryan - I liked the portion where we had to make our code and integrate it into a preexisting shell. It allowed us to understand how complex and useful simple code can be included into a more complex file.
















