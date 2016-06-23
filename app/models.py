from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	social_id = db.Column(db.String(64), nullable=False, unique=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	students = db.relationship('Student', backref='parent', lazy='dynamic')
    #might not be actually parent in all cases, maybe 'relevant_adult'?

	@property 
	def is_authenticated(self): 
		return True
	@property 
	def is_active(self):
 		return True

	@property 
	def is_anonymous(self):
		return False



	def get_id(self):
		try:
			return unicode(self.id) #python 2
		except NameError:
			return str(self.id) #python 3
	def get_students(self):
		return self.students

	def __repr__(self):
		return '<User %r>' % (self.nickname)


class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post %r>' % (self.body)
