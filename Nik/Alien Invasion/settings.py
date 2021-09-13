class Settings:
    #A class to store all of the settings for alien invasion

    def __init__(self):
        #initialize the games settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #bullet settings

        self.bullet_speed = 2
        self.bullet_width = 700
        self.bullet_height = 25
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        #Alien Settings
        self.alien_speed = 5
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    #ship settings
        self.ship_speed = 2
        self.ship_limit = 5
        