import numpy as np
import time
from multiprocessing import Pool, cpu_count

def process_batch(args):
    a_batch, b_values = args

    a_batch = a_batch[:, np.newaxis]
    b_batch = b_values[np.newaxis, :]

    conditions_a = (a_batch - 1) % (3 * b_batch - 1) == 0
    conditions_b = (b_batch - 1) % (3 * a_batch - 1) == 0

    valid_pairs = np.logical_and(conditions_a, conditions_b)

    valid_indices = np.where(valid_pairs)

    found_pairs_a = a_batch[valid_indices[0]]
    found_pairs_b = b_batch[valid_indices[1]]

    return list(zip(found_pairs_a, found_pairs_b))

def find_and_save_pairs(limit, filename, batch_size=10):
    start_time = time.time()  # Record the start time

    a_values = np.arange(2, limit)
    b_values = np.arange(2, limit)

    a_batches = [a_values[i:i+batch_size] for i in range(0, len(a_values), batch_size)]
    args_list = [(a_batch, b_values) for a_batch in a_batches]

    num_processes = min(cpu_count(), len(args_list))

    with Pool(num_processes) as pool:
        found_pairs_list = pool.map(process_batch, args_list)
        found_pairs = [pair for pairs in found_pairs_list for pair in pairs]

    end_time = time.time()  # Record the end time

    timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    updated_filename = f"limit{limit}_{filename}"

    with open(updated_filename, "w") as file:
        file.write(f"Upper Limit: {limit}\n")
        file.write(f"Elapsed Time: {end_time - start_time:.4f} seconds\n")
        file.write(f"Number of Pairs: {len(found_pairs)}\n")
        file.write(f"Timestamp: {timestamp_str}\n\n")

        for a_val, b_val in found_pairs:
            file.write(f"Pair found: a = {a_val}, b = {b_val}\n")

    elapsed_time = end_time - start_time
    print(f"Process completed in {elapsed_time:.4f} seconds")
    print(f"Pairs saved to: {updated_filename}")
    print(f"Number of Pairs: {len(found_pairs)}")

# Set the upper limit for 'a' and 'b'
upper_limit = 100_000
# Define the base output file name
file_name = "integer_pairs_results.txt"
# Call the function to find and save pairs
find_and_save_pairs(upper_limit, file_name)
