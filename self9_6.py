import csv

L = [["漢字", "莞爾", "幹事"], ["欣然", "近前"], ["D", "G", "H"]]

with open("self9_7.csv", "w", encoding="cp932") as f:
    w = csv.writer(f, delimiter=",")
    for i in L:
        w.writerow(i)
