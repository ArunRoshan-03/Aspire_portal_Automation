import openpyxl


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
