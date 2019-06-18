# Team Splitter

This is a simple piece of code written with Python 3 that splits a X number of people into a Y number of teams. The program will query the the number of people as well as the number of teams, the names of the people and teams, and randomly and evenly distribute them.

### How it works:

In summary, the program shuffles names of people in a list, taking the first N number and putting them into Team A, followed by the next N number in to Team B and so on. Remainder people are sorted randomly into teams.

After this the program will query you if you want to save the team allocation in a text file. Whether the user chooses to do so or not, it will then query whether the user wishes to restart or close the program.

### Side notes:

- The program will not allow only blanks for names of people as well as teams. 
- Users will be able to enter 5 fullstops [.....] followed by an enter at any time to exit the program.
- Duplicate team names and person names are not allowed.
- The program takes into account remainder people, and will distribute them evenly and randomly into teams.
- The text files will be saved into a folder named "Saved files". It will not allow the user to replace existing files/rename the files currently there.
