# Tworzenie plików z danymi testowymi

# Dane do pierwszego pliku
data1 = """10
3
15 4
20 5
10 3
"""
with open('test_data1.txt', 'w') as file:
    file.write(data1)

# Dane do drugiego pliku
data2 = """25
4
10 5
40 10
30 8
50 12
"""
with open('test_data2.txt', 'w') as file:
    file.write(data2)

# Dane do trzeciego pliku
data3 = """50
5
60 10
100 20
120 30
200 25
50 5
"""
with open('test_data3.txt', 'w') as file:
    file.write(data3)
