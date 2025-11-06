import pandas as pd
import random
import os

def random_sample_csv_to_excel():
    # 输入和输出文件路径
    input_file = "/Users/luzhu/Documents/PC query历史记录/dd_1104.csv"
    output_file = "/Users/luzhu/Documents/PC query历史记录/dd_1104_sample_300.xlsx"
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：找不到输入文件 {input_file}")
        return
    
    try:
        # 读取CSV文件
        print(f"正在读取文件: {input_file}")
        df = pd.read_csv(input_file)
        total_rows = len(df)
        print(f"文件总行数: {total_rows}")
        
        # 确保总行数大于等于300
        sample_size = min(300, total_rows)
        
        # 随机抽样
        print(f"正在随机抽取 {sample_size} 行数据...")
        sampled_df = df.sample(n=sample_size, random_state=42)  # 使用固定随机种子确保可重复性
        
        # 保存为Excel文件
        print(f"正在保存到: {output_file}")
        sampled_df.to_excel(output_file, index=False)
        
        print(f"成功！已从 {total_rows} 行中随机抽取 {sample_size} 行并保存到 {output_file}")
        
    except Exception as e:
        print(f"处理过程中发生错误: {str(e)}")

if __name__ == "__main__":
    random_sample_csv_to_excel()
