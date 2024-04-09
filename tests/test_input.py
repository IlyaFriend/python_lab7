################################################
###        To tun tests, run `pytest`        ###
###        No files are needed, the test     ###
###        create files for themselves       ###
################################################

import sys
import pandas as pd
sys.path.append('../app/io')

from input import read_from_file_with_builtin, read_from_file_with_pandas

# Тестування функції read_from_file_with_builtin
def test_read_from_file_with_builtin_file_not_found():
    # Перевіряємо, що функція повертає None, якщо файл не знайдено
    assert read_from_file_with_builtin("nonexistent_file.txt") is None

# Тестування функції read_from_file_with_builtin
def test_read_from_file_with_builtin_empty_file(tmp_path):
    # Створюємо тестовий порожній файл
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Перевіряємо, що функція повертає пустий рядок, якщо файл порожній
    assert read_from_file_with_builtin(test_file) == ""

def test_read_from_file_with_builtin_file_found_2(tmp_path):
    # Створюємо тестовий файл з вмістом
    file_content = "Test content for file"
    test_file = tmp_path / "test_file.txt"
    with open(test_file, 'w') as file:
        file.write(file_content)
    
    # Перевіряємо, що функція повертає очікуваний вміст файлу
    assert read_from_file_with_builtin(test_file) == file_content

# Тестування функції read_from_file_with_pandas
def test_read_from_file_with_pandas_file_not_found():
    # Перевіряємо, що функція повертає None, якщо файл не знайдено
    assert read_from_file_with_pandas("nonexistent_file.csv") is None

# Тестування функції read_from_file_with_pandas
def test_read_from_file_with_pandas(tmp_path):
    # Створюємо тестовий файл з вмістом
    file_content = "A,B,C\n1,2,3\n4,5,6\n"
    test_file = tmp_path / "test_file.csv"
    with open(test_file, 'w') as file:
        file.write(file_content)
    
    # Очікувані дані, які повинні бути прочитані з файлу
    expected_data = pd.DataFrame({'A': [1, 4], 'B': [2, 5], 'C': [3, 6]})
    
    # Перевіряємо, чи дані зчитуються правильно
    assert read_from_file_with_pandas(test_file).equals(expected_data)

# Тестування функції read_from_file_with_pandas
def test_read_from_file_with_pandas_valid_data(tmp_path):
    # Створюємо тестовий файл з даними
    file_content = "A,B,C\n1,2,3\n4,5,6\n7,8,9\n"
    test_file = tmp_path / "valid_data_file.csv"
    with open(test_file, 'w') as file:
        file.write(file_content)
    
    # Очікувані дані, які мають бути прочитані з файлу
    expected_data = pd.DataFrame({'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]})
    
    # Перевіряємо, чи дані зчитуються правильно
    assert read_from_file_with_pandas(test_file).equals(expected_data)