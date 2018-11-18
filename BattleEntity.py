#coding=utf-8

from SkillBase import SkillBase

def create_skill(battle_entity, skill_id):
	try:
		skill_class = imp.load_module()
	except:
		skill_class = SkillBase
	return skill_class(battle_entity, skill_id)

class BattleEntity(object):
	def __init__(self, hero_data, skill_data):
		self.init_base_property(hero_data)
		self.init_skill(skill_data)

	def init_base_property(self, hero_data):
		''' hp, mp, lv etc.
		'''
		self.hp = 100
		self.mp = 100
		self.hero_id = 1

	def init_skill(self, skill_data):
		''' add skills
		'''
		pass

	def check_can_use(self, skill_id):
		return True

	# CLIENT_ONLY
	def use_skill(self, skill_id):
		err = self.check_can_use(skill_id)
		if err == 0:
			skill = create_skill(self, skill_id)
			skill.start()
		else:
			print("error use skill")

	# CLIENT_ONLY
	def xuli_finish(self):
		pass
