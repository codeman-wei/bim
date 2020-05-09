from flask_web import db

class Sections(db.Model):
	"""docstring for ClassName"""
	__tablename__ = 'sections'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	sectionsname = db.Column(db.String(255), nullable=True)
	def __init__(self, sectionsname):
		super(Sections, self).__init__()
		self.sectionsname = sectionsname




class SysMonitor(db.Model):
	"""docstring for ClassName"""
	__tablename__ = 'sysmonitor'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	sections_id = db.Column(db.Integer, nullable = True)
	stresses = db.Column(db.String(255))
	shape = db.Column(db.String(255))
	temperature = db.Column(db.String(255))
	humidity = db.Column(db.String(255))
	windpower = db.Column(db.String(255))
	day = db.Column(db.DateTime, nullable = True)
	def __init__(self, sections_id, stresses, shape, temperature, humidity, windpower, day):
		super(Sections, self).__init__()
		self.sections_id = sections_id
		self.stresses = stresses
		self.shape = shape
		self.temperature = temperature
		self.humidity = humidity
		self.windpower = windpower
		self.day = day

	def to_json(self):
		json_data = {
			'id' : self.id,
			'sections_id': self.sections_id,
			'stresses': self.stresses,
			'shape': self.shape,
			'temperature': self.temperature,
			'humidity': self.humidity,
			'windpower': self.windpower,
			'day' :self.day
		}
		return json_data