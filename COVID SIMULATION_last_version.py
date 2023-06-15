# Comments:

# The following code has two types of simulations where 
# the first one makes the tour given 2 parameters supplied
# by the user which are the number of people and the number of days.
# The parameters given by the exercise were not changed which
# means that the probability of dying is 0.02% and the probability 
# of spreading the virus is 10%
# On the other hand, the second simulation recovers the code until the entire 
# population becomes healthy since they acquired the virus, 
# it would be important to see in how many days all the people recover 
# and make the respective analyzes.

import random as rd
import math

# Function that counts the days of sick people
def get_count_days(list_people):
    
    for i in range(len(list_status_ppl)):
        
        # if people is sick, start counting days
        if list_status_ppl[i][0] == 1:
            # Add a day if the person is sick            
            list_status_ppl[i][1] += 1
    
    # Returns the number of days the person is sick
    return list_status_ppl

# Function that counts the number of people recovered after 10 days
def get_people_recovered(count_ppl_infected,N_population,list_status_ppl, infect):
    
    for i in range(len(list_status_ppl)):
        # If people are sick and them number of days is 10 then they become healthy
        if list_status_ppl[i][0] == 1 and list_status_ppl[i][1] == 10:
            list_status_ppl[i][0] = 0
            # Start the count of days from 0 again
            list_status_ppl[i][1] = 0
            # Subtract the number of infected people
            count_ppl_infected -= 1
            infect -= 1
            # Add again the person who was sick to the list of healthy people
            N_population += 1
    
    # Returns healthy people and infected people
    return count_ppl_infected, N_population, infect

# Function that counts the number of dead people
def get_people_dead(count_ppl_dead,count_ppl_infected,list_status_ppl, infect):
    
    for i in range(len(list_status_ppl)):
        
        # Random probability to compare with rate_mortality
        probability_dead = rd.random()
                    
        # If the probabilty is grater than rate_mortality then sick person die
        if list_status_ppl[i][0] == 1 and probability_dead < rate_mortality:
            # [2 == people dead]
            list_status_ppl[i][0] = 2
            # If the conditional is met, each dead person will be counted
            count_ppl_dead += 1
            # Subtract the number of infected people
            count_ppl_infected -= 1
            infect -= 1
    
    # Returns the dead people and the new total of infected people
    return count_ppl_dead, count_ppl_infected, infect

# The user must select the simulation he would like to evaluate
choice = int(input("Simulation 1 >> [Run the code with number of days]\nSimulation 2 >> [Run the code with infecctions until cero]\nEnter number of simulation: "))
# Ask the user for quantity of people he will test
N_population = int(input("Enter number of people: "))
# Parameter defined as 10% probability te get the virus after a infected person meet a healthy person
rate_of_infection = 10/100
# Parameter defined like 0.2% probability of dead
rate_mortality = 0.02/10
# List of healthy people
list_status_ppl = list()
# Counter of infected people
count_ppl_infected = 2
# Counter of dead people
count_ppl_dead = 0
# Counter of recovered people
count_ppl_recovered = 0
# Counter variable to evaluate the real number of infected people after giving 2 infected people as initial parameter
infect = 0

# status [0 = healthy], [1 = sick], [2 = dead]

# Substrad 2 people from population given the infected people must be in population
N_population -= 2

# Conditional to evaluate the development of infection in days
if choice == 1:
    
    # As the user for quantity of days he will evaluate the smulation
    n_days = int(input("Enter number of days: "))
    
    # Create the list of people from N_population
    for ppl1 in range(N_population):
        # list of people healthy
        list_status_ppl.append([0,0])
    
    # Loop to run each day        
    for n in range(n_days):
        
        # Print the situation of each day
        print("-------------day",n,"-------------")
        
        # Loop to run each sick people and evaluate how many the will met
        for ppl2 in range(0,count_ppl_infected):
            
            # Number of people who will be met by sick people [from 0 to 21]
            known_ppl = rd.randint(0,21)
                        
            # Loop to run each people met to evaluate if they get the virus or not
            for ppl3 in range(known_ppl):
                # Percentage to compare with 30% of probability to get the virus
                prob = rd.random()
                
                # Random position of people met by sick people of the list_status_ppl
                position_people_infected = rd.randint(0,N_population)
                
                # If random probability [prob] is grater than probability to get the virus [rate of infection] and people is healthy
                if prob < rate_of_infection and list_status_ppl[position_people_infected][0] == 0:
                    # The status of healthy people [0 = healthy], it has to be changed by 1 [1 = sick]
                    list_status_ppl[position_people_infected][0] = 1
                    # Counter to know the quantity of sick people
                    count_ppl_infected += 1
                    # Subtract people from healthy people counter
                    N_population -= 1
                    
        # Funtion to count days for each people either sick, healthy or dead            
        list_status_ppl = get_count_days(list_status_ppl)
        # Funtion to count recovered people if they have more than 10 days and they have not dead
        count_ppl_infected, N_population, infect = get_people_recovered(count_ppl_infected,N_population,list_status_ppl, infect)
        # Funtion to count quantity of people dead
        count_ppl_dead, count_ppl_infected, infect = get_people_dead(count_ppl_dead,count_ppl_infected,list_status_ppl, infect)
        
        # Print the number of infected people, recovered people and dead people
        print("Number of people infected >>",count_ppl_infected,"\nNumber of people recovered and healthy >>",N_population,"\nNumber of people dead >>",count_ppl_dead)
        # Print the total of people tested
        print("Total people tested: ",(count_ppl_infected+N_population+count_ppl_dead))

# Conditional to evalute the simulation until all of people become healthy after getting the virus
if choice == 2:
    
    # Index to count the number of days
    n = 0
    # Variable to count the sick people
    infect = 0
    # Subtract 2 people sick from population
    N_population -= 2

    # Create the list of people from N_population
    for ppl1 in range(N_population):
        # list of people healthy
        list_status_ppl.append([0,0])
    
    # Until all of people who were initially infected become healthy
    while infect >= 0:
        
        # Validate that number of infected people is cero after 100 days
        if n > 100 and infect == 0:
            
            # Become the counter of sick people in 0
            count_ppl_infected = 0
            # Break the loop if this condition is true
            break
        
        else:
            # Count the number of days until the condition decribed is met
            n += 1
            # Print the situation of each day
            print("-------------day",n,"-------------")
            
            # Loop to run each sick people and evaluate how many the will met
            for ppl2 in range(0,count_ppl_infected):
                
                # Number of people who will be met by sick people [from 0 to 21]
                known_ppl = rd.randint(0,21)
                
                
                # Loop to run each people met to evaluate if they get the virus or not
                for ppl3 in range(known_ppl):
                    # Percentage to compare with 30% of probability to get the virus
                    prob = rd.random()
                    # Random position of people met by sick people of the list_status_ppl
                    position_people_infected = rd.randint(0,N_population)
                    
                    # If random probability [prob] is grater than probability to get the virus [rate of infection] and people is healthy
                    if prob < rate_of_infection and list_status_ppl[position_people_infected][0] == 0:
                        # The status of healthy people [0 = healthy], it has to be changed by 1 [1 = sick]
                        list_status_ppl[position_people_infected][0] = 1
                        # Counter to know the quantity of sick people
                        count_ppl_infected += 1
                        infect += 1
                        # Subtract people from healthy people counter
                        N_population -= 1
                        
        # Funtion to count days for each people either sick, healthy or dead         
        list_status_ppl = get_count_days(list_status_ppl)
        # Funtion to count recovered people if they have more than 10 days and they have not dead
        count_ppl_infected, N_population, infect = get_people_recovered(count_ppl_infected,N_population,list_status_ppl, infect)
        # Funtion to count quantity of people dead
        count_ppl_dead, count_ppl_infected, infect = get_people_dead(count_ppl_dead,count_ppl_infected,list_status_ppl, infect)
        
        # Print the number of infected people, recovered people and dead people
        print("Number of people infected >>",infect,"\nNumber of people recovered and healthy >>",N_population,"\nNumber of people dead >>",count_ppl_dead)
    