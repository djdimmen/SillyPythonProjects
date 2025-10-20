import sys, os, subprocess

txt_files = [f for f in os.listdir() if f.endswith('.txt') and os.path.isfile(f)]

if not txt_files:
    print("No .txt files found.")
    sys.exit(0)

for idx, file in enumerate(txt_files, 1):
    print(f"{idx}. {file}")

try:
    choice = int(input("Enter the number of the file you want to choose: "))
    if 1 <= choice <= len(txt_files):
        selected_file = txt_files[choice - 1]
        print(f"You selected: {selected_file}")
    else:
        print("Invalid selection.")
except ValueError:
    print("Please enter a valid number.")
