import pdfplumber


def extract_text_from_pdf(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text

if __name__ == "__main__":
    text = extract_text_from_pdf("krishi valleru resume(edited) copy.pdf")
    print(text[:1000])