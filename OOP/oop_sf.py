"""
oop_sf.py
street fighter
Ryu
Ken
Honda
https://i.ytimg.com/vi/-iptPtdN-bo/maxresdefault.jpg
https://i.pinimg.com/originals/6b/10/a7/6b10a706d1b7fc687e14d8d48bf05cee.jpg
https://cdn.vox-cdn.com/thumbor/OfHpyMTIomN3n05pNWl1o4-WW7s=/0x19:960x522/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/19591750/SIGIL_Imp_in_body.png
https://i.ytimg.com/vi/MiBDl_82BWw/maxresdefault.jpg
bottom-up/top
top->bottom
- health
- hangi atak ne kadar azaltiyor?
- atak yaparken, hangisi gelecek, random yapalım.
"""

# %%

import random
import time


class Fighter:
    def __init__(self):
        self._health = 100

    def get_health(self):
        return self._health

    def lower_health(self, damage):
        self._health = self._health - damage


class Honda(Fighter):
    def __init__(self):
        super().__init__()
        self._health = 120

    def punch(self):
        how_much = random.randint(10, 20)
        return how_much

    def kick(self):
        how_much = random.randint(10, 20)
        return how_much

    def special(self):
        how_much = random.randint(20, 30)
        return how_much


class Ryu(Fighter):
    def __init__(self):
        super().__init__()

    def punch(self):
        how_much = random.randint(14, 24)
        # sprite goster
        return how_much

    def kick(self):
        how_much = random.randint(20, 35)
        return how_much

    def special(self):
        how_much = random.randint(22, 28)
        return how_much


class Scene:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def _attack(self, attacking_fighter, attacked_fighter):
        which_attack = random.randint(1, 10)
        # 1..4 -> punch
        # 5..9 -> kick
        # 10 -> special
        if which_attack in [1, 2, 3, 4]:
            how_much = attacking_fighter.punch()
            print("punch:", how_much)
        elif which_attack in [5, 6, 7, 8, 9]:
            how_much = attacking_fighter.kick()
            print("kick:", how_much)
        else:
            how_much = attacking_fighter.special()
            print("special:", how_much)
        attacked_fighter.lower_health(how_much)

    def let_them_fight(self):
        # print(self.fighter1.get_health())
        # print(self.fighter2.get_health())

        done = False
        while not done:
            self._attack(self.fighter1, self.fighter2)
            self._attack(self.fighter2, self.fighter1)
            print(self.fighter1.get_health(), self.fighter2.get_health())

            if self.fighter1.get_health() <= 0 and self.fighter2.get_health() <= 0:
                print("draw: double KO")
                done = True
            else:
                if self.fighter1.get_health() <= 0:
                    print("fighter2 wins!")
                    done = True
                elif self.fighter2.get_health() <= 0:
                    print("fighter1 wins!")
                    done = True
            time.sleep(2)


def main():
    # Ryu: class, blueprint, plan
    ryu1 = Ryu()  # ryu1: object, instance, nesne
    honda1 = Honda()
    scene1 = Scene(ryu1, honda1)
    scene1.let_them_fight()
    # turn based
    # oyun bitene kadar, her karaktere 1er söz verecek.

    print("game over")


if __name__ == "__main__":
    main()