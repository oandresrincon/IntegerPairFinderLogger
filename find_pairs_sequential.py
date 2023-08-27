import numpy as np
import time
import os
from tqdm import tqdm

def find_pairs_for_a(a, b_values):
    conditions_a = (3 * b_values - 1) % (a - 1) == 0
    found_b_values = b_values[conditions_a]

    conditions_b = (3 * a - 1) % (found_b_values - 1) == 0
    found_pairs_b = found_b_values[conditions_b]

    pairs = [(a, b) for b in found_pairs_b]
    return pairs

def find_and_save_pairs(limit, filename):
    start_time = time.time()

    a_values = np.arange(2, limit)
    b_values = np.arange(2, limit)

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    folder_name = "pairs"
    os.makedirs(folder_name, exist_ok=True)
    updated_filename = os.path.join(folder_name, f"{limit}_{timestamp}.txt")

    pair_count = 0  # Initialize pair count

    with open(updated_filename, "w") as file:
        file.write(f"Upper Limit: {limit}\n")
        file.write(f"Timestamp: {timestamp}\n")

        # Create a progress bar for the loop over 'a' values
        for a in tqdm(a_values, desc="Finding pairs"):
            pairs = find_pairs_for_a(a, b_values)

            if len(pairs) > 0:
                for a, b in pairs:
                    file.write(f"Pair found: a = {a}, b = {b}\n")
                    pair_count += 1

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time

    with open(updated_filename, "a") as file:
        file.write(f"\nTotal Pairs Found: {pair_count}\n")
        file.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")
        file.write(f"Total Pairs Found: {pair_count}")

    print(f"Upper Limit: {limit}")
    print(f"Timestamp: {timestamp}")
    print(f"Process completed in {elapsed_time:.4f} seconds")
    print(f"Total Pairs Found: {pair_count}")
    print(f"Pairs saved to: {updated_filename}")

# Set the upper limit for 'a' and 'b'
upper_limit = 1000_000
# Define the base output file name
file_name = "pairs"
# Call the function to find and save pairs
find_and_save_pairs(upper_limit, file_name)
