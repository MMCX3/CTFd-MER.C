# TODO: Read the file
import re
import base64
import json

with open("CTF-W2_expanded_security_logs.json", "r") as f:
    logs = json.load(f)

log_data = json.dumps(logs)   

# Approach: Get and Decode the base64 string.
potential_flags_base64 = re.findall(r'[A-Za-z0-9+/]{20,}[=]{0,2}', log_data)
for string in potential_flags_base64:
    try:
        decoded_string = base64.b64decode(string).decode('utf-8')
        print(f"Decoded string: {decoded_string}")
    except:
        continue

# Find the unique flag
for decoded_string in potential_flags_base64:
    try:
        result = base64.b64decode(decoded_string).decode('utf-8')
        if "FLAG{" in result:
            print(f"Flag found: {result}")
    except:
        continue