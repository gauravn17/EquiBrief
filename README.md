# 📊 EquiBrief – AI Summarizer of Stocks
![EquiBrief logo](https://github.com/user-attachments/assets/3c53c24d-ded2-46bc-b4b4-8dbe27d528be)

An AI-powered tool that **extracts and summarizes key financial insights** from Indian companies’ **annual reports**, **earnings call transcripts**, and **investor presentations**.

---

### ✅ Mission
Make financial intelligence **affordable and accessible** for:
- Small finance firms
- NBFCs
- Individual analysts

💸 Say goodbye to expensive platforms like Bloomberg and FactSet.

---

### 💡 Why This Matters
> Financial data should be accessible — not a luxury.

EquiBrief democratizes access to structured insights for:
- Emerging finance professionals  
- Startups  
- Small funds  

...who need **reliable data without paying $25,000/year**.

---

### 🚀 Project Goals
- 🔍 Parse public documents from company websites, NSE/BSE
- 📊 Extract key financial data:
  - Revenue, Net Profit, Growth Rates  
  - Loan Book Size (banks/NBFCs)  
  - Gross & Net NPA figures  
  - Management commentary and future outlook  
  - Expansion plans and risk disclosures
- 🧾 Deliver clean, structured summaries ready for analysis
- 💻 Build a **low-cost**, **scalable** alternative to expensive platforms

---

### 🧩 Implementation Overview

#### 1. Data Ingestion
- **Source**: Annual reports, earnings calls, investor decks  
- **Input**: PDFs or text files, manually downloaded into the `/data/` folder (MVP)

#### 2. Document Parsing
- **Text Extraction**: Use `pdfplumber` for clean text from structured PDFs  
- **OCR (Fallback)**: Use `pytesseract` for scanned or image-based reports

#### 3. Summarization Engine
- **LLM-based Extraction**: Send parsed text to GPT-4o / GPT-3.5-Turbo  
- **Custom Prompts**: Finance-specific templates to extract:
  - Revenue, Profit, Growth %  
  - Gross/Net NPAs (for banks/NBFCs)  
  - Management Tone / Strategic Outlook  
  - Expansion & Risk commentary

#### 4. Data Storage
- Save summaries as:
  - 📄 Text summaries  
  - 🔧 JSON (for structured data)  
  - (Optional) Insert into Postgres / SQLite

#### 5. Frontend Display
- 🔧 Simple Flask + React dashboard *(or)* CSV download
- 🔍 Search by: Company, Sector, Year, Metrics

---

### 🏛️ System Architecture

```
[Public Reports (PDFs)]
          ↓
 [PDF Parser – pdfplumber]
          ↓
   [Extracted Raw Text]
          ↓
 [Summarizer – GPT-4o/GPT-3.5]
          ↓
  [Structured Summary: JSON/Text]
          ↓
 [Storage – CSV, JSON, Database]
          ↓
 [Frontend Dashboard – Flask/React]
```

---

### 📦 Example Workflow

> Input: `AU_Small_Finance_Bank_FY24_Annual_Report.pdf`

1. Extract text via `pdfplumber`  
2. Send to GPT-4o:  
   _"Extract Revenue, Net Profit, NPAs, Management Outlook"_  
3. Receive structured summary  
4. Save as: `summaries/au_small_finance_bank_2024.json`  
5. View in dashboard or export to CSV
"""

# Save to a file
output_path = Path("/mnt/data/README_EquiBrief.md")
output_path.write_text(readme_content.strip())

output_path.name
