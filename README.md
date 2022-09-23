# Multiplayers Rock Paper Scissors
I was messing around with `socket`'s and wanted to make something with it because it seemed cool and decided a multiplayer game was a good way of applying my skills. What better game then Rock Paper Scissors?  
**NOTE**: This is simply a small project and only a small example, so a lot of the code isn't made to reflect what an *actual* multiplayer game would be built like or created. It's simply optimized to work on a single computer, with multiple scripts (servers, clients) running.

## Features
* Multiplayer allows for you to play with other people
    * Well, in this case, only on the same computer since the server uses `localhost` (127.0.0.1.)
* For offline players, includes a bot over multiplayer play
* Allows private servers to be setup
    * Again, in this case only on your own computer, but still works as a "private" server anyways

## Problems
So one main problem I wanted to highlight is that since this is just a simple project, I really don't feel like doing *too* much on error handling. Yes, I'll implement some basic error handling and what not but I really don't wanna plan for every single contingincy ever and make it perfect. That would take me too much time and give me headaches so yeah. And also frankly, I don't wanna worry about the [Two Generals' Problem](https://en.wikipedia.org/wiki/Two_Generals%27_Problem "Two Generals' Problem(Networking) - Wikipedia) at all right now. Maybe in the future...

## TODO
- [ ] Add "Best of" gamemode
- [ ] Add "Rock Paper Scissors Lizard Spock" gamemode
- [ ] Add "1-Match, 3-People" gamemode
- [ ] Add "4-Person Tournament" gamemode
- [ ] Add RPS-101 gamemode (Realistically, I won't add this unless I get *to* bored. No one is gonna play a 101 battle royale. I don't even know 75 people.)
- [ ] Add Specialised Servers and Server Browser (Alpha servers are normal, Bravo Servers are "Best of", etc.)
- [ ] Add "Time limits" rule
- [ ] Add Custom Items
