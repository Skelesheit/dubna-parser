import json
from dataclasses import asdict

from dubna_old_parser.parser import ScheduleParser

parser = ScheduleParser()

path_folder = r'downloads'

schedule = parser.parse(path_folder)

print(schedule.model_dump_json(indent=2))

print(json.dumps(asdict(**schedule), ensure_ascii=False, indent=2))
