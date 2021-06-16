#-------------------------------------------------------------------
# Program by Vycheslav.H.
#
#
# Version   Date    Info
# 1.0       2021    Lesson
#
#------------------------------------------------------------------

class Warior():
    """Class for game HERO"""
    def __init__(self, login, level, skill):
        """Initiate a Hero"""
        self.login = login
        self.level = level
        self.skill = skill
        self.heath = 100

    def show_hero(self):
        """Show all parametrs of this Hero"""
        message_parametrs = (self.login + " Level is: " + str(self.level) + " Skill is: " + str(self.skill) + " Health is: " + str(self.heath)).title()
        print(message_parametrs)

    def level_up(self):
        """Level up Hero"""
        self.level = self.level + 1

    def move (self):
        """Moving Hero"""
        print("Hero " + self.login + " start moving...")

    def set_heath(self, new_health):
        self.heath=new_health

new_hero1 = Warior("Guru", 1, 1)
new_hero2 = Warior("Novice", 2, 2)

new_hero1.show_hero()
new_hero2.show_hero()
new_hero1.move()
new_hero2.set_heath(90)
new_hero2.show_hero()
