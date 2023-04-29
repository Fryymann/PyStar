# PyStar

## Entity
#### Represents an object in space, organic and inorganic alike.
- name:string
- coordinate_x:int
- coordinate_y:int

## Enemy extends Entity
#### Represents an NPC "opponent"
- ship:<Ship>

## Player extends Entity
#### Represents the Player. Contains properties and methods needed to interact with the game
- ship:<Ship>
- can communicate some how: chat, broadcast, chat-room style, global chat

## Asteroid extends Entity

- mass:int determines damage done to object colliding with it

<hr>

## Ship extends Entity

- name : string
- hull_max:int only protect against physical damage
- hull_current:int
- shields_max:int only protect againt energy damage
- shields_current:int
- weapon : <Weapon>
- speed_max:int max number of spaces moved per tick
- speed_current:int current number of spaces moved per tick
- acceleration_rate:int how many ticks it takes to increase speed by 1
- current_power:int ( phase 2 )
- evasion_rating: ( phase 2 )
- status ( in_combat, idle, etc... )
- target: <Ship> | null
- pilot: <Player>|<Enemy>
- radar_hp:int how much damage before it stops working and you are blind

<hr>

## Weapon

- name
- range:int
- damage_die:int type of die rolled
- damage_type: [projectile, energy, etc...]
- speed

<hr>

## Space

- occupant:<Entity>
- coords(x,y)

## Entity superclass of Player, Enemy, Asteroid, Ship

- location:<Space>
- name

## The Game Itself

- map: 2 dimensional array filled with <Space> objects

```

~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ! ~ ~ ~ ~ ~ ~ ~
~ * ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ * ~ ~ ~ ~ ~ ~ ~ ~
~ ~ * ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ * ~ # ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ! ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

Hull: 200/200 | Shields: 150/200 | Power: 85%
Nearby: Enemy Interceptor, Kaleb

> target enemy
> fire


```

<hr>

## handling player input

input() returns a string representing the values of the
command_name and the options_string.

- we need to split the string returned from input() into a list
- the first item in the list should be the command_name
- the second item in the list should be the option_string

> write a function that takes a string as an argument and returns a list with two items: [ command_name, options_string ]

    "chat Hi my name is Dood!" --> [ 'chat', 'Hi my name is Dood!' ]

## processing comamnds

after the input is processed, the `command_name` on the `command_list` is then used to determine which command to pass the `options_string` variable to

- using the command_name at `command[0]` find the matching command function and pass the `options_string` as an argument.
- if no command matching the `command_name` is found, set the `GAME_MESSAGE` with a string representing a message informing the player that their input does not match an existing command.

> write a function that takes a list `command_list` as an argument
> the list will have 2 elements `command_name` and `options_string`
>


<hr>

# team stuff
- stations in the ship for each player
    - captain - ship orientation, travel speed & direction
    -

    ship responsibilities
    1. orientation ( N E S W U D )
    2. weapons
    3. shields
    4. thrusters
    5. power
    6. counter weapons


```js
let wimpOut = -10
const DC_FACTOR = 18

while (battle === true)
    // if enemy took damage: wimpOut += 5
  if (randomNumber(1-20) + wimpOut > DC_FACTOR){
      // enemy flees
  }
  decision = randomNumber(1-20)
  switch(decision)
      case 1 - 10:
          // do counter measures, defensive stuff
      case 11 - 20:
            // attack, lock-on, aggressive stuff

```
