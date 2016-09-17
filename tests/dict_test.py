damage_cases = {
        1: {
            "police_no"     : 1,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_date"   : "2017-10-09"
        },
        2: {
            "police_no"     : 2,
            "damage_group"  : "Wertsachen",
            "damage_type"   : "einfacher Diebstahl",
            "damage_date"   : "2017-10-05"
        }
    }

dict = {1:True, 2:False}

case = damage_cases[1]
print dict[2]

