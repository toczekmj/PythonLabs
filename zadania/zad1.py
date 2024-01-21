import json

with open('tramwaje.json', 'r', encoding="utf-8") as read_file:
    data = json.load(read_file)

lines = {}
stops = {}

for line in data['tramwaje']:
    lines[line['linia']] = []
    if 'przystanek' in line:
        for stop in line['przystanek']:
            lines[line['linia']].append(stop['nazwa'][:-3])
            stops[stop['nazwa'][:-3]] = True

with open('tramwaje_out.json', 'w', encoding="utf-8") as write_file:
    json.dump(lines, write_file, ensure_ascii=False, indent=4)

for line in sorted(lines, key=lambda l: len(lines[l]), reverse=True):
    print(f"Linia {line} – liczba przystanków: {len(lines[line])}")

for stop in stops:
    print(stop)

print(f"Liczba przystanków: {len(stops)}")
