import re
from typing import Dict, Optional

# Zidna .* fel ekher bech y9bel el Referer w User-Agent
LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>.*?)\] '
    r'"(?P<method>\S+) (?P<endpoint>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\S+).*'  # <--- Houni salla7na
)

def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    match = LOG_PATTERN.match(line.strip())
    if match:
        return match.groupdict()
    return None