def input_text_from_console():
    """
    Function for inputting text from the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Enter text from the console: ")


def read_from_file_with_builtin(filename):
    """
    Function for reading from a file using Python's built-in capabilities.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: The content of the file.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not found!")
        return None

def read_from_file_with_pandas(filename):
    """
    Function for reading from a file using the pandas library.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        DataFrame: A DataFrame object containing the data from the file.
    """
    import pandas as pd
    try:
        data = pd.read_csv(filename)  # Assuming the file is in CSV format
        return data
    except FileNotFoundError:
        print("File not found!")
        return None
