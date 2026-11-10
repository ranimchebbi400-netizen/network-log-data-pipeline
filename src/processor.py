import pandas as pd
from src.parser import parse_log_line

def process_logs(file_path: str) -> pd.DataFrame:
    parsed_data = []
    failed_lines = 0
    with open(file_path, 'r') as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed:
                parsed_data.append(parsed)
            else:
                failed_lines += 1
                
    print(f"[!] Data Quality: {failed_lines} lines failed to parse.")
    
    df = pd.DataFrame(parsed_data)
    df['size'] = df['size'].replace('-', '0')
    df['status'] = pd.to_numeric(df['status'], errors='coerce')
    df['size'] = pd.to_numeric(df['size'], errors='coerce').fillna(0)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%b/%Y:%H:%M:%S %z', errors='coerce')
    return df