#coding=utf-8

import buff_data
import Timer

class BuffBase(object):
	def __init__(self, buff_id, duration):
		self.owner = None
		self.buff_id = buff_id
		self.duration = duration

	def set_owner(self, owner):
		self.owner = owner

	def start(self):
		pass

	def end(self):
		pass

class TimerBuffBase(BuffBase):
	def __init__(self, buff_id, duration):
		super(TimerBuffBase, self).__init__(buff_id, duration)

	def on_timer(self):
		pass

	def start(self):
		super(TimerBuffBase, self).start()
		static_data = buff_data.get(buff_id, {})
		timer_interval = static_data.get('timer', 0)
		self.timer = Timer.addRepeate(timer_interval, lambda: self.on_timer())

		self.on_timer()

	def end(self):
		super(TimerBuffBase, self).end()
		self.timer.cancle()

class Buff_1(TimerBuffBase):
	'''
	fire
	'''
	def on_timer(self):
		self.owner.hp -= 1
