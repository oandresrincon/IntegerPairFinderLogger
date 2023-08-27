import numpy as np
import time
import os

def find_and_save_pairs(limit, filename):
    # Record the start time
    start_time = time.time()

    # Generate arrays of values for 'a' and 'b'
    a_values = np.arange(2, limit)
    b_values = np.arange(2, limit)

    # Create a folder to store results
    folder_name = "pairs_results_folder"
    os.makedirs(folder_name, exist_ok=True)
    updated_filename = os.path.join(folder_name, f"{filename}_{limit}.txt")

    # Open the result file for writing
    with open(updated_filename, "w") as file:
        file.write(f"Upper Limit: {limit}\n")
        file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n\n")

        # Loop over values of 'a'
        for a in a_values:
            # Check conditions for 'b' using vectorized operations
            conditions_a = (a - 1) % (3 * b_values - 1) == 0
            found_b_values = b_values[conditions_a]

            # Check conditions for 'a' using vectorized operations on found 'b' values
            conditions_b = (found_b_values - 1) % (3 * a - 1) == 0
            found_pairs_b = found_b_values[conditions_b]

            # If valid pairs are found for this 'a' value
            if len(found_pairs_b) > 0:
                for b in found_pairs_b:
                    file.write(f"Pair found: a = {a}, b = {b}\n")

    # Record the end time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Append elapsed time to the result file
    with open(updated_filename, "a") as file:
        file.write(f"\nElapsed Time: {elapsed_time:.4f} seconds\n")

    # Print summary
    print(f"Upper Limit: {limit}")
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    print(f"Process completed in {elapsed_time:.4f} seconds")
    print(f"Pairs saved to: {updated_filename}")

# Set the upper limit for 'a' and 'b'
upper_limit = 50_000
# Define the base output file name
file_name = "pairs"
# Call the function to find and save pairs
find_and_save_pairs(upper_limit, file_name)
