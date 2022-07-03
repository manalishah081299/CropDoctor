from base import db
from base.com.vo.crop_vo import CropVO
from base.com.vo.disease_vo import DiseaseVO


class MedicineVO(db.Model):
    __tablename__ = 'medicine_table'
    medicine_id = db.Column('medicine_id', db.Integer, primary_key=True, autoincrement=True)
    medicine_name = db.Column('medicine_name', db.String(255), nullable=False)
    medicine_crop_id = db.Column('medicine_crop_id', db.Integer, db.ForeignKey(CropVO.crop_id))
    medicine_disease_id = db.Column('medicine_disease_id', db.Integer, db.ForeignKey(DiseaseVO.disease_id))

    def as_dict(self):
        return {
            'medicine_id': self.medicine_id,
            'medicine_name': self.medicine_name,
            'medicine_crop_id': self.medicine_crop_id,
            'medicine_disease_id': self.medicine_disease_id,
        }


db.create_all()
