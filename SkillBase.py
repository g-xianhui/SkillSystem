#coding=utf-8

import BuffHelpers

class SkillBase(object):
	def __init__(self, owner, skill_id):
		self.owner = owner

	def destroy(self):
		self.owner = None

	def init_skill_graph(self, skill_id):
		'''
		register event timer, graph data will be like:
		(
			(0.1, (damage, target_selector, caculate_formula)),
			(0.2, (heal, target_selector, caculate_formula)),
			(0.3, (add_buff, target_selector, buff_id, duration)),
			(0.4, (user_message_1, user_define_data))
		)
		'''
		pass

	def start(self):
		self.init_skill_graph(skill_id)

	def interup(self):
		pass

	def add_buff(self, target, buff_id, duration):
		buff = BuffHelpers.create_buff(buff_id, duration)
		target.add_buff(buff)

	def heal(self, target, hp):
		pass

	def damage(self, target, hp):
		pass

	def on_user_message_1(self, data):
		'''
		special event, each specific skill explain itself
		'''
		pass
