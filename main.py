import argparse
import cmd
import shlex
import collabsBeatBlock.chart as c
import pathlib


class Main(cmd.Cmd):
    prompt = ">>> "
    intro = """
    Program for merge levels in Beat Block.
    Github of program: https://github.com/Alt-Gerutro/collabsBeatBlock
    Steam of the game: https://store.steampowered.com/app/3045200/Beatblock/
    
    Program was NOT made by the game developers*
    
    Type help to get help.
    """

    def emptyline(self):
        print("Please enter a command. Type help to get help")

    def do_merge(self, arg):
        """Merge your .zip files.
        Usage: merge (-p | --paths) path/1.zip path/2.zip ... path/n.zip (-o | -output-path) path/n+1.zip (-i | --independent-mode) (-d | --delete-needles-events)
        """
        parser = argparse.ArgumentParser(prog="merge_charts")

        parser.add_argument("-p", "--paths",
                            nargs="+",
                            type=pathlib.Path,
                            help="Paths to .zip files.",
                            required=True)
        parser.add_argument("-o", "--output-path",
                            type=pathlib.Path,
                            help="Path to .zip file where the merged level will be written.",
                            required=True)

        parser.add_argument("-i", "--independent-mode",
                            help="Enable independent mode. More in README file on github repo.",
                            required=False)

        try:
            args = parser.parse_args(shlex.split(arg))
            cl = c.Collab(args.paths, args.output_path)
            cl.unzip_parts()
            cl.create_level()
        except SystemExit:
            print()
        except Exception as e:
            print("An error occupied:", e)

    # def do_merge_charts(self, arg):
    #     """Merge your files chart.json.
    #     Usage: merge_charts (-p | --paths) path/1/chart.json path/2/chart.json ... path/n/chart.json ((-d | --default-mode) | (-n | --non-default-mode))
    #     """
    #     parser = argparse.ArgumentParser(prog="merge_charts")
    #
    #     parser.add_argument("-p", "--paths",
    #                         nargs="+",
    #                         type=pathlib.Path,
    #                         help="Paths to .zip files.",
    #                         required=True)
    #     parser.add_argument("-o", "--output-path",
    #                         type=pathlib.Path,
    #                         help="Path to .zip file where the merged level will be written.",
    #                         required=True)
    #
    #     parser.add_argument("-i", "--independent-mode",
    #                         help="Enable independent mode. More in README file on github.",
    #                         required=False)
    #
    #     try:
    #         args = parser.parse_args(shlex.split(arg))
    #         cl = c.Collab(args.paths, args.End_path)
    #         cl.unzip_parts()
    #         cl.create_level()
    #     except SystemExit:
    #         print()
    #     except Exception as e:
    #         print("An error occupied:", e)

    def do_exit(self, arg):
        """Stop the program"""
        return True

    def do_EOF(self, line):
        """Handle EOF (Ctrl-D) to exit."""
        return self.do_exit(line)


if __name__ == "__main__":
    Main().cmdloop()

# merge -p "C:\Users\gerut\PycharmProjects\collabsBeatBlock\Charts\p1.zip" "C:\Users\gerut\PycharmProjects\collabsBeatBlock\Charts\p2.zip" -o "C:\Users\gerut\PycharmProjects\collabsBeatBlock\Final.zip"