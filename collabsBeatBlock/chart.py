import pathlib
import zipfile as zp
import os
import json
import shutil


def get_name():
    with open("../parts/part_0/level.json", "r", encoding="utf-8") as f:
        d = json.load(f)
    name_ = (f"{d.get("metadata").get("artist")} - "
             f"{d.get("metadata").get("songName")} [{d.get("metadata").get("difficulty")}] "
             f"(by {d.get("metadata").get("charter")})")
    f.close()
    return name_


class Collab:
    def __init__(self, diction: list, folder_to_new_level):
        self.name = None
        self.parts = {}
        self.num_of_parts = len(diction)
        self.folder_to_new_level = folder_to_new_level
        for i in range(self.num_of_parts):
            key = f"part_{i}"
            self.parts[key] = diction[i]

    def unzip_parts(self):
        p = pathlib.Path("../parts")
        try:
            p.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            print(f"Permission denied: {p}")
            return

        for r in range(self.num_of_parts):
            pth = pathlib.Path(f"../parts/part_{r}")
            try:
                pth.mkdir(parents=True, exist_ok=True)
            except PermissionError:
                print(f"Permission denied: {pth}")
                continue

            if not zp.is_zipfile(self.parts[f"part_{r}"]):
                print(f"{self.parts[f'part_{r}']} is not a zip file")
                continue

            try:
                with zp.ZipFile(self.parts[f"part_{r}"], 'r') as zip_ref:
                    zip_ref.extractall(pth)
            except zp.BadZipFile:
                print(f"Bad zip file: {self.parts[f'part_{r}']}")

    def zipping(self):
        new_path = pathlib.Path(f"../parts/Full_level/{get_name()}")
        new_path.mkdir(parents=True, exist_ok=True)
        with zp.ZipFile(self.folder_to_new_level, 'a', zp.ZIP_DEFLATED) as zipf:
            root_dir = f"../parts/Full_level"
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, root_dir)
                    zipf.write(file_path, arcname)

    def merge_levels(self):
        levels_pths = {}
        for r in range(self.num_of_parts):
            levels_pths[f"part_{r}"] = f"../parts/part_{r}/level.json"
        combined_events = []
        data_from_first_part = None
        merged_data = None

        for part, data in levels_pths.items():
            with open(data, "r", encoding="utf-8") as f:
                d = json.load(f)
            events = d.get("events", [])
            if not isinstance(events, list):
                raise ValueError(f"Expected a list for 'events' in {part}, got {type(events).__name__}")
            combined_events.extend(events)

            if part == "part_0":
                data_from_first_part = d

        if data_from_first_part:
            merged_data = data_from_first_part.copy()
            merged_data["events"] = combined_events
        return merged_data

    def merge_charts(self):
        charts_pths = {}
        for r in range(self.num_of_parts):
            charts_pths[f"part_{r}"] = f"../parts/part_{r}/chart.json"
        combined_charts = []
        for part, path in charts_pths.items():
            try:
                with open(path, 'r') as file_l:
                    file = json.load(file_l)
                    combined_charts.extend(file)
                    file_l.close()
            except FileNotFoundError:
                print(f"File not found: {path}")
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {path}")
        return combined_charts

    def create_level(self):
        new_path = pathlib.Path(f"../parts/Full_level/{get_name()}")
        new_path.mkdir(parents=True, exist_ok=True)
        lvl_path = pathlib.Path(new_path, "level.json")
        crt_path = pathlib.Path(new_path, "chart.json")

        with open(lvl_path, "w+", encoding="utf-8") as file_lvl:
            merged_lvl = self.merge_levels()
            file_lvl.truncate()
            file_lvl.seek(0)
            json.dump(merged_lvl, file_lvl)
            file_lvl.close()

        with open(crt_path, "w+", encoding="utf-8") as file_crt:
            file_crt.seek(0)
            file_crt.write(str(self.merge_charts()).replace("'", "\""))
            file_crt.close()
        self.zipping()
        # shutil.rmtree("../parts")
