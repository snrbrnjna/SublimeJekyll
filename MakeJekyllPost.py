import sublime, sublime_plugin
import datetime

header = '''---
layout: post
date: %s %s
title: "%s"
categories: 
tags: 
published: true
author: 
embed: 
---
'''

def make_post_date():
	now = datetime.datetime.now()
	file_date = now.strftime("%Y-%m-%d")
	return file_date

def make_post_time():
	now = datetime.datetime.now()
	file_time = now.strftime("%H-%M-%S")
	return file_time

def make_file_name(title_input):
	jek_date = make_post_date()
	jek_title = title_input.lower().replace(' ','-')
	jek_file_type = '.md'
	jek_post_title = jek_date + '-' + jek_title + jek_file_type
	return jek_post_title

class MakeJekyllPostCommand(sublime_plugin.WindowCommand):
	
	def on_done(self, title):
		new_post = self.window.new_file()
		post_title = make_file_name(title)
		new_post.set_name(post_title)

		new_header = header % (make_post_date(), make_post_time(), title)
		
		edit = new_post.begin_edit()
		new_post.insert(edit, 0, new_header)
		new_post.end_edit(edit)

	def run(self):
		self.window.show_input_panel("Post Title:", "", self.on_done, None, None)
