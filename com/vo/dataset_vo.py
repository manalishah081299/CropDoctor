from base import db

from base.com.vo.disease_vo import DiseaseVO


class DatasetVO(db.Model):
    __tablename__ = 'dataset_table'
    dataset_id = db.Column('dataset_id', db.Integer, primary_key=True, autoincrement=True)
    dataset_disease_id = db.Column('dataset_disease_id', db.Integer, db.ForeignKey(DiseaseVO.disease_id))
    dataset_description = db.Column('dataset_description', db.String(255), nullable=False)
    dataset_imagename = db.Column('dataset_imagename', db.String(255), nullable=False)
    dataset_imagepath = db.Column('dataset_imagepath', db.String(255), nullable=False)
    dataset_datetime = db.Column('dataset_datetime', db.DATETIME)

    def as_dict(self):
        return {
            'dataset_id': self.dataset_id,
            'dataset_disease_id': self.dataset_disease_id,
            'dataset_description': self.dataset_description,
            'dataset_imagename': self.dataset_imagename,
            'dataset_imagepath': self.dataset_imagepath,
            'dataset_datetime': self.dataset_datetime

        }


db.create_all()
