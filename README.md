# PyStar

## Enemy extends Entity
- ship:<Ship>

## Player extends Entity
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