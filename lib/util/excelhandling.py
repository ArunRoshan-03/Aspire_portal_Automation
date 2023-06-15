import openpyxl
from datetime import time


def create_excel_sheet(file_path):
    workbook = openpyxl.Workbook()
    workbook.save(file_path)
    print(f"Excel sheet created successfully: {file_path}")


def write_data_to_excel(file_path, data, sheet_name):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name

    for row_index, row_data in enumerate(data, start=1):
        for col_index, cell_value in enumerate(row_data, start=1):
            sheet.cell(row=row_index, column=col_index, value=cell_value)

    workbook.save(file_path)


def read_data_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))

    for row in data:
        print(row)


def get_cell_value(file_path, sheet_name, column):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    max_row = sheet.max_row

    for row in range(2, max_row + 1):
        cell_value = sheet[column + str(row)].value
        print(cell_value)

    workbook.close()


def validate_time_sheet(file_path):
    # Load the Excel file
    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook.active

    # Initialize a list to store the results
    results = []

    # Iterate through the rows starting from the second row (excluding the header)
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        emp_id = row[0]
        times = row[1:]

        continuous_times_below_7 = False
        weeks = []

        # Iterate through the time values
        for i, time_value in enumerate(times, start=1):
            if isinstance(time_value, time) and time_value.hour <= 7:
                if not continuous_times_below_7:
                    # Start of a continuous sequence of times below or equal to 7
                    week = worksheet.cell(row=1, column=i + 1).value
                    weeks.append(week)
                    # continuous_times_below_7 = True
            else:
                if continuous_times_below_7 or time_value == "-":
                    # End of a continuous sequence of times below or equal to 7
                    continuous_times_below_7 = False
                if time_value == "-":
                    # Include rows with "-" values and get the week
                    week = worksheet.cell(row=1, column=i + 1).value
                    weeks.append(week)

        if len(weeks) >= 2 or continuous_times_below_7:
            # Store the employee ID and the weeks with continuous times below or equal to 7
            results.append((emp_id, weeks))

    # Print the results
    for emp_id, weeks in results:
        print(f"Employee ID: {emp_id}")
        if weeks:
            print("Timesheet as less than 7 hours or empty data")
            for week in weeks:
                print(f"Week: {week} ")
        print()

    # Close the workbook
    workbook.close()
