from rich.console import Console
from rich.prompt import Prompt
import argparse
import sys, traceback
import pathlib
from collabsBeatBlock.chart import Collab

console = Console()


def merge(paths, output, filtered):
    col = Collab(paths, output)
    col.unzip_parts()
    col.create_level(filtered=filtered)


def main():
    console.print("""
    Program for merge levels in Beat Block.
    Github of program: https://github.com/Alt-Gerutro/collabsBeatBlock
    Steam of the game: https://store.steampowered.com/app/3045200/Beatblock/

    Program was NOT made by the game developers*

    See github for get help.
    """)
    while True:
        args = None
        Prompt.prompt_suffix = ""
        command = Prompt.ask(">>> ")

        if command == "exit" or command == "quit":
            console.print("Exiting...", style="bold red")
            break

        if command is None or command == "":
            console.print("Enter a command")
            continue
        parser = argparse.ArgumentParser()
        parser.add_argument("command", choices=["merge"], help="Command")
        parser.add_argument("-p", "--paths", nargs="+", type=str, help="Пути к файлам", required=True)
        parser.add_argument("-o", "--output-path", type=str, help="Path to output .zip file")
        parser.add_argument("-f", "--filter", nargs="+", type=str, help="Filter to output level")

        try:
            args = parser.parse_args(command.split())
        except SystemExit:
            console.print("Error: invalid command or arguments", style="bold red")
        except KeyboardInterrupt:
            console.print("Exit", style="bold red")
        except Exception:
            traceback.print_exc(file=sys.stdout)

        if args.command == "merge":
            merge(args.paths, args.output_path, args.filter)


if __name__ == "__main__":
    main()

# merge -p C:\Users\gerut\PycharmProjects\collabsBeatBlock\Charts\p1.zip C:\Users\gerut\PycharmProjects\collabsBeatBlock\Charts\p2.zip C:\Users\gerut\PycharmProjects\collabsBeatBlock\Charts\p3.zip -o C:\Users\gerut\PycharmProjects\collabsBeatBlock\Final.zip -f play showResults