def main():
  # Get an odometer value in U.S. miles from the user.
  start_def = int(input("Enter the amount of miles at the start: "))
  # Get another odometer value in U.S. miles from the user.
  end_def = int(input("Enter the amount of miles at the end: "))
  # Get a fuel amount in U.S. gallons from the user.
  gallons_total = int(input("Enter the total gallons on thr tank: "))
  # Call the miles_per_gallon function and store
  mpg = miles_per_gallon(start_def, end_def, gallons_total)
  # the result in a variable named mpg.
  # Call the lp100k_from_mpg function to convert the
  # miles per gallon to liters per 100 kilometers and
  # store the result in a variable named lp100k.
  lp100k = lp100k_from_mpg(mpg)
  # Display the results for the user to see.
  print(lp100k)
  pass
def miles_per_gallon(start_miles, end_miles, amount_gallons):
  """Compute and return the average number of miles
  that a vehicle traveled per gallon of fuel.
  Parameters
  start_miles: An odometer value in miles.
  end_miles: Another odometer value in miles.
  amount_gallons: A fuel amount in U.S. gallons.
  
  Return: Fuel efficiency in miles per gallon.
  """
  fuel_efficency = (end_miles - start_miles) / amount_gallons
  return fuel_efficency
def lp100k_from_mpg(mpg):
  """Convert miles per gallon to liters per 100
  kilometers and return the converted value.
  Parameter mpg: A value in miles per gallon
  Return: The converted value in liters per 100km.
  """
  convert = 235215 / mpg
  return mpg
# Call the main function so that
# this program will start executing.
main()