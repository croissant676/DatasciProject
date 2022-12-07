with open('data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    with open('formatted.csv', 'w', encoding='utf-8') as f2:
        for i, line in enumerate(lines):
            if i % 2 == 1:
                continue
            f2.write(line)
