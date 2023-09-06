import PyPDF2
import re

def find_vowel_words(text):
    words = re.findall(r'\b[aeiouAEIOU][a-zA-Z]*\b', text)
    return words

def main():
    input_pdf_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\SQLCompleteStudyNotes.pdf'
    output_txt_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\output.txt'

    # Read text from the PDF file
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()

    # Find words starting with vowels
    vowel_words = find_vowel_words(text)

    # Write vowel words to the output file
    with open(output_txt_path, 'w') as output_file:
        for word in vowel_words:
            output_file.write(word + '\n')

    print(f"Vowel words written to {output_txt_path}")

if __name__ == "__main__":
    main()
