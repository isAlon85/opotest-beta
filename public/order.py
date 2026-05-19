import json

with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for i, item in enumerate(data, start=1):
    item["id"] = i

with open("questions_id.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)