# kotomo

kotomo is a tamagotchi-style game about caring for virtual pets.

## dependencies

- python3
- pygame

## instalation

clone the repo and launch with
```
python main.py
```

## how to play

the goal of the game is to keep your pets alive.

each pet has 4 values associated with it:
    - **health** - you cannot influence it directly, but it is calculated using all of other values instead,
    - **hunger**,
    - **thirst**,
    - **happiness**.

these values decrease as time passes.
you can improve your pets' status by feeding them food (done by clicking **on the food**) or by cuddling (by clicking **on the pet**).

each type of food increases different stats. cuddling will only increase your pet's happiness - however, not cuddling the pet often enough will have a large impact on happiness, even if the food you feed it increases that particular stat!

the game uses a local save to keep each pet's status - stats decrease even if the game is not launched.

if a pet's health goes down to 0 at any point, then it becomes **dead**. dead pets' stats cannot be altered in any way - they're gone for good, so try to keep them alive and well!