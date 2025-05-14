import sys
import logging
from scripts.pdf_parser import extract_text_from_pdf
from scripts.summarizer import summarize_text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    pdf_path = sys.argv[1] if len(sys.argv) > 1 else "data/sample_report.pdf"

    logger.info("Extracting text from PDF...")
    try:
        extracted_text = extract_text_from_pdf(pdf_path)
        if not extracted_text.strip():
            raise ValueError("PDF appears to be empty or unreadable.")
    except Exception as e:
        logger.error(f"Failed to extract text: {e}")
        return

    logger.info("Summarizing financial data...")
    summary = summarize_text(extracted_text)

    print("\n=== Financial Summary ===")
    print(summary)

    with open("data/summary_output.txt", "w") as f:
        f.write(summary)

if __name__ == "__main__":
    main()
