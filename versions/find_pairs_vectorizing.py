import numpy as np
import time

def find_and_save_pairs(limit, filename):
    start_time = time.time()  # Record the start time

    a_values = np.arange(2, limit)
    b_values = np.arange(2, limit)

    # Create 2D arrays for 'a' and 'b' using broadcasting
    a = a_values[:, np.newaxis]
    b = b_values[np.newaxis, :]

    conditions_a = (a - 1) % (3 * b - 1) == 0
    conditions_b = (b - 1) % (3 * a - 1) == 0

    # Use np.logical_and to combine boolean conditions
    valid_pairs = np.logical_and(conditions_a, conditions_b)

    # Flatten and get indices of valid pairs
    valid_indices = np.where(valid_pairs)

    found_pairs_a = a_values[valid_indices[0]]
    found_pairs_b = b_values[valid_indices[1]]

    end_time = time.time()  # Record the end time

    timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    updated_filename = f"limit{limit}_{filename}"

    with open(updated_filename, "w") as file:
        file.write(f"Upper Limit: {limit}\n")
        file.write(f"Elapsed Time: {end_time - start_time:.4f} seconds\n")
        file.write(f"Number of Pairs: {len(found_pairs_a)}\n")
        file.write(f"Timestamp: {timestamp_str}\n\n")

        for a_val, b_val in zip(found_pairs_a, found_pairs_b):
            file.write(f"Pair found: a = {a_val}, b = {b_val}\n")

    elapsed_time = end_time - start_time
    print(f"Process completed in {elapsed_time:.4f} seconds")
    print(f"Pairs saved to: {updated_filename}")

# Set the upper limit for 'a' and 'b'
upper_limit = 50_000
# Define the base output file name
file_name = "integer_pairs_results.txt"
# Call the function to find and save pairs
find_and_save_pairs(upper_limit, file_name)
