import tkinter as tk
from tkinter import ttk
import requests

# 定义 API URL
API_URL = "https://apiserver.alcex.cn/google/translate/"

def translate():
    input_text = input_box.get("1.0", tk.END).strip()
    source_lang = source_var.get()
    target_lang = target_var.get()

    if not input_text:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "请输入要翻译的文本。")
        return

    params = {
        "text": input_text,
        "source_lang": source_lang,
        "target_lang": target_lang
    }
    headers = {
        "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
        "Content-Type": "application/json"
    }

    try:
        # 使用 POST 请求
        response = requests.post(API_URL, params=params, headers=headers)
        response.raise_for_status()
        result = response.json()
        # 根据返回参数说明提取翻译结果
        if result.get("code") == 200:
            translated_text = result.get("data")
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, translated_text)
        else:
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, f"翻译失败，状态码: {result.get('code')}")
    except requests.RequestException as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"请求出错: {str(e)}")
    except ValueError:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"无法解析服务器响应，请稍后重试。响应内容: {response.text}")

# 创建主窗口
root = tk.Tk()
root.title("海绵单词翻译工具")
root.geometry("600x600")  # 设置窗口大小
root.configure(bg="#f0f0f0")  # 设置窗口背景颜色

# 创建标题标签
title_label = tk.Label(root, text="海绵单词翻译工具", font=("Arial", 24, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# 创建输入框部分
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="输入要翻译的文本:", font=("Arial", 14), bg="#f0f0f0")
input_label.pack()
input_box = tk.Text(input_frame, height=10, width=50, font=("Arial", 12))
input_box.pack(pady=5)

# 创建源语言和目标语言选择框部分
lang_frame = tk.Frame(root, bg="#f0f0f0")
lang_frame.pack(pady=10)

source_var = tk.StringVar(root)
source_var.set("auto")  # 默认源语言为自动检测
target_var = tk.StringVar(root)
target_var.set("en")  # 默认目标语言为英文

source_menu_label = tk.Label(lang_frame, text="源语言:", font=("Arial", 14), bg="#f0f0f0")
source_menu_label.pack(side=tk.LEFT, padx=10)
source_menu = ttk.Combobox(lang_frame, textvariable=source_var, values=["auto", "zh", "en"], font=("Arial", 12))
source_menu.pack(side=tk.LEFT, padx=10)

target_menu_label = tk.Label(lang_frame, text="目标语言:", font=("Arial", 14), bg="#f0f0f0")
target_menu_label.pack(side=tk.LEFT, padx=10)
target_menu = ttk.Combobox(lang_frame, textvariable=target_var, values=["zh", "en"], font=("Arial", 12))
target_menu.pack(side=tk.LEFT, padx=10)

# 创建翻译按钮
translate_button = tk.Button(root, text="翻译", command=translate, font=("Arial", 16), bg="#007BFF", fg="white", bd=0, padx=20, pady=10)
translate_button.pack(pady=20)

# 创建输出框部分
output_frame = tk.Frame(root, bg="#f0f0f0")
output_frame.pack(pady=10)

output_label = tk.Label(output_frame, text="翻译结果:", font=("Arial", 14), bg="#f0f0f0")
output_label.pack()
output_box = tk.Text(output_frame, height=10, width=50, font=("Arial", 12))
output_box.pack(pady=5)

# 创建版权和 QQ 群信息标签
copyright_label = tk.Label(root, text="版权所有 © 海绵单词", font=("Arial", 12), bg="#f0f0f0")
copyright_label.pack(pady=10)

qq_group_label = tk.Label(root, text="官方 QQ 群 533683061", font=("Arial", 12), bg="#f0f0f0")
qq_group_label.pack(pady=5)

# 运行主循环
root.mainloop()