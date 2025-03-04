import sys

# Define the required custom properties
REQUIRED_PROPERTIES = [
    '--primary-color',
    '--color-black',
    '--color-white',
    '--color-light-grey',
    '--color-dark-grey',
    '--text-color'
]

def check_custom_properties(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        for prop in REQUIRED_PROPERTIES:
            if prop not in content:
                print(f"Missing custom property: {prop}")
                return
    print("OK")

def main():
    if len(sys.argv) != 2:
        print("Usage: python custom_property_checker.py <path_to_css_file>")
        return
    css_file = sys.argv[1]
    check_custom_properties(css_file)

if __name__ == "__main__":
    main()
