import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class CreepyPalWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("CreepyPal - MC Assistant")
        self.root.geometry("1405x800")

        # 加载背景图片列表
        self.background_images = [
            ImageTk.PhotoImage(Image.open("background1.jpg")),
            ImageTk.PhotoImage(Image.open("background2.jpg")),
            ImageTk.PhotoImage(Image.open("background3.jpg"))
        ]
        self.current_background_index = 0

        # 创建Canvas显示背景图片
        self.canvas = tk.Canvas(self.root, width=1405, height=800)
        self.canvas.pack(fill="both", expand=True)
        self.update_background()

        # 翻页按钮
        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_page)
        self.prev_button.place(x=50, y=550)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_page)
        self.next_button.place(x=700, y=550)

        # 文本输入框
        self.input_label = tk.Label(self.root, text="Send your Question&Goal:")
        self.input_label.place(x=10, y=50)

        self.input_box = tk.Entry(self.root, width=80)
        self.input_box.place(x=200, y=50)

        # 文本输出框
        self.output_label = tk.Label(self.root, text="CreepyPal:")
        self.output_label.place(x=105, y=150)

        self.output_box = tk.Text(self.root, height=15, width=70)
        self.output_box.place(x=200, y=150)

        # 发送按钮
        self.send_button = tk.Button(self.root, text="send", command=self.get_answer)
        self.send_button.place(x=770, y=45)

    def update_background(self):
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_images[self.current_background_index])

    def prev_page(self):
        self.current_background_index = (self.current_background_index - 1) % len(self.background_images)
        self.update_background()

    def next_page(self):
        self.current_background_index = (self.current_background_index + 1) % len(self.background_images)
        self.update_background()

    def get_answer(self):
        question = self.input_box.get()
        if not question:
            messagebox.showwarning("Type error", "Please enter a question or keyword！")
            return

        # 模拟生成回答的部分
        response = f"Based on your question '{question}', we recommend that you collect the following resources and perform these synthetic routes..."

        # 显示在输出框中
        self.output_box.delete(1.0, tk.END)  # 清空之前的内容
        self.output_box.insert(tk.END, response)


if __name__ == "__main__":
    root = tk.Tk()
    app = CreepyPalWindow(root)
    root.mainloop()
