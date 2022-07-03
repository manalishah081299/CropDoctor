from base import db
from base.com.vo.crop_vo import CropVO
from base.com.vo.disease_vo import DiseaseVO
from base.com.vo.login_vo import LoginVO


class ClassificationVO(db.Model):
    __tablename__ = "classification_table"
    classification_id = db.Column("classification_id", db.Integer, primary_key=True, autoincrement=True)
    classification_login_id = db.Column("classification_login_id", db.Integer, db.ForeignKey(LoginVO.login_id))
    classification_crop_id = db.Column("classification_crop_id", db.Integer, db.ForeignKey(CropVO.crop_id))
    classification_disease_id = db.Column("classification_disease_id", db.Integer, db.ForeignKey(DiseaseVO.disease_id))
    classification_imagename = db.Column('classification_imagename', db.String(255), nullable=False)
    classification_imagepath = db.Column('classification_imagepath', db.String(255), nullable=False)
    classification_status = db.Column('classification_status', db.String(255), nullable=False)
    classification_datetime = db.Column('classification_datetime', db.DateTime)

    def as_dict(self):
        return {
            "classification_id": self.classification_id,
            "classification_login_id": self.classification_login_id,
            "classification_crop_id": self.classification_crop_id,
            "classification_disease_id": self.classification_disease_id,
            "classification_imagename": self.classification_imagename,
            "classification_imagepath": self.classification_imagepath,
            "classification_status": self.classification_status,
            "classification_datetime": self.classification_datetime,
        }


db.create_all()
