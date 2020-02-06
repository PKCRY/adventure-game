import scenes

class Map(object):
    #These are all of the different traversible scenes
    #Commented out scenes will be added later
    scenes = {
        'death': scenes.Death(),
        'tavern': scenes.Tavern(),
        'town_center': scenes.TownCenter(),
        'general_store': scenes.GeneralStore(),
        'trader_wagon': scenes.TraderWagon(),
        'road_out_of_town': scenes.RoadOutOfTown(),
        'gloomy_forest': scenes.GloomyForest(),
        'imbued_ruins_entrance': scenes.ImbuedRuinsEntrance(),
        #'imbued_ruins_fountain': scenes.ImbuedRuinsFountain(),
        #'imbued_ruins_throne': scenes.ImbuedRuinsThrone(),
        #'imbued_ruins_garden': scenes.ImbuedRuinsGarden(),
        'imbued_ruins_treasure': scenes.ImbuedRuinsTreasure(),
        'somber_mountains': scenes.SomberMountains(),
        'ancient_mines_entrance': scenes.AncientMinesEntrance(),
        #'ancient_mines_main_hall': scenes.AncientMinesMainHall(),
        #'ancient_mines_forge': scenes.AncientMinesForge(),
        #'ancient_mines_jail': scenes.AncientMinesJail(),
        'ancient_mines_treasure_room': scenes.AncientMinesTreasureRoom()

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def change_scene(self, scene_name):
        new_scene = Map.scenes.get(scene_name)
        return new_scene

    def opening_scene(self):
        return self.change_scene(self.start_scene)
