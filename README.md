# Multiplayers Rock Paper Scissors
I was messing around with `socket`'s and wanted to make something with it because it seemed cool and decided a multiplayer game was a good way of applying my skills. What better game then Rock Paper Scissors?  

## Features
* Multiplayer allows for you to play with other people
    * Well, in this case, only on the same computer since the server uses `localhost` (127.0.0.1.)
* For offline players, includes a bot

## Problems
So one main problem I wanted to highlight is that since this is just a simple project, I really don't feel like doing *too* much on error handling. Yes, I'll implement some basic error handling and what not but I really don't wanna plan for every single contingincy ever and make it perfect. That would take me too much time and give me headaches so yeah.

## TODO
- [ ] Add a server browser (Multiple different servers)
- [ ] Add "Private" Servers (Privatly Hosted Servers)
- [ ] Add "Rock Paper Scissors Lizard Spock" gamemode
- [ ] Add "Best of" gamemode
- [ ] Add "4-Person Tournament" gamemode
- [ ] Implement a queue system for servers (Since servers have different game modes, the queue system should also choose which server to queue for. Whichever has less people in line will be the chosen server)
- [ ] Add settings so they user can change features (example: supress command line colors)
- [ ] Add a GUI (Should still allow users to play in either GUI or Command-Line mode)
- [ ] Recreate game in Rust (Would be cool to make it in a compiled language)
