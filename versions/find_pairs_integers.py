import numpy as np
import time
import os
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

def find_pairs_for_a(a, b_values):
    conditions_a = (3 * b_values - 1) % (a - 1) == 0
    found_b_values = b_values[conditions_a]

    conditions_b = (3 * a - 1) % (found_b_values - 1) == 0
    found_pairs_b = found_b_values[conditions_b]

    pairs = [(a, b) for b in found_pairs_b]
    return pairs

def process_a(a):
    pairs = find_pairs_for_a(a, b_values)
    with open(updated_filename, "a") as file:
        for a, b in pairs:
            file.write(f"Pair found: a = {a}, b = {b}\n")
    return len(pairs)  # Return the count of pairs found for this 'a'

def find_and_save_pairs(limit, filename):
    start_time = time.time()

    a_values = np.arange(2, limit)
    global b_values
    b_values = np.arange(2, limit)

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    folder_name = "pairs"
    os.makedirs(folder_name, exist_ok=True)
    global updated_filename
    updated_filename = os.path.join(folder_name, f"{limit}_{timestamp}.txt")

    with open(updated_filename, "w") as file:
        file.write(f"Upper Limit: {limit}\n")
        file.write(f"Timestamp: {timestamp}\n\n")

    num_processes = cpu_count()
    with Pool(num_processes) as pool:
        # Use the map function to collect the number of pairs found for each 'a'
        pair_counts = list(tqdm(pool.imap(process_a, a_values), total=len(a_values), desc="Finding pairs"))

    # Calculate the total number of pairs found
    total_pairs_found = sum(pair_counts)

    end_time = time.time()
    elapsed_time = end_time - start_time

    with open(updated_filename, "a") as file:
        # Write the total number of pairs found to the file
        file.write(f"\nTotal Pairs Found: {total_pairs_found}\n")
        file.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")

    print(f"Upper Limit: {limit}")
    print(f"Timestamp: {timestamp}")
    print(f"Process completed in {elapsed_time:.4f} seconds")
    print(f"Total Pairs Found: {total_pairs_found}")
    print(f"Pairs saved to: {updated_filename}")

# Set the upper limit for 'a' and 'b'
upper_limit = 1000_000
# Call the function to find and save pairs
find_and_save_pairs(upper_limit, "pairs_parallel.txt")
