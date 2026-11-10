# Network Traffic Log Analyzer

A Python-based Data Engineering pipeline that automates the ingestion, parsing, and cleaning of raw Apache server logs.

## 🚀 Project Objective
The main goal of this project is to build an automated Data Engineering pipeline. It takes unstructured, raw server logs (Apache Common Log Format) and transforms them into a structured, clean CSV dataset ready for Data Analysis and BI Dashboards.

## ⚙️ Architecture & Workflow
1. **Ingestion**: Reads raw `.log` files from the `data/` directory.
2. **Parsing**: Uses Regular Expressions (Regex) to extract key fields (IP, Timestamp, HTTP Method, Endpoint, Status Code, Size).
3. **Cleaning & Processing**: Uses Pandas to transform parsed data into a DataFrame, handle missing values, and enforce correct data types (datetime, integers).
4. **Export**: Saves the cleaned DataFrame into a `.csv` file for further analysis.

## 🛠️ Tech Stack
- **Python 3**
- **Pandas** (Data manipulation & cleaning)
- **Regex** (Unstructured data parsing)
- **Git & GitHub** (Version control)

## 📂 Project Structure
```text
network-log-data-pipeline/
│
├── data/                  # Raw log files (not pushed to GitHub)
├── src/                   # Source code
│   ├── __init__.py
│   ├── parser.py          # Regex parsing logic
│   ├── processor.py       # Pandas cleaning & transformation
│   └── main.py            # Pipeline orchestrator

how o run
Clone the repository:
git clone https://github.com/ranimchebbi400-netzen/network-log-data-pipeline.git
Install dependencies:
pip install -r requirements.txt
Run the pipeline:
python -m src.main


│
├── .gitignore
├── requirements.txt
└── README.mdh
