import random                                                         #
import time                                                           #
target_temp = random.randint(-30, 60)                                 #
print(f"Your target temperature for this iteration is {target_temp}") #
############ DO NOT EDIT ABOVE THIS LINE ##############################

def process_temperature(input_temp, target_temp):
    """Function that takes an input temperature and target temperature
    applies a function to move it towards equilibrium.
    It should return a single float as the output indicating 
    the new, altered temperature"""

############ MY CODE #########################################################
    delta_t = target_temp-input_temp   #4.3.2 Finds difference         s #
    print(f"Your total desired change in temperature is {delta_t}")          #
    change_t = delta_t * 0.25   #4.3.4 How much my TCS is changing t by      #
    print(f"25% of change in temperature for this iteration is {change_t}")  #
    new_t = input_temp + change_t   #4.3.3 Changes t by 25%                  #
    return new_t   #return new t                                     #
                                                                             #
input_temp = float(10)   #4.3.1 current temp                                #
#target_temp = float(20)     #4.3.1 desired temp                             #
print(f"Your current temperature for this iteration is {input_temp}")       #
#print(f"Your target temperature for this iteration is {target_temp}")       #
                                                                             #
#new_temper = process_temperature(input_temp, target_temp)  #Calling function      #
print(f"Your new current temperature is {new_t}")                            #
##############################################################################


################### DO NOT EDIT THIS PORTION ############################
def main():                                                             #
    duration = 15      # Duration to feed signals in seconds            #                              #
    sequence = []                                                       #
    i = 0                                                               #
    temperature = random.randint(-30, 60)                               #
    while True:                                                         #
        direction = random.choice([-1, 1])                              #
        change = random.uniform(0, 2) * direction                       #
        new_temperature = max(-30, min(60, temperature + change))       #
        print(f"New temperature reading: {new_temperature:.2f}")        #
        temperature = process_temperature(new_temperature,target_temp)  #
        time.sleep(1)  # Wait for 1 second before the next signal       #
        sequence.append(temperature)                                    #
        i += 1                                                          #
        if i > duration:                                                #
            print(sequence)                                             #
            exit()                                                      #
if __name__ == "__main__":                                              #
    main()                                                              #
#########################################################################
