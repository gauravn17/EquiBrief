from scripts.pdf_parser import extract_text_from_pdf
from scripts.summarizer import summarize_text
def main():
    pdf_path = "data/sample_report.pdf"  # path to your PDF

    print("[INFO] Extracting text from PDF...")
    extracted_text = extract_text_from_pdf(pdf_path)

    print("[INFO] Summarizing financial data...")
    summary = summarize_text(extracted_text)

    print("\n=== Financial Summary ===")
    print(summary)

if __name__ == "__main__":
    main()