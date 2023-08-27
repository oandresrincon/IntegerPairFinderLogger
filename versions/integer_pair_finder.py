import os
import time

def find_and_save_pairs(limit, filename):
    found_pairs = []

    start_time = time.time()  # Record the start time

    # Pre-calculate constants for efficiency
    for a in range(2, limit):
        a_const = 3 * a - 1  # Calculate the constant for 'a'
        for b in range(2, limit):
            b_const = 3 * b - 1  # Calculate the constant for 'b'

            # Check the conditions for the pairs using pre-calculated constants
            if (a - 1) % b_const == 0 and (b - 1) % a_const == 0:
                found_pairs.append((a, b))

    end_time = time.time()  # Record the end time

    timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Create a folder if it doesn't exist
    folder_name = "results_folder"
    os.makedirs(folder_name, exist_ok=True)

    updated_filename = os.path.join(folder_name, f"{filename}_limit{limit}.txt")

    # Use a list comprehension to generate the pairs string
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
    print(f"Pairs saved to: {updated_filename}")

# Set the upper limit for 'a' and 'b'
upper_limit = 1000
# Define the base output file name
file_name = "integer_pairs_results"
# Call the function to find and save pairs
find_and_save_pairs(upper_limit, file_name)
