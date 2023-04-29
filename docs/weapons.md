DoT - damage over time
AoE - area of effect


    - reload_time/cooldown_time

# weapon class
    - type:
        kinetic ( guns, cannons )
        explosive ( rockets, missiles, bombs, mines )
        energy ( lasers, photon cannons )
        nuclear ( does energy and explosive damage )

    - mass ( determine its general size used to determine what ships it fits into )
    - power_draw ( amount of power required to operate component )
    - damage ( base_damage + modifications)
    - range ( base_range + modifications )
    - accuracy ( accuracy_modifier = base_accuracy + modifications ) accuracy = d20 + acc_mod
    - targeting_system ( susceptible to counter measure systems)
      - type: heat, electronic signatures, radar ( adds bonus to accuracy but takes time to lock on )
    - ammo/charges ( current/max )
    - speed ( affect the lock-on time, reload/cooldown time )

<hr>

## kinetic
  - ammo_type: bullet, missile, rocket
  - reload_rate
  - current_ammo
  - max_ammo



### ammo
    nuclear ammo would have impact, incindiary, emp, radiation but then also leave an AoE DoT of radiation damage
      - type ( kinetic, explosive, energy, nucluer )
      - damage_type ( impact, incindiary, cryo, )
      - damage_modifier
      - travel_speed

<hr>

# counter weapon systems?
    type ( head, electronic, radar )

<hr>

## energy
  - cooldown_rate
  - focus_item?
