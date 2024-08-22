import argparse
import cmd
import shlex
import collabsBeatBlock.chart as c
import pathlib


class Main(cmd.Cmd):
    prompt = "> "
    intro = """
    Program for merge levels in Beat Block.
    Github of program: https://github.com/Alt-Gerutro/collabsBeatBlock
    Steam of the game: https://store.steampowered.com/app/3045200/Beatblock/
    
    Program was NOT made by the game developers*
    
    Type help to get help
    """

    def emptyline(self):
        print("Please enter a command. Type help to get help")

    def do_merge(self, arg):
        """Merge your .zip files.
        Usage: merge (-p | --paths) path/1.zip path/2.zip ... path/n.zip ((-d | --default-mode) | (-n | --non-default-mode))"""
        parser = argparse.ArgumentParser(prog="merge")

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("-d", "--default-mode", action="store_true", help="Turn on default merge. The merge does not depend on the last block, but on the 0 line")
        group.add_argument("-n", "--non-default-mode", action="store_true", help="Turn on non-default merge. The merge does depend on the last block, but on the 0 line")

        parser.add_argument("-p", "--paths", nargs="+", type=pathlib.Path, help="Paths to .zip files", required=True)
        parser.add_argument("-E", "--End-path", type=pathlib.Path, help="Path to .zip file where the merged level will be recorded")

        try:
            args = parser.parse_args(shlex.split(arg))
            cl = c.Collab(args.paths, args.End_path)
            cl.unzip_parts()
            cl.create_level()
        except SystemExit:
            print()
        except Exception as e:
            print("An error occupied:", e)

    def do_merge_charts(self, arg):
        """Merge your files chart.json.
        Usage: merge_charts (-p | --paths) path/1/chart.json path/2/chart.json ... path/n/chart.json ((-d | --default-mode) | (-n | --non-default-mode))
        """
        parser = argparse.ArgumentParser(prog="merge_charts")

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("-d", "--default-mode", action="store_true", help="Turn on default merge. The merge does not depend on the last block, but on the 0 line")
        group.add_argument("-n", "--non-default-mode", action="store_true", help="Turn on non-default merge. The merge does depend on the last block, but on the 0 line")

        parser.add_argument("-p", "--paths", nargs="+", type=pathlib.Path, help="Paths to .zip files", required=True)
        parser.add_argument("-E", "--End-path", type=pathlib.Path, help="Path to .zip file where the merged level will be recorded")

        try:
            args = parser.parse_args(shlex.split(arg))
            cl = c.Collab(args.paths, args.End_path)
            cl.unzip_parts()
            cl.create_level()
        except SystemExit:
            print()
        except Exception as e:
            print("An error occupied:", e)

    def do_exit(self, arg):
        """Stop the program"""
        return True

    def do_EOF(self, line):
        """Handle EOF (Ctrl-D) to exit."""
        return self.do_exit(line)


if __name__ == "__main__":
    Main().cmdloop()

# merge -p "C:\Users\gerut\PycharmProjects\collabsBeatBlock\Charts\p1.zip" "C:\Users\gerut\PycharmProjects\collabsBeatBlock\Charts\p2.zip" -d -E "C:\Users\gerut\PycharmProjects\collabsBeatBlock\Final.zip"