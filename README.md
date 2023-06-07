# Liber Characterum
### A Character Creator Application for Warhammer 40k TTRPGs

In the grim darkness of the 41st millennium, it's a bit annoying to try and build a new character for your tabletop games. LC is here to try and make that a bit easier.

## How to Use

Currently, only the client folder has any usable code. To make or view a character file, run client/main.py in your editor of choice.


## Books Supported
- [ ] Black Crusade
    - [ ] Core Rulebook
    - [ ] Tome of Blood
    - [ ] Tome of Decay
    - [ ] Tome of Excess
    - [ ] Tome of Fate


## To Do List

- [ ] Character Creation
  - [X] Bugfix: When changing race, does not reset Archetype selection or Characteristics
  - [ ] Configure Skill selection when there is an Any choice as an option (Ex. Forsaken)
  - [ ] Configure special Passion bonuses/penalties
    - [ ] Wealth Pride
    - [ ] Betrayal Disgrace
    - [ ] Greed Disgrace
    - [ ] Regret Disgrace
    - [ ] Perfection Motivation
  - [ ] Add Starting Gear to New Character Window
  - [ ] Configure Starting Psychic Power selection for psykers
  - [ ] Add warning on Create if missing or incorrect data
- [ ] Data
  - [ ] Add weapon Descriptions
  - [ ] Create csvs
    - [ ] Cybernetics
    - [ ] Force Fields
    - [ ] Mutations
    - [ ] Weapon/Armor Augments
    - [ ] Weapon Properties
  - [ ] Populate csvs
    - [ ] Gear
- [ ] Character Sheet
  - [ ] Characteristics Tab
    - [ ] Add ability to change Character Portrait
    - [ ] Fix formatting for top row
    - [ ] Add labels for Portrait, alignment, and description
    - [ ] Add functionality to purchase skill training advancements
  - [ ] Traits and Talents
    - [ ] Configure Add Talent button
    - [ ] Add Mutations?
  - [ ] Equipment
    - [ ] Fix rendering 'nan' in info
    - [ ] Configure Add Weapon and Add Armor to actually add new equipment
    - [ ] Add 'Equipped' toggle for Armor and Force Field
    - [ ] Add Force Field info
    - [ ] Configure Add Force Field button
    - [ ] Add functionality to Armor Coverage picture
    - [ ] Fix Armor Coverage picture sizing
  - [ ] Gear
    - [ ] Configure Add Gear button
    - [ ] Separate gear into Categories?
  - [ ] Powers
    - [ ] Configure Add Power button to actually add new power
    - [ ] Add more filters to Add Power selection
  - [ ] Advancements
    - [ ] Add functionality to keep track of spent XP
    - [ ] Add Alignment tracking
      - [ ] Factor Alignment into XP costs
    - [ ] Add Purchased Advancements info
    - [ ] Add info on click functionality
  - [ ] Configure Save button to update character json

## Future Concerns
  - Custom Races, Archetypes, Talents, and Equipment
  - Daemon Prince Characters
  - Adventure Log
  - Crusade Forces Tab
  - Add hover window for info, instead of clicking?
  - Executable file for installation and running
  - PDF export of character sheet