import numpy as np
import time

def find_and_save_pairs(limit, filename):
    start_time = time.time()  # Record the start time

    found_pairs = []

    a_values = np.arange(2, limit)
    b_values = np.arange(2, limit)

    for a in a_values:
        conditions_b = (b_values - 1) % (3 * a - 1) == 0
        valid_b_indices = np.where(conditions_b)[0]

        if valid_b_indices.size > 0:
            valid_b_values = b_values[valid_b_indices]
            conditions_a = (a - 1) % (3 * valid_b_values - 1) == 0
            valid_a_values = np.repeat(a, conditions_a.sum())
            found_pairs.extend(zip(valid_a_values, valid_b_values))

    end_time = time.time()  # Record the end time

    timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    updated_filename = f"limit{limit}_{filename}"

    with open(updated_filename, "w") as file:
        file.write(f"Upper Limit: {limit}\n")
        file.write(f"Elapsed Time: {end_time - start_time:.4f} seconds\n")
        file.write(f"Number of Pairs: {len(found_pairs)}\n")
        file.write(f"Timestamp: {timestamp_str}\n\n")

        #for a_val, b_val in found_pairs:
        #    file.write(f"Pair found: a = {a_val}, b = {b_val}\n")

    elapsed_time = end_time - start_time
    print(f"Process completed in {elapsed_time:.4f} seconds")
    print(f"Pairs saved to: {updated_filename}")

# Set the upper limit for 'a' and 'b'
upper_limit = 100_000
# Define the base output file name
file_name = "integer_pairs_results.txt"
# Call the function to find and save pairs
find_and_save_pairs(upper_limit, file_name)
