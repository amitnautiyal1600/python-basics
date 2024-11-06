import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_large_data_file(file_path, num_lines, line_length):
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            line = generate_random_string(line_length) + '\n'
            file.write(line)

generate_large_data_file('large_data.csv', 1000000, 100)