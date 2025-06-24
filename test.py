import json
from dataclasses import asdict

from dubna_parser import ScheduleParser


parser = ScheduleParser()

path_folder = r'downloads'

schedule = parser.parse(path_folder)

def normalize_keys(obj):
    if isinstance(obj, dict):
        return {
            (k.coordinate if hasattr(k, "coordinate") else str(k)): normalize_keys(v)
            for k, v in obj.items()
        }
    if isinstance(obj, list):
        return [normalize_keys(i) for i in obj]
    return obj

raw = normalize_keys(asdict(schedule))
print(json.dumps(raw, ensure_ascii=False, indent=2))


# print(json.dumps(asdict(schedule), ensure_ascii=False, indent=2))