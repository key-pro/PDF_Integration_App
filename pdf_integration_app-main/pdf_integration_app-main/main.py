# 必要なライブラリをインポート
import os
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import messagebox
import pandas as pd
import requests
import json
from PIL import Image, ImageTk
from PyPDF2 import PdfMerger  # 追加

# # tkdndライブラリのパスを設定
os.environ['TKDND_LIBRARY'] = r'./tkdnd2.9'

class MainApp:

    def __init__(self, root):
        self.root = root
        self.root.title("PDF統合アプリ")
        
        # ドロップエリアを作成
        self.drop_area = tk.Label(self.root, text="ここにファイルをドロップ", bg="lightgray", width=40, height=10)
        self.drop_area.pack(pady=20)

        # ドロップイベントをバインド
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.on_drop)

    def on_drop(self, event):
        # ドロップされたファイルのパスを取得
        file_paths = list(self.root.tk.splitlist(event.data))  # タプルをリストに変換
        print(f"ドロップされたファイルのパス: {file_paths}")
        messagebox.showinfo("ファイルパス", f"ドロップされたファイルのパス: {file_paths}")

        # PDFを統合
        self.merge_pdfs(file_paths)

    def merge_pdfs(self, file_paths):
        try:
            merger = PdfMerger()
            # ドロップされたファイル名を数字でソート
            file_paths.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.basename(x)))) or float('inf'))

            # ソートされた順番でPDFを統合
            for pdf in file_paths:
                merger.append(pdf)
            
            # フォルダ名とファイル名を取得して結合
            path_parts = os.path.normpath(file_paths[0]).split(os.sep)
            if len(path_parts) >= 3:
                folder_name = "【" + path_parts[-3] + "】"+ "_" + path_parts[-4] + "_" + path_parts[-2]
            else:
                folder_name = "merged"

            output_dir = os.path.dirname(file_paths[0])
            output_path = os.path.join(output_dir, f"{folder_name}.pdf")
            
            # 統合したPDFを保存
            merger.write(output_path)
            merger.close()
            
            messagebox.showinfo("完了", f"PDFが統合されました: {output_path}")
        except Exception as e:
            messagebox.showerror("エラー", f"PDFの統合中にエラーが発生しました: {str(e)}")

if __name__ == "__main__":
    root = TkinterDnD.Tk()  # TkinterDnDを使用してウィンドウを作成
    app = MainApp(root)     # MainAppクラスのインスタンスを作成
    root.mainloop()         # メインループを開始
#【202401】Panorama_月次報告書