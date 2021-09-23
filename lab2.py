# Lab Number: 2
# Program Inputs: Births per second (float), deaths per second (float), migration per second (float),
# Program Inputs (2): Current population (integer), number of years in future (float)
# Program Outputs: Estimated population (integer)

# This block asks the user for the three inputs that change population.
perSecondBirths = input('How many births per second occur in this country?')
perSecondDeaths = input('How many deaths per second occur in this country?')
perSecondMigration = input('What is the migration per second of this country? \n(If more people leave then enter, you may enter a negative value.)')

# This block asks the user for the current population and the number of years in the future they want to see.
currentPopulation = input('What is the current population of this country?')
futureYears = input('How many years in the future would you like this estimate?')

# This line adds all of the population changing effects into one number.
# Then it converts that number from per seconds into per years (which is the unit we're working with).
# There are 60 seconds in a minute, 60 minutes in an hour, 24 hours in a day, 365 days in a year.
# So the product of those numbers is how many seconds there are in a year.
perYearPopulationChange = 60 * 60 * 24 * 365 * ((float(perSecondBirths) - float(perSecondDeaths)) + float(perSecondMigration))

# The estimated population is the current population plus the net change over the next number of years.
estimatedPopulation = int(int(currentPopulation) + (perYearPopulationChange * float(futureYears)))

# Since countries cannot have a negative population, this line will put a floor cap on the output at 0.
if estimatedPopulation <= 0:
    print('The population of this country will eventually die out.')
# If there is more than 0 people in the country (a positive number) after so many years, the program will output it.
else:
    print('The estimated population of this country in', futureYears, 'years will be ' + str(estimatedPopulation) + '.')
