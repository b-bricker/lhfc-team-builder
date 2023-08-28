# LHFC Team Builder

This script can be used to build soccer teams across multiple age divisions keeping an even distribution of age and gender for each team.

## Usage

The script accepts 2 positional arguments:

- INPUT_FILE_PATH - a file path to a CSV with the raw roster info from SportsEngine, invalid paths will result in error
- CUTOFF_DATE - the cutoff date for determining age groups, formatted as MM/DD/YYYY

There is also 1 optional argument:

- -o --output - a file path for the output file, defaults to `roster.txt` if not provided

Examples assume that the user is operating from the root directory of this repo.

```bash
# with no output file provided, outputs to ./roster.txt
python3 ./src/main.py ./my_input.csv 10/31/2023

# with shorthand output file provided, outputs to ./my_output.txt
python3 ./src/main.py ./my_input.csv 10/31/2023 -o ./my_output.txt

# with longhand output file provided, outputs to ./my_output.txt
python3 ./src/main.py ./my_input.csv 10/31/2023 --output ./my_output.txt
```
