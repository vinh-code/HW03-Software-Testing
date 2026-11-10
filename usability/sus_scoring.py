#!/usr/bin/env python3
"""Chấm điểm SUS từ CSV.  Dùng:  python3 sus_scoring.py sus_responses.csv

CSV: participant,q1,...,q10  (mỗi câu là số nguyên 1-5)
"""
import csv
import statistics as st
import sys


def sus(answers):
    if len(answers) != 10 or any(not 1 <= a <= 5 for a in answers):
        raise ValueError(f"Cần 10 câu trả lời trong 1..5, nhận được: {answers}")
    total = sum((a - 1) if i % 2 == 0 else (5 - a) for i, a in enumerate(answers))
    return total * 2.5


def grade(score):
    if score >= 80.3:
        return "A (Xuất sắc)"
    if score >= 68:
        return "B/C (Tốt/Trung bình)"
    if score >= 51:
        return "D (Dưới trung bình)"
    return "F (Kém)"


def main(path):
    scores = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ans = [int(row[f"q{i}"]) for i in range(1, 11)]
            s = sus(ans)
            scores.append(s)
            print(f"{row['participant']:<14} SUS = {s:5.1f}   {grade(s)}")
    if not scores:
        print("CSV không có dòng dữ liệu.")
        return
    print("-" * 44)
    print(f"n = {len(scores)}   mean = {st.mean(scores):.1f}   "
          f"median = {st.median(scores):.1f}   "
          f"SD = {st.stdev(scores) if len(scores) > 1 else 0:.1f}   "
          f"min = {min(scores):.1f}   max = {max(scores):.1f}")
    print(f"Mức trung bình: {grade(st.mean(scores))}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Dùng: python3 sus_scoring.py sus_responses.csv")
    main(sys.argv[1])
