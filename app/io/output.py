def output_text_to_console(text):
    """
    Function for outputting text to the console.

    Args:
        text (str): The text to be outputted.
    """
    print("Output text to console:", text)

def write_to_file_with_builtin(filename, text):
    """
    Function for writing to a file using Python's built-in capabilities.

    Args:
        text (str): The text to be written to the file.
    """
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print("Data written to file successfully!")
    except FileNotFoundError:
        print("File not found!")
