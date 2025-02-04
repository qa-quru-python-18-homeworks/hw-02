import os

def read_file(file_path):
    """Reads the content of a file and returns it as a list of lines."""
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def process_data(lines):
    """Processes the data."""
    return [line for line in lines]

def write_file(file_path, lines):
    """Writes the processed lines to a new file."""
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    # Read the input file
    lines = read_file(input_file)
    if not lines:
        return
    
    # Process the data
    processed_lines = process_data(lines)
    
    # Write the processed data to the output file
    write_file(output_file, processed_lines)
    print(f"Processed data has been written to {output_file}")

if __name__ == "__main__":
    main()