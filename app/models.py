from . import db 
class List (db.Model):
	__tablename__='account_list'
	al_data=db.Column(db.Date)
	al_item=db.Column(db.varchar(20))
	al_price=db.Column(db.Float)
class Role(db.Model):
	__tablename__='account_book'
	ab_id=db.Column(db.Integer,primary_key=True)
	ab_list=db.Column(db.Date）
	ab_amount=db.Column(db.Float)
	ab_comment=db.Column(db.String(100))
