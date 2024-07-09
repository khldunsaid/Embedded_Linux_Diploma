import re
from openpyxl import Workbook

def parse_header_file(header_file):
    # Regular expression to match function prototypes
    prototype_pattern = re.compile(r'\b\w+\s+\w+\s*\(.*?\)\s*;')

    # Read the header file content
    with open(header_file, 'r') as file:
        content = file.read()

    # Find all prototypes using the regular expression
    prototypes = prototype_pattern.findall(content)
    return prototypes

def write_to_excel(prototypes, excel_file):
    # Create a new workbook and select the active worksheet
    workbook = Workbook()
    sheet = workbook.active

    # Write header
    sheet.append(["ID", "Function Prototype"])

    # Write prototypes to the sheet with unique IDs
    for idx, prototype in enumerate(prototypes):
        sheet.append([f"IDX{idx}", prototype])

    # Save the workbook
    workbook.save(excel_file)

def main():
    header_file = 'interrupt.h'  # Replace with your header file path
    excel_file = 'function_prototypes.xlsx'  # Output Excel file

    # Parse the header file to get function prototypes
    prototypes = parse_header_file(header_file)

    # Write the prototypes to an Excel file
    write_to_excel(prototypes, excel_file)
    print(f"Function prototypes have been written to {excel_file}")

if __name__ == "__main__":
    main()