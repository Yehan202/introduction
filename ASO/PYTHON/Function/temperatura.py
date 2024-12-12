import sys

temp = []

# Extract relevant numeric arguments
args = [float(arg) for arg in sys.argv[1:] if arg.replace('.', '', 1).isdigit()]

# Find max and min values from the numeric arguments
max_value = max(args)
min_value = min(args)

# Loop through arguments to process temperature values after "-t"
for j in range(1, len(sys.argv)):
    if sys.argv[j] == "-t":
        temp_value = float(sys.argv[j + 1])
        if temp_value == max_value or temp_value == min_value:
            continue  # Skip max and min values
        temp.append(temp_value)

# Print the temp list and calculate the average
print(temp)
if len(temp) > 0:
    temp_media = sum(temp) / len(temp)
    print(temp_media)
else:
    print("No valid temperatures to compute average.")
