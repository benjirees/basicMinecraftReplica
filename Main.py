from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
grassBlock = load_texture('assets/GrassNew.png')
stoneBlock = load_texture('assets/stoneBlock.png')
woodBlock = load_texture('assets/woodBlock.png')
dirtBlock = load_texture('assets/dirtBlock.jpg')
block_pick = 1

images = [grassBlock, stoneBlock, woodBlock, dirtBlock]

window.fps_counter.enabled = False
window.exit_button.visible = False

def update():
	global block_pick

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if held_keys['1']: 
		block_pick = 1

	if held_keys['2']: 
		block_pick = 2

	if held_keys['3']: 
		block_pick = 3

	if held_keys['4']: 
		block_pick = 4

	#if held_keys['5']:
		#block_pick = 5

class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				if block_pick == 1: 
					voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: 
					voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: 
					voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: 
					voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				#if block_pick = 5:
					#voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
			if key == 'right mouse down':
				destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150, -10, 0),
			position = Vec2(0.4, -0.6))

	def active(self):
		self.position = Vec2(0.3, -0.5)

	def passive(self):
		self.position = Vec2(0.4, -0.6)

class Inventory(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'quad',
			scale = (.5, .8),
			origin = (-.5, .5),
			position = (0, 0),
			texture = 'white_cube',
			texture_scale = (4,1),
			color = color.dark_gray
			)

		self.item_parent = Entity(parent=self, scale=(1/5, 1/8))

	def find_free_spot(self):
		taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
		for y in range(8):
			for x in range(5):
				if not (x,-y) in taken_spots:
					return(x,-y)

	def append(self, item):
		icon = Button(
			parent = inventory.item_parent,
			model = 'quad',
			origin = (-.5, .5),
			color = color.color(0,0,random.uniform(0.9,1)),
			position = self.find_free_spot(),
			z = -.1,
			texture = grassBlock)

for z in range(20):
	for x in range(20):
		voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
sky = Sky()
hand = Hand()
#inventory = Inventory()

#for i, img in enumerate(images):
	#inventory.append(images[i])

app.run()