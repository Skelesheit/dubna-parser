import json
from dataclasses import asdict

from dubna_parser import ScheduleParser


parser = ScheduleParser()

path_folder = r'downloads'

schedule = parser.parse(path_folder)

print(json.dumps(asdict(schedule), ensure_ascii=False, indent=2))