import tkinter as tk
from tkinter import messagebox

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Máy tính đơn giản")
window.geometry("400x300")

# Hàm kiểm tra đầu vào hợp lệ
def validate_input():
    try:
        # Lấy giá trị từ ô nhập liệu
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        
        # Kiểm tra số tự nhiên
        if num1 <= 0 or num2 <= 0:
            messagebox.showerror("Lỗi", "Vui lòng nhập số tự nhiên (số nguyên dương)")
            return None
        return num1, num2
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số tự nhiên hợp lệ")
        return None

# Các hàm xử lý phép tính
def add():
    result = validate_input()
    if result:
        num1, num2 = result
        result_label.config(text=f"Kết quả: {num1 + num2}")

def subtract():
    result = validate_input()
    if result:
        num1, num2 = result
        result_label.config(text=f"Kết quả: {num1 - num2}")

def multiply():
    result = validate_input()
    if result:
        num1, num2 = result
        result_label.config(text=f"Kết quả: {num1 * num2}")

def divide():
    result = validate_input()
    if result:
        num1, num2 = result
        if num2 == 0:
            messagebox.showerror("Lỗi", "Không thể chia cho 0")
        else:
            result_label.config(text=f"Kết quả: {num1 / num2}")

# Tạo và đặt vị trí các thành phần giao diện
label1 = tk.Label(window, text="Nhập số thứ nhất:")
label1.pack(pady=5)

entry1 = tk.Entry(window)
entry1.pack(pady=5)

label2 = tk.Label(window, text="Nhập số thứ hai:")
label2.pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Khung chứa các nút tính toán
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Tạo các nút tính toán
add_button = tk.Button(button_frame, text="+", command=add, width=5)
add_button.pack(side=tk.LEFT, padx=5)

subtract_button = tk.Button(button_frame, text="-", command=subtract, width=5)
subtract_button.pack(side=tk.LEFT, padx=5)

multiply_button = tk.Button(button_frame, text="×", command=multiply, width=5)
multiply_button.pack(side=tk.LEFT, padx=5)

divide_button = tk.Button(button_frame, text="÷", command=divide, width=5)
divide_button.pack(side=tk.LEFT, padx=5)

# Nhãn hiển thị kết quả
result_label = tk.Label(window, text="Kết quả: ", font=("Arial", 12))
result_label.pack(pady=20)

# Khởi chạy ứng dụng
window.mainloop()