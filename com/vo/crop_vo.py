from base import db


class CropVO(db.Model):
    __tablename__ = 'crop_table'
    crop_id = db.Column('crop_id', db.Integer, primary_key=True, autoincrement=True)
    crop_name = db.Column('crop_name', db.String(255), nullable=False)
    crop_description = db.Column('crop_description', db.String(255), nullable=False)

    def as_dict(self):
        return {
            'crop_id': self.crop_id,
            'crop_name': self.crop_name,
            'crop_description': self.crop_description
        }


db.create_all()
