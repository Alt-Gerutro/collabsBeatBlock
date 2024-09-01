# collabsBeatBlock
Console program to merge parts of levels in game "[Beat Block](https://store.steampowered.com/app/3045200/Beatblock/)"  

[Usage](#Usage)  
[Flags](#Flags)  
[Merge Mods](#MergeMods)  
[Thanks](#Thanks)
## Usage
To use this program start .exe file and type `help`.
Congratulations, you have seen a list of all possible commands.

|   | Command      | Description                                        |                               Flags                               |
|---|--------------|----------------------------------------------------|:-----------------------------------------------------------------:|
| 1 | help         | Get Help.                                          |                                 -                                 |
| 2 | merge        | General command. Merge your **.zip** archives.     | (-p \| -paths), (-o \| --output-path), (-i \| --independent-mode) |
| 5 | exit         | Stop the program. (Ctrl + D) also work.            |                                 -                                 |

[//]: # (| 3 | merge_levels | Merge **level.json** files from **.zip** archives. | &#40;-p \| -paths&#41;, &#40;-o \| --output-path&#41;, &#40;-i \| --independent-mode&#41; |)

[//]: # (| 4 | merge_charts | Merge **chart.json** files from **.zip** archives. | &#40;-p \| -paths&#41;, &#40;-o \| --output-path&#41;, &#40;-i \| --independent-mode&#41; |)
## Flags

|   | Flag | Full flag                | Description                                                 | Example                                                                                           |
|---|------|--------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 1 | -p   | --paths                  | Paths to your **.zip** files.                               | -p "path/p1.zip" "path/p2.zip" "path/pn.zip" \| --paths "path/p1.zip" "path/p2.zip" "path/pn.zip" |
| 2 | -o   | --output-path            | Path to the archive where the merged level will be written. | -o "path/Final.zip" \| --output-path "path/Final.zip"                                             |
| 3 | -i   | --independent-mode       | Enable independent mode.                                    | -i \| --independent-mode                                                                          |
> Warning: Do not use an existing archive to write chart files twice. **Chart.json** and **level.json** will be in two, possibly different copies in the same archive.

## MergeMods
Mods to merge means how program will merge parts.

1. Independent mode - Offset part **independent** on the offset of the previous ones.
2. Sequential mode - Offset part **depends** on the offset of the previous ones.
3. Delete needless events mode - Delete events `play` incompletely and `showResuts` completely. 

## Thanks
Ratori(ratori6),  
Diwss(diwss),  
himych(himych_hehe),  
And me(gerutro).