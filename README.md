# Pairs Finding and Saving

This Python script finds pairs of integers (a, b) that satisfy specific conditions and saves them to a text file

## Description

This program searches for integer pairs (a, b) within specified limits that satisfy the following conditions:
- (a - 1) % (3 * b - 1) == 0
- (b - 1) % (3 * a - 1) == 0

It then calculates various statistics about the process and the results, including the number of pairs found and the elapsed time. The results are saved to a text file with a name based on the provided filename and the upper limit of the search.

## Requirements

- Python version 3.10.6 (used in this script)
- NumPy library
- tqdm library

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt

## Usage

1. Install Python if not already installed.

2. Save the program code to a file named `find_pairs_integers.py`.

3. Open a terminal or command prompt

4. Navigate to the directory where the `find_pairs_integers.py` file is located.

5. Run the program using the command:
   ```bash
  python find_pairs_integers.py

## Customization

You can customize the program's behavior by modifying the following variables in the code:

- upper_limit: Set the upper limit for 'a' and 'b' when searching for pairs.
- file_name: Specify the base output file name for saving results.

For example, you can set upper_limit to control the range of values to search for pairs, and you can modify file_name to change the name of the output file.

## Output

The program will display the following information:

- Elapsed time taken to run the program.
- Number of pairs found.
- Name of the file where the pairs are saved.

## Author

Oscar Rincon
