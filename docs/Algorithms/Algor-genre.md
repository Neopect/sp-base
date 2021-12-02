# Algorithm - Genre defining

## JSON Main Structure
- User Playlists
  - User1
    - plist1
      - Song
        - Song
        - Artist
        - ID
        - Features
          - Genres
            - Genre1
            - Genre2
          - Moods
            - Mood1
            - Mood2
        - User
- Global Playlists
  - plist1
  - plist2

## JSON Generated Playlists Structure
- Group Playlists
  - plist1 *Name will follow with first & last letter of name in alphabetical order*
    - Users
    - Song
      - etc
      - !include Features
  - plist2

#### Example naming scheme
*John, Sam, Dave = DeJnSm*

## JSON Daily Playlists Structure
- Daily Mix 1
  - Users
  - Day1
    - Song
    - Song
  - Day2
    - Song
    - Song
  - Exceptions
    - without x
    - without y
    - without z
    - without x,y
    - etc