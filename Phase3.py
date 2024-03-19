# tạo class light
class Light:
    def __init__(self, light_id, color):
        self.id = light_id
        self.color = color
    def __repr__(self):
        respone = Light(id={self.id}, color={self.color})
        return respone

# tạo class room
class Room:
    def __init__(self, room_id):
        self.id = room_id
        self.lights = []

    def add_light(self, light):
        self.lights.append(light)
    
    def sort_light(self):
        colors_order = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
        self.lights.sort(key=lambda )