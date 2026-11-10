#!/usr/bin/env python3
"""Sinh GUI_Checklist.xlsx và GUI_Checklist.md từ danh sách ITEMS bên dưới.

Chạy:  python3 build_checklist.py
Sửa/thêm mục ở ITEMS rồi chạy lại. LƯU Ý: chạy lại sẽ ghi đè kết quả Pass/Fail
đã nhập trong Excel -> sau khi bắt đầu thực thi, hãy sửa trực tiếp trong Excel.

Origin:
  AI-draft  = bộ khởi tạo (cần bạn review, sửa, xoá mục sai)
  Student   = mục bạn tự thêm vì AI bỏ sót (BẮT BUỘC điền cột "Why AI missed")
"""
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

from order_items import ITEMS  # sửa danh sách mục trong order_items.py

HEAD = ["ID", "IA", "Screen", "Checklist item / Expected result", "Spec ref",
        "Origin", "Why AI missed (bắt buộc nếu Origin=Student)",
        "Status (Chrome)", "Notes (lý do Failed)", "Bug ID", "Screenshot",
        "Status (Firefox)", "Status (Platform 3)", "Platform 3 là gì?"]

def build_xlsx(path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Checklist"
    ws.append(HEAD)
    for i, (ia, scr, item, ref, origin) in enumerate(ITEMS, 1):
        ws.append([f"GUI-{i:03d}", ia, scr, item, ref, origin, "", "", "", "", "", "", "", ""])

    hfill = PatternFill("solid", fgColor="1F4E78")
    thin = Side(style="thin", color="BBBBBB")
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = hfill
        c.alignment = Alignment(wrap_text=True, vertical="center")
    widths = [9, 7, 18, 60, 14, 10, 34, 13, 40, 10, 18, 13, 13, 16]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
    ws.freeze_panes = "E2"
    ws.auto_filter.ref = ws.dimensions

    last = ws.max_row
    dv = DataValidation(type="list", formula1='"Passed,Failed,N/A"', allow_blank=True)
    ws.add_data_validation(dv)
    for col in ("H", "L", "M"):
        dv.add(f"{col}2:{col}{last + 60}")  # chừa chỗ cho mục thêm sau
    dv2 = DataValidation(type="list", formula1='"AI-draft,Student"', allow_blank=True)
    ws.add_data_validation(dv2)
    dv2.add(f"F2:F{last + 60}")

    # ---- Summary sheet (công thức tự đếm) ----
    s = wb.create_sheet("Summary")
    s.append(["Chỉ số", "Chrome", "Firefox", "Platform 3"])
    rng = lambda col: f"Checklist!{col}2:{col}1000"
    s.append(["Tổng số mục thiết kế", "=COUNTA(Checklist!A2:A1000)", "=B2", "=B2"])
    s.append(["Đã thực thi", f'=COUNTIF({rng("H")},"Passed")+COUNTIF({rng("H")},"Failed")',
              f'=COUNTIF({rng("L")},"Passed")+COUNTIF({rng("L")},"Failed")',
              f'=COUNTIF({rng("M")},"Passed")+COUNTIF({rng("M")},"Failed")'])
    s.append(["Passed", f'=COUNTIF({rng("H")},"Passed")', f'=COUNTIF({rng("L")},"Passed")', f'=COUNTIF({rng("M")},"Passed")'])
    s.append(["Failed", f'=COUNTIF({rng("H")},"Failed")', f'=COUNTIF({rng("L")},"Failed")', f'=COUNTIF({rng("M")},"Failed")'])
    s.append(["N/A", f'=COUNTIF({rng("H")},"N/A")', f'=COUNTIF({rng("L")},"N/A")', f'=COUNTIF({rng("M")},"N/A")'])
    s.append([])
    s.append(["Mục AI-draft", f'=COUNTIF({rng("F")},"AI-draft")'])
    s.append(["Mục Student thêm", f'=COUNTIF({rng("F")},"Student")'])
    s.append([])
    s.append(["Theo IA (tổng mục)"])
    for ia in ("IA-01", "IA-02", "IA-03", "IA-04"):
        s.append([ia, f'=COUNTIF({rng("B")},"{ia}")'])
    for c in s[1]:
        c.font = Font(bold=True, color="FFFFFF"); c.fill = hfill
    s.column_dimensions["A"].width = 28
    for col in "BCD":
        s.column_dimensions[col].width = 14
    wb.save(path)

def build_md(path):
    L = ["# GUI Checklist (bản Markdown)\n",
         "> Bản khởi tạo. Cột Status/Notes điền trong file Excel `GUI_Checklist.xlsx` rồi export lại nếu cần.\n",
         "| ID | IA | Screen | Checklist item / Expected result | Spec ref | Origin | Status | Notes |",
         "|---|---|---|---|---|---|---|---|"]
    for i, (ia, scr, item, ref, origin) in enumerate(ITEMS, 1):
        L.append(f"| GUI-{i:03d} | {ia} | {scr} | {item.replace('|', '/')} | {ref} | {origin} |  |  |")
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")

if __name__ == "__main__":
    build_xlsx("GUI_Checklist.xlsx")
    build_md("GUI_Checklist.md")
    from collections import Counter
    print("Tổng:", len(ITEMS), dict(Counter(x[0] for x in ITEMS)), dict(Counter(x[4] for x in ITEMS)))
