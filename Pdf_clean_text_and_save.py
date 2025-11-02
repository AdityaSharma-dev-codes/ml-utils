import fitz
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download required NLTK data once and then comment out for further runs
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return words

def save_cleaned_text_to_file(cleaned_words, output_path="cleaned_text.txt"):
    # Save cleaned tokens to a file (one token per line).

    if not isinstance(cleaned_words, (list, tuple)):
        raise TypeError("cleaned_words must be a list or tuple of tokens")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(map(str, cleaned_words)))

    print(f"Cleaned words saved to {output_path}")

# Usage
pdf_file = r"D:\Downloads\Final Assessment - Viewer Page _ Infosys Springboard.pdf"
raw_text = extract_text_from_pdf(pdf_file)
cleaned_text = clean_text(raw_text)
save_cleaned_text_to_file(cleaned_text, output_path="cleaned_text.txt")