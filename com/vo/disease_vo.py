from base import db
from base.com.vo.crop_vo import CropVO


class DiseaseVO(db.Model):
    __tablename__ = 'disease_table'
    disease_id = db.Column('disease_id', db.Integer, primary_key=True, autoincrement=True)
    disease_name = db.Column('disease_name', db.String(255), nullable=False)
    disease_description = db.Column('disease_description', db.String(255), nullable=False)
    disease_crop_id = db.Column('disease_crop_id', db.Integer, db.ForeignKey(CropVO.crop_id))

    def as_dict(self):
        return {
            'disease_id': self.disease_id,
            'disease_name': self.disease_name,
            'disease_description': self.disease_description,
            'disease_crop_id': self.disease_crop_id
        }


db.create_all()
