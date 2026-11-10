from src.processor import process_logs

def main():
    input_file = "data/access.log"
    output_file = "data/cleaned_logs.csv"
    
    print(f"[-] Starting Pipeline: Reading {input_file}...")
    try:
        df = process_logs(input_file)
        print(f"[-] Successfully parsed {len(df)} log lines.")
        df.to_csv(output_file, index=False)
        print(f"[-] Cleaned data saved to {output_file} 🚀")
        print("\n--- Quick Summary (Top 3 Status Codes) ---")
        print(df['status'].value_counts().head(3))
    except FileNotFoundError:
        print(f"[X] ERROR: Could not find {input_file}. Make sure the file is inside the data folder.")

if __name__ == "__main__":
    main()