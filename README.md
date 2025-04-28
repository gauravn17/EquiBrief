# GRhesearch
AI Summarizer of Stocks

An AI-powered tool that extracts and summarizes key financial information from Indian companies’ annual reports, earnings call transcripts, and investor presentations.

✅ Designed to make important financial insights affordable and accessible for small finance firms, NBFCs, and individual analysts — without the high costs of platforms like Bloomberg or FactSet.

💡 Why This Matters

Financial data should be accessible, not a luxury.

This tool democratizes access to structured insights for emerging finance professionals, startups, and smaller funds who need reliable data — without paying $25,000 a year.
⸻

🚀 Project Goals
	•	Parse public documents (PDFs/text) from company websites, NSE/BSE, etc.
	•	Extract critical financial data:
	•	Revenue, Net Profit, Growth Rates
	•	Loan Book Size (for banks/NBFCs)
	•	Gross and Net NPA figures
	•	Management commentary and outlook
	•	Expansion plans and key risks
	•	Deliver clean, structured summaries ready for quick analysis.
	•	Build a low-cost, scalable alternative to expensive data platforms.

🧩 Implementation Details

The AI Stock Summarizer works in a modular pipeline, broken down into three major stages:

1. Data Ingestion
	•	Source: Publicly available documents such as annual reports, earnings call transcripts, and investor presentations from Indian company websites, NSE/BSE filings.
	•	Files are manually downloaded (initial MVP) into the /data/ folder.

2. Document Parsing
	•	Text Extraction: Use pdfplumber to extract text cleanly from structured PDFs.
	•	OCR (optional): For scanned or image-based PDFs, fallback to OCR solutions like pytesseract.

3. Financial Information Summarization
	•	Prompt-based LLM Summarization: Send extracted text to OpenAI’s GPT models (gpt-4o or gpt-3.5-turbo) using custom finance-focused prompts.
	•	Output: Extract structured key metrics:
	•	Revenue, Profit, Growth %
	•	Gross and Net NPAs (for banks/NBFCs)
	•	Management Tone/Outlook
	•	Expansion/Risk commentary

4. Data Storage
	•	Summaries are saved as:
	•	Text summaries
	•	JSON files for structured data
	•	(Later) Could be inserted into a database (Postgres/SQLite)

5. Frontend Display 
	•	Simple Flask + React dashboard or CSV download.
	•	Features: Search by Company, Sector, Time Period, Financial Metrics.

🏛️ System Design Flow

Here’s the end-to-end architecture of the system:

[Public Reports (PDFs)] 
          ↓ 
[PDF Parser (pdfplumber)]
          ↓ 
[Extracted Raw Text]
          ↓ 
[Summarizer Engine (OpenAI GPT)]
          ↓ 
[Financial Summary (structured JSON/text)]
          ↓ 
[Storage (CSV/JSON/Database)]
          ↓ 
[Frontend Dashboard (Optional - Flask/React)]

📦 Quick Example (Full Path)

Input:  AU Small Finance Bank FY24 Annual Report.pdf
    ↓
Extract text via pdfplumber
    ↓
Send to GPT-4o:
    "Extract Revenue, Net Profit, NPAs, Management Outlook"
    ↓
Receive structured summary
    ↓
Save into `summaries/au_small_finance_bank_2024.json`
    ↓
Display in dashboard or export CSV for analysis
