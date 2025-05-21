import sys
import re
from collections import Counter, defaultdict

# Patterns (these are sample regex patterns, adjust them based on log contents)
FAILED_LOGIN_PATTERN = r"login attempt \[FAILED\] for user \w+ from (\d+\.\d+\.\d+\.\d+)"
SUCCESS_LOGIN_PATTERN = r"login attempt \[SUCCESS\] for user (\w+) with password (\w+) from (\d+\.\d+\.\d+\.\d+)"

def _print_counter(counter_dict):
    for key, count in sorted(counter_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}: {count}")

def analyze_failed_logins(lines, min_count=1):
    ip_counter = Counter()
    for line in lines:
        match = re.search(FAILED_LOGIN_PATTERN, line)
        if match:
            ip = match.group(1)
            ip_counter[ip] += 1

    filtered = {ip: count for ip, count in ip_counter.items() if count >= min_count}
    _print_counter(filtered)

def analyze_successful_creds(lines):
    creds_map = defaultdict(set)
    for line in lines:
        match = re.search(SUCCESS_LOGIN_PATTERN, line)
        if match:
            user, passwd, ip = match.groups()
            creds_map[(user, passwd)].add(ip)

    sorted_creds = sorted(creds_map.items(), key=lambda item: len(item[1]), reverse=True)
    print("username | password | IP count")
    print("------------------------------")
    for (user, passwd), ip_set in sorted_creds:
        print(f"{user:<8} | {passwd:<8} | {len(ip_set)}")

def main():
    if len(sys.argv) < 4:
        print("Usage: python analyze_log.py <logfile> --task <task-name> [--min-count N]")
        return

    logfile = sys.argv[1]
    task = sys.argv[3]
    min_count = 1
    if '--min-count' in sys.argv:
        min_count = int(sys.argv[sys.argv.index('--min-count') + 1])

    with open(logfile, "r") as f:
        lines = f.readlines()

    if task == "failed-logins":
        analyze_failed_logins(lines, min_count)
    elif task == "successful-creds":
        analyze_successful_creds(lines)
    else:
        print("Unknown task.")

if __name__ == "__main__":
    main()
