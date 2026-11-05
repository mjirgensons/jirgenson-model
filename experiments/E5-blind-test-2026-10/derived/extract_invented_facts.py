"""Extract every invented fact the judge listed in round 5 (python3 derived/extract_invented_facts.py)."""
import csv, glob, json, re
rows = []
for f in sorted(glob.glob('judgments/round5/*.md')):
    name = f.split('/')[-1][:-3]
    blocks = re.findall(r'```json\s*(\{.*?\})\s*```', open(f, encoding='utf-8').read(), re.S)
    if not blocks:
        continue
    j = json.loads(blocks[-1])
    task, x, y, order = re.match(r'(T\d+)_(.+?)_vs_(.+?)_(12|21)$', name).groups()
    label = {'1': x, '2': y} if order == '12' else {'1': y, '2': x}
    for k, v in j['responses'].items():
        for fact in v.get('invented_facts', []):
            rows.append([task, label[k], name, fact])
rows = [r for r in rows if r[1].startswith('A-')] + [r for r in rows if 'v1.5-c' in r[1]]
with open('derived/invented_facts_round5.csv', 'w', newline='', encoding='utf-8') as out:
    w = csv.writer(out)
    w.writerow(['scenario', 'answer', 'judge_record', 'invented_fact_as_listed_by_judge'])
    w.writerows(rows)
print(len(rows), 'rows')
