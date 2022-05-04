# Data Processing Workflow

### Basic Conversion flow
1. Spotify json
2. Shorten json
3. SQL



# File organization preview
---

## playlist.json (Part 1)
```
NA
```



## plist.json (Part 2)
```
[
    "name": "user"
    [
        "Song",
        "Artist",
        "Duration (converted to min float)",
        "Explicit condition",
        "Spotify ID",
        "Preview URL",
        [
            "Genre"
        ],
        [
            "Mood"
        ]
    ]
]
```


## db.sql (Part 3)
*Songs table:*
| ID                 | song | artist | dur   | exp     | spotid | purl |
|--------------------|------|--------|-------|---------|--------|------|
| str(`song-artist`) | str  | str    | float | boolean | str    | str  |

*Owners table:*
| ID                 | name1   | name2   | name3   | name4   | name5   | name(#)... |
|--------------------|---------|---------|---------|---------|---------|------------|
| str(`song-artist`) | boolean | boolean | boolean | boolean | boolean | boolean    |

*Users table:*
| ID         | fname | lname | group1 | group2 | pulled      | purged      |
|------------|-------|-------|--------|--------|-------------|-------------|
| randint(6) | str   | str   | str    | str    | str(`date`) | str(`date`) |

*Groups table:*
| ID         | name |
|------------|------|
| randint(3) | str  |

*Genre&Mood table:*
| ID                 | gen1    | gen2    | gen3    | mood1   | mood2   | mood(#)... |
|--------------------|---------|---------|---------|---------|---------|------------|
| str(`song-artist`) | boolean | boolean | boolean | boolean | boolean | boolean    |