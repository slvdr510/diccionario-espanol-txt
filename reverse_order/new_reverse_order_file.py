def reverse_words_in_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            reversed_word = line.strip()[::-1]
            file.write(reversed_word + '\n')

if __name__ == "__main__":
    input_file = '0_palabras_todas.txt'  # Replace with your input file path
    partes_input_file = input_file.split('.')
    input_file_primera_parte = file=partes_input_file[0]
    output_file = input_file_primera_parte + '_del_reves.txt'
    reverse_words_in_file(input_file, output_file)