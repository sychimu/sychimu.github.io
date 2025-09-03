import pandas as pd

def excel_to_js_array(excel_path, sheet_name, output_js_path):
    # 读取Excel数据
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    
    # 处理空值（替换为空字符串）
    df = df.fillna('')
    
    # 转换为JavaScript二维数组格式
    # 格式示例：[["主板型号1", "板型1", ...], ["主板型号2", "板型2", ...]]
    js_array = []
    # 添加表头（可选，如果需要的话）
    # js_array.append(df.columns.tolist())
    # 添加数据行
    for _, row in df.iterrows():
        js_array.append(row.tolist())
    
    # 转换为JavaScript字符串
    js_code = f"const motherboardData = {js_array};"
    
    # 保存到JS文件
    with open(output_js_path, 'w', encoding='utf-8') as f:
        f.write(js_code)
    
    print(f"转换完成！数据已保存到 {output_js_path}")

# 使用示例
if __name__ == "__main__":
    # 替换为你的Excel文件路径
    excel_path = "motherboard.xlsx"
    # 替换为工作表名称（如之前的"list"）
    sheet_name = "list"
    # 输出的JS文件路径
    output_js_path = "motherboard_data.js"
    
    excel_to_js_array(excel_path, sheet_name, output_js_path)
