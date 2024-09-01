import pathlib
import zipfile as zp
import os
import json
import shutil
import glob


def get_name():
    with open("../parts/part_0/level.json", "r", encoding="utf-8") as f:
        d = json.load(f)
    metadata = d.get("metadata")
    name = f'{metadata.get("artist")} - {metadata.get("songName")} [{metadata.get("difficulty")}] ({metadata.get("charter")})'
    return name


def find_root_dir(path):
    return glob.glob("**/chart.json").parent


def copy_deco(part_pth, end_pth):
    shutil.copytree(part_pth, end_pth, ignore=shutil.ignore_patterns("level.json", "chart.json", "backup"),
                    dirs_exist_ok=True)


def dump_file(pth, merged_items):
    with open(pth, "w+", encoding="utf-8") as file:
        file.write(json.dumps(merged_items))


class Collab:
    def __init__(self, parts_list: list, output_folder: str):
        self.name = None
        self.output_folder = output_folder
        self.num_of_parts = len(parts_list)
        self.parts = {f"part_{i}": parts_list[i] for i in range(self.num_of_parts)}

    def unzip_parts(self):
        parts_dir = pathlib.Path("../parts")
        try:
            parts_dir.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            print(f"Permission denied: {parts_dir}")
            return

        for part, part_zip in self.parts.items():
            part_path = pathlib.Path(f"../parts/{part}")
            part_path.mkdir(parents=True, exist_ok=True)

            if not zp.is_zipfile(part_zip):
                print(f"{part_zip} is not a zip file")
                continue
            try:
                with zp.ZipFile(part_zip, 'r') as zip_ref:
                    zip_ref.extractall(part_path)
            except zp.BadZipFile:
                print(f"Bad zip file: {part_zip}")

    def zip_full_level(self):
        full_level_path = pathlib.Path(f"../parts/Full_level/{get_name()}")
        full_level_path.mkdir(parents=True, exist_ok=True)
        for i in range(self.num_of_parts):
            copy_deco(f"../parts/part_{i}", full_level_path)
        with zp.ZipFile(self.output_folder, 'a', zp.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(full_level_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, full_level_path.parent)
                    zipf.write(file_path, arcname)

    def merge_levels_ind(self):
        levels_pths = {f"part_{i}": f"../parts/part_{i}/level.json" for i in range(self.num_of_parts)}
        combined_events = []
        prev_parts_offset = 0
        data_from_first_part = None
        merged_data = None

        for part, path in levels_pths.items():
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                events = data.get("events", [])
                if not isinstance(events, list):
                    raise ValueError(f"Expected a list for 'events' in {part}, got {type(events).__name__}")

                if len(events) > 0:
                    if part != "part_0":
                        for event in events:
                            print(prev_parts_offset)
                            print(event["time"])
                            event["time"] += prev_parts_offset
                            print(event["time"], "\n")
                    combined_events.extend(events)
                    for i in range(len(events)):
                        if events[-i]["type"] != "deco":
                            prev_parts_offset = events[-i]["time"]
                    print(events)

                if part == "part_0":
                    data_from_first_part = data

        if data_from_first_part:
            merged_data = data_from_first_part.copy()
            merged_data["events"] = combined_events

        return merged_data

    def merge_levels(self):
        levels_pths = {f"part_{i}": f"../parts/part_{i}/level.json" for i in range(self.num_of_parts)}
        combined_events = []
        data_from_first_part = None
        merged_data = None

        for part, path in levels_pths.items():
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            events = data.get("events", [])
            if not isinstance(events, list):
                raise ValueError(f"Expected a list for 'events' in {part}, got {type(events).__name__}")
            combined_events.extend(events)

            if part == "part_0":
                data_from_first_part = data

        if data_from_first_part:
            merged_data = data_from_first_part.copy()
            merged_data["events"] = combined_events
        return merged_data

    def merge_charts_ind(self):
        charts_pths = {f"part_{i}": f"../parts/part_{i}/chart.json" for i in range(self.num_of_parts)}
        combined_charts = []
        prev_parts_offset = 0
        for part, path in charts_pths.items():
            try:
                with open(path, 'r') as file_l:
                    file = json.load(file_l)
                    for lvl_items in file:
                        if part != "part_0":
                            lvl_items["time"] += prev_parts_offset
                    combined_charts.extend(file)
                    prev_parts_offset += file[-1][0]["time"]
            except FileNotFoundError:
                print(f"File not found: {path}")
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {path}")
        return combined_charts

    def merge_charts(self):
        charts_pths = {f"part_{i}": f"../parts/part_{i}/chart.json" for i in range(self.num_of_parts)}
        combined_charts = []
        for part, path in charts_pths.items():
            try:
                with open(path, 'r') as file_l:
                    file = json.load(file_l)
                    combined_charts.extend(file)
            except FileNotFoundError:
                print(f"File not found: {path}")
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {path}")
        return combined_charts

    def create_level(self, independent_mode: bool = False):
        new_path = pathlib.Path(f"../parts/Full_level/{get_name()}")
        new_path.mkdir(parents=True, exist_ok=True)
        lvl_path = pathlib.Path(new_path, "level.json")
        crt_path = pathlib.Path(new_path, "chart.json")

        if independent_mode:
            merged_crt = self.merge_charts()
            merged_lvls = self.merge_levels()
        else:
            merged_crt = self.merge_charts_ind()
            merged_lvls = self.merge_levels_ind()

        dump_file(crt_path, merged_crt)
        dump_file(lvl_path, merged_lvls)
        self.zip_full_level()

        shutil.rmtree("../parts")


# if __name__ == "__main__":
    # cl = Collab(, r"../Final.zip")
    # cl.unzip_parts()
    # print(cl.merge_levels_ind())
    # cl.create_level()
