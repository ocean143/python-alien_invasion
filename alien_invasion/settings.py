class Settings():

	def __init__(self):
		# 游戏界面的宽度
		self.screen_width = 1200
		# 游戏界面的高度
		self.screen_height = 800
		# 游戏界面的背景
		self.bg_color = (255, 255, 255) 
		# 飞船的移动速度
		self.ship_move_speed = 7.5

		# 子弹设置
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_speed = 5
		# 最大子弹数目
		self.bullet_maxnum = 10