import os

def check_html_structure(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        if '<html' in content:
            print("OK")
        else:
            print("Missing 'html'")

def main():
    html_file = 'index.html'
    if os.path.exists(html_file):
        check_html_structure(html_file)
    else:
        print(f"{html_file} not found.")

if __name__ == "__main__":
    main()
