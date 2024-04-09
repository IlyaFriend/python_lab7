from input import input_text_from_console, read_from_file_with_builtin, read_from_file_with_pandas
from output import output_text_to_console, write_to_file_with_builtin

def main():
    # Ввод тексту з консолі
    text_from_console = input_text_from_console()
    print("Text from console:", text_from_console)
    output_text_to_console()
    write_to_file_with_builtin(text_from_console)

    # Зчитування з файлу за допомогою вбудованих можливостей Python
    text_from_builtin = read_from_file_with_builtin()
    print("Text from file with built-in:", text_from_builtin)
    output_text_to_console()
    write_to_file_with_builtin(text_from_builtin)

    # Зчитування з файлу за допомогою бібліотеки pandas
    data_from_pandas = read_from_file_with_pandas()
    print("Data from file with pandas:", data_from_pandas)
    output_text_to_console()
    write_to_file_with_builtin(data_from_pandas)

if __name__ == "__main__":
    main()
