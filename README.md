# collabsBeatBlock
Console program to merge parts of levels in game "[Beat Block](https://store.steampowered.com/app/3045200/Beatblock/)"  

[File Tree](#file-tree)
[Usage](#Usage)  
[Flags](#Flags)  
[For Filters](#for-filters)  
[Merge Mods](#MergeMods)  
[Thanks](#Thanks)  

> If you enter unknown command - program will close.

## File Tree
For everything to work, your .zip files should look like this:
```
.
└── File.zip/
    ├── chart.json
    ├── level.json
    ├── deco1.png
    ├── deco2.png
    ├── decon.png
    └── song.ogg
```

**NOT** THIS:
```
.
└── File.zip/
    └── part_dir/
        ├── chart.json
        ├── level.json
        ├── deco1.png
        ├── deco2.png
        ├── decon.png
        └── song.ogg
```  

And you get something like this:
```
.
└── File.zip/
    └── Author - Song [LV] (by Creator)/
        ├── chart.json
        ├── level.json
        ├── deco1.png
        ├── deco2.png
        ├── decon.png
        └── song.ogg
```
> All info to directory name program gets from first part.

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

|   | Flag | Full flag          | Description                                                 | Example                                                                                           |
|---|------|--------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| 1 | -p   | --paths            | Paths to your **.zip** files.                               | -p "path/p1.zip" "path/p2.zip" "path/pn.zip" \| --paths "path/p1.zip" "path/p2.zip" "path/pn.zip" |
| 2 | -o   | --output-path      | Path to the archive where the merged level will be written. | -o "path/Final.zip" \| --output-path "path/Final.zip"                                             |
| 3 | -f   | --filter           | Delete events from final **level.json** file.               | -f "event1" "event2" "eventn" \| --filtered-mode "event1" "event2" "eventn"                       |

[//]: # (| 3 | -i   | --independent-mode | Enable independent mode.                                    | -i \| --independent-mode                                                                          |)
> Warning: Do not use an existing archive to write chart files twice. **Chart.json** and **level.json** will be in two, possibly different copies in the same archive.

## For Filters
Please, type a `In file` names on filter flag.  

|    | In game             | In file           |
|----|---------------------|-------------------|
| 1  | Decoration          | deco              |
| 2  | Ease                | ease              |
| 3  | Force Player Sprite | forcePlayerSprite |
| 4  | Hall Of Mirrors     | hom               |
| 5  | Noise               | noise             |
| 6  | Outline             | outline           |
| 7  | Set BG Color        | setBgColor        |
| 8  | Set Boolean         | setBoolean        |
| 9  | Set Color           | setColor          |
| 10 | Bookmark            | bookmark          |
| 10 | Run tag             | tag               |
| 11 | Edit Paddles        | paddles           |
| 12 | Play Song           | play              |
| 13 | Set BPM             | setBPM            |
| 14 | Show Results        | showResults       |

## MergeMods
Mods to merge means how program will merge parts.

1. Independent mode - Offset part **independent** on the offset of the previous ones.
2. Sequential mode - Offset part **depends** on the offset of the previous ones.

## Thanks
Ratori(ratori6),  
Diwss(diwss),  
himych(himych_hehe),  
And me(gerutro).