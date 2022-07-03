from base import db
from base.com.vo.classification_vo import ClassificationVO
from base.com.vo.crop_vo import CropVO
from base.com.vo.disease_vo import DiseaseVO


class ClassificationDAO:
    def insert_classification(self, classification_vo):
        db.session.add(classification_vo)
        db.session.commit()

    def view_classification(self, classification_vo):
        classification_vo_list = db.session.query(ClassificationVO, DiseaseVO, CropVO) \
            .filter_by(classification_login_id=classification_vo.classification_login_id) \
            .join(DiseaseVO, ClassificationVO.classification_disease_id == DiseaseVO.disease_id) \
            .join(CropVO, ClassificationVO.classification_crop_id == CropVO.crop_id) \
            .all()
        return classification_vo_list
