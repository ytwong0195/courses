from system.core.controller import *
class Courses(Controller):
	def __init__(self, action):
		super(Courses, self).__init__(action)
		self.load_model('Course')

	def index(self):
		course = self.models['Course'].get_all_courses()
		return self.load_view('index.html', course=course)

	def show(self,id):
		course = self.models['Course'].get_course_by_id(id)
		return self.load_view('show.html', course=course)

	def add(self):
		post = request.form
		if len(post['title'])<15:
			flash ("Course name must be at least 15 characters")
			print "less than 15"
			return redirect('/')
		else:
			course_details = {
			'title':post['title'],
			'description': post['description']
			}
			flash ("New course added!")
			self.models['Course'].add_course(course_details)
			return redirect('/')

	# def update(self,course_id):
	# 	course_details={
	# 	'id': course_id,
	# 	'title': post['name'],
	# 	'description': post['description']		
	# 	}
	# 	self.models['Course'].update_course(course_details)
	# 	return redirect('/')

	def delete(self,id):
		self.models['Course'].delete_course(id)
		return redirect('/')
