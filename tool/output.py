import pandas as pd

# 指定文件路径
file_path = ""

# 读取 Excel 文件
try:
    excel_data = pd.ExcelFile(file_path)
    
    # 输出文件中的所有 sheet 名称
    print("Excel 文件中的 Sheet 名称:")
    print(excel_data.sheet_names)
    
    # 遍历每个 Sheet 并输出数据
    for sheet_name in excel_data.sheet_names:
        print(f"\nSheet: {sheet_name}")
        
        # 读取每个 Sheet 的数据
        sheet_data = excel_data.parse(sheet_name)
        
        # 输出前 5 行数据
        print(sheet_data.head())  # 仅显示前 5 行以避免数据过多
except Exception as e:
    print(f"读取文件时出错: {e}")

