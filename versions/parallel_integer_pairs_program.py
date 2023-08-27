import os
import time
import multiprocessing

def find_pairs_for_range(start_a, end_a, limit):
    found_pairs = []

    for a in range(start_a, end_a):
        a_const = 3 * a - 1
        for b in range(2, limit):
            b_const = 3 * b - 1

            if (a - 1) % b_const == 0 and (b - 1) % a_const == 0:
                found_pairs.append((a, b))

    return found_pairs

def find_and_save_pairs(limit, filename, num_processes):
    start_time = time.time()  # Record the start time

    pool = multiprocessing.Pool(processes=num_processes)
    results = []

    chunk_size = (limit - 2) // num_processes
    for i in range(num_processes):
        start_a = 2 + i * chunk_size
        end_a = start_a + chunk_size if i != num_processes - 1 else limit
        results.append(pool.apply_async(find_pairs_for_range, (start_a, end_a, limit)))

    pool.close()
    pool.join()

    found_pairs = []
    for result in results:
        found_pairs.extend(result.get())

    end_time = time.time()  # Record the end time

    timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    folder_name = "results_folder"
    os.makedirs(folder_name, exist_ok=True)
    updated_filename = os.path.join(folder_name, f"{filename}_limit{limit}.txt")

    pairs_str = "\n".join([f"Pair found: a = {pair[0]}, b = {pair[1]}" for pair in found_pairs])

    with open(updated_filename, "w") as file:
        file.write(f"Upper Limit: {limit}\n")
        file.write(f"Elapsed Time: {end_time - start_time:.4f} seconds\n")
        file.write(f"Number of Pairs: {len(found_pairs)}\n")
        file.write(f"Timestamp: {timestamp_str}\n\n")
        file.write(pairs_str)  # Write the pairs string

    elapsed_time = end_time - start_time
    print(f"Process completed in {elapsed_time:.4f} seconds")
    print(f"Number of Pairs: {len(found_pairs)}")
    print(f"Number of available CPU cores: {num_processes}")
    print(f"Pairs saved to: {updated_filename}")

if __name__ == "__main__":
    # Set the upper limit for 'a' and 'b'
    upper_limit = 100_000
    # Define the base output file name
    file_name = "integer_pairs_results"
    # Define the number of processes to use
    num_processes = multiprocessing.cpu_count()  # Use all available CPU cores

    # Call the parallel function to find and save pairs
    find_and_save_pairs(upper_limit, file_name, num_processes)
