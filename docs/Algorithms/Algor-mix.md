# Steps for processing data

1. Copy URL from file
2. Format uri
3. Read each playlist
   - Copy song name, artist, and uri


# Playlist Types
- Mix it up (Commines random list of songs from each person)
  - MIU Exceptions (Same as main, but has variants without people)
- Daily Rotation (Creates master playlist, then breaks it apart into multiple sequences)

## Playlist folder structure
- Bot
  - Master Mix it up
    - Everyone
    - Withouts
      - Without x
      - Without y
      - Without z & a
  - Daily Rotations
    - Day 1
      - Everyone
      - Withouts
        - Without x
        - Without y
        - Without z & a
    - Day 2
      - Everyone
      - Withouts
        - Without x
        - Without y
        - Without z & a
    - Day 3
      - Everyone
      - Withouts
        - Without x
        - Without y
        - Without z & a


# Playlist Variable structure
- Playlists
  - play1
    - song1
      - name
      - artist
      - id
    - song2
    - song3
  - play2
  - play3

# Algorithm

## Rotation

### Create randoms
1. Dup playlists into a active and secondary playlist
2. Take the smallest playlist and have the set be the split value
3. Copy # random songs to active and remove them from secondary
4. Repeat step 3 times

### Exceptions
1. Check for Exceptions
2. Don't include playlist in mix

### Mix
1. Create playlist from each set to 1 list
2. Randomly move songs around

### Dup Check
1. If same song is present remove dup
2. Add random song from Uni list


## On Demand creation
1. Check if similar track is made
2. Create playlist based on users
3. Upload playlist
4. Fetch all playlist
5. Filter playlist by name and grab id
6. Play playlist


# Algorithm (Long version)
- [X] Read config
  - [X] Create config file
  - [X] Read config file
  - [X] Clean data
  - [X] Convert URL to proper playlist
  - [X] Mark down names
  - [X] Set everything to global
- [X] Download playlist data
  - [ ] Check if it should re-download the playlist
  - [ ] Read files instead of downloading
  - [X] Read each url and download json of track data
  - [X] Format json string to python list
  - [X] Loop through the entire playlist
  - [X] Copy temp list to master list
- [ ] Handle exceptions
  - [ ] Read users list and tell which to ignore
  - [ ] Remove the user and playlist index from both lists
- [ ] Explicit content
  - [ ] If the song is explicit remove it from list
- [X] Mixing lists
  - [X] Take 50 songs from each playlist and add them to active list
  - [X] Remove copied songs from org list
  - [X] Add global playlist
  - [ ] Remove dups and replace with global
  - [X] Repeat 3 times
  - [ ] Re-loop playlist if less than 150 tracks