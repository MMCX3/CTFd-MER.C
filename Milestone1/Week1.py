# MO-IT143 - Ethical Hacking S3101 | A.Y. 2025 - 2026
# Team C / MER/C : Dela Cruz, L.M., Tubera, K.G., & Samaniego, M.Y.

#Week 1 - Flagged for Extraction
import re

#Read the file , line by line
with open('CTF-W1_mystery_text_file.txt', 'r') as f:
    content = f.read()
    flags = re.findall(r'FLAG\{.*?\}',content)

#Find the unique message
flag_counts = {}
for f in flags:
    flag_counts[f] = flag_counts.get(f,0) + 1

for f, count in flag_counts.items():
    print(f"{f} = {count}")


