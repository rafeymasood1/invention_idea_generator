import random


class RandomInventionIdeas:
    def __init__(self, material, powered_by, movements, size, actual_thing, location):

        self.material = material
        self.powered_by = powered_by
        self.movements = movements
        self.size = size
        self.actual_thing = actual_thing
        self.location = location

        text = "We will give a unique invention idea to you!, every keyword we return to you will be completely random so you will have to crack it yourself! "
        self.about_it = text

    def role_all_dice(self):

        material_choice = random.choice(self.material)
        powered_by_choice = random.choice(self.powered_by)
        movements_choice = random.choice(self.movements)
        size_choice = random.choice(self.size)
        actual_thing_choice = random.choice(self.actual_thing)
        location_choice = random.choice(self.location)

        print(f" {actual_thing_choice} {movements_choice}")


# In[6]:


material_1 = ["wood", "paper", "metal", "sand", "fabric", "plastic"]
powered_by_1 = ["manual", " electric", "digital", "wind", "water", "radiowave"]
movement_1 = ["flys", "under_water", "on_road", "secret_agent", "stationary", "solar"]
size_1 = ["mini", "giant", "portable", "inhabitable", "wearable", "pocket"]
actual_thing_1 = ["robot", "vehicle", "tool", "game", "app", "art"]
location_1 = ["home", "office", "industrial", "public", "personal", "agriculture"]

idea_1 = RandomInventionIdeas(
    material_1, powered_by_1, movement_1, size_1, actual_thing_1, location_1
)


# In[7]:


idea_1 = RandomInventionIdeas(
    material_1, powered_by_1, movement_1, size_1, actual_thing_1, location_1
)
idea_1.role_all_dice()


# In[ ]:
