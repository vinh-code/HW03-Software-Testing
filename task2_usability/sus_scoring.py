#!/usr/bin/env python3
"""Score SUS 1–5 responses; preserve the declared provenance of each row."""
import csv
import statistics as st
import sys


def sus(answers):
    if len(answers) != 10 or any(type(a) is not int or not 1 <= a <= 5 for a in answers):
        raise ValueError('Cần đúng 10 số nguyên trong 1..5.')
    return sum(a - 1 if i % 2 == 0 else 5 - a for i, a in enumerate(answers)) * 2.5


def main(path):
    scores = []
    ids = set()
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            pid = row['participant']
            if pid in ids:
                raise ValueError('Trùng participant: ' + pid)
            ids.add(pid)
            value = sus([int(row[f'q{i}']) for i in range(1, 11)])
            scores.append(value)
            print(f'{pid}: {value:.1f}/100')
    if not scores:
        print('Không có câu trả lời; không tính điểm.'); return
    print(f'n={len(scores)}; mean={st.mean(scores):.2f}; median={st.median(scores):.2f}; '
          f'sample_SD={st.stdev(scores) if len(scores)>1 else 0:.2f}; min={min(scores):.1f}; max={max(scores):.1f}')
    print('SUS là điểm thang 0–100, đo lường mức độ dễ sử dụng của hệ thống theo chuẩn quốc tế.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Dùng: python3 sus_scoring.py sus_responses.csv')
    main(sys.argv[1])
