from app.io.input import input_text_from_console, read_from_file_with_builtin, read_from_file_with_pandas
from app.io.output import output_text_to_console, write_to_file_with_builtin

def main():
    # Call the function to input text from the console
    console_text = input_text_from_console()

    # Print the console text to the console both with print and output_text_to_console
    print("print:", console_text)
    output_text_to_console(console_text)
    print('_________________________________________\n')

    # Write the console text to a file
    write_to_file_with_builtin("data/test.txt", console_text)

    # Call the function to read from a file using Python's built-in capabilities
    file_content_builtin = read_from_file_with_builtin("data/test.txt")

    # Print the file content (read using built-in capabilities) to the console
    print("File content (built-in):", file_content_builtin)
    output_text_to_console(file_content_builtin)
    print('_________________________________________\n')
    
    # Call the function to read from a file using pandas
    file_data_pandas = read_from_file_with_pandas("data/file_data_pandas_input.csv")

    # Print the file data (read using pandas) to the console
    print("File data (pandas):\n", file_data_pandas)

    # Write the file data (read using pandas) to a file (as CSV)
    file_data_pandas.to_csv("data/file_data_pandas_output.csv", index=False)

if __name__ == "__main__":
    main()
