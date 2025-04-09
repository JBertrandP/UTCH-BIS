# Import the necessary libraries
import csv  # To read the CSV file
from collections import defaultdict  # To count occurrences of each brand

# First of all: Read the CSV file
# Open the CSV file and load the data into a list
responses = []  # Create an empty list to store the survey responses
with open("beer_survey_chihuahua.csv", "r", encoding="utf-8") as file:  # Open the CSV file in read mode
    reader = csv.reader(file)  # Create a CSV reader object to read the file
    next(reader)  # Skip the header row (Age, Beers per Week, Favorite Brand)
    for row in reader:  # Loop through each row in the CSV file
        responses.append(row)  # Add the row to the list

# Then we Analyze the data
# Create a dictionary to count how many people prefer each brand
brand_counts = defaultdict(int)  # A dictionary with default value 0 for any new key
# Create a variable to store the total number of beers consumed
total_beers = 0  # Initialize the total beers counter to 0

# Loop through each response
for response in responses:  # Loop through each row in the responses list
    age = int(response[0])  # Extract the age
    beers = int(response[1])  # Extract the number of beers per week and convert it to integer
    brand = response[2]  # Extract the favorite brand (it's already a string btw)

    # Update the count for the favorite brand
    brand_counts[brand] += 1  # Increment the count for this brand by 1
    # Add to the total number of beers consumed
    total_beers += beers  # Add the number of beers to the total

# We then display the results
# Print the total number of beers consumed
print(f"Total beers consumed per week by all respondents: {total_beers}")

# Print a table of the most popular brands
print("\nMost Popular Beer Brands:")  # Print a heading for the table
print("-" * 30)  # Print a line of dashes
# Use string formatting to align the columns
print(f"{'Brand':<15} {'Number of People':<15}")  # Print the table header with fixed-width columns
print("-" * 30)  # Print another line of dashes
for brand, count in brand_counts.items():  # Loop through each brand and its count
    print(f"{brand:<15} {count:<15}")  # Print the brand and count in columns
print("-" * 30)  # Print a final line of dashes