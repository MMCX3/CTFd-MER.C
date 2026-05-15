import re

def find_hidden_flags(log_file="CTF-W3_expanded_access_logs.txt"):
   
    print(" EXTRACTING HIDDEN FLAGS ")
    
    try:
        with open('Milestone1/Milestone1-Files/CTF-W3_expanded_access_logs.txt', 'r') as f:
            log_data = f.read()

        hidden_flags = re.findall(r"FLAG\{.*?\}", log_data)
        alt_flags = re.findall(r"MMDC_CTF\{.*?\}", log_data)

        all_found = hidden_flags + alt_flags

        if all_found:
            for flag in all_found:
                print(f"-> {flag}")
        else:
            print("-> No hidden flags found.")
            
    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")

if __name__ == "__main__":
    find_hidden_flags()