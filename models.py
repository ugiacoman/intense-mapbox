from app import db
from sqlalchemy.dialects.postgresql import JSON


'''
Provider Table:

	id: (Foreign key references id in Provider Table)
	name:
	is_hospital: Boolean

'''
class Provider(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(200))
	is_hospital = db.Column(db.Boolean)

	def __init__(self, id, name, is_hospital):
		self.id = id
		self.name = name
		self.is_hospital = is_hospital
		

'''
Diagnosis Table:

	procedure: 
	provider_id: (Foreign key references id in Provider Table)
	avg_total_payments:
	avg_medicare_payments:
	avg_covered_charges:
	total_discharge: 

'''
class Diagnosis(db.Model):
	procedure = db.Column(db.Integer, primary_key=True)
 	provider_id = db.Column(db.Integer, ForeignKey("Provider.id"), primary_key=True)

	avg_total_payments = db.Column(db.Numeric(precision=2, asdecimal=True))
	avg_medicare_payments = db.Column(db.Numeric(precision=2, asdecimal=True))
	avg_covered_charges = db.Column(db.Numeric(precision=2, asdecimal=True))
	total_discharge = db.Column(db.Numeric(precision=2, asdecimal=True))

	def __init__(self, procedure, provider_id, avg_medicare_payments, avg_total_payments, 
		avg_covered_charges, total_discharge):
		self.procedure = procedure
		self.provider_id = provider_id
		self.avg_total_payments = avg_total_payments
		self.avg_medicare_payments = avg_medicare_payments
		self.avg_covered_charges = avg_covered_charges
		self.total_discharge = total_discharge		


'''
Location Table:

	id: (Foriegn key references id in Provider Table)
	city:
	street_address:
	state:
	zip_code:

'''
class Location(db.Model):
	id = db.Column(db.Integer, ForeignKey("Provider.id"), primary_key=True)

	city = db.Column(db.String(100))
	street_address = db.Column(db.String(200))
	state = db.Column(db.String(2))
	zip_code = db.Column(db.Integer)

	def __init__(self, id, city, street_address, state, zip_code):
		self.id = id
		self.city = city
		self.street_address = street_address
		self.state = state
		self.zip_code = zip_code

