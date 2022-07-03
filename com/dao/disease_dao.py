from base import db
from base.com.vo.crop_vo import CropVO
from base.com.vo.disease_vo import DiseaseVO


class DiseaseDAO:
    def insert_disease(self, disease_vo):
        db.session.add(disease_vo)
        db.session.commit()

    def view_disease(self):
        disease_vo_list = db.session.query(DiseaseVO, CropVO) \
            .join(CropVO, DiseaseVO.disease_crop_id == CropVO.crop_id) \
            .all()
        return disease_vo_list

    def delete_disease(self, disease_vo):
        disease_vo_list = DiseaseVO.query.get(disease_vo.disease_id)
        db.session.delete(disease_vo_list)
        db.session.commit()

    def edit_disease(self, disease_vo):
        disease_vo_list = DiseaseVO.query.filter_by(disease_id=disease_vo.disease_id).all()
        return disease_vo_list

    def update_disease(self, disease_vo):
        db.session.merge(disease_vo)
        db.session.commit()

    def find_disease_id(self, disease_vo):
        disease_vo_list = DiseaseVO.query.filter_by(disease_name=disease_vo.disease_name).all()
        disease_id = disease_vo_list[0].disease_id
        return disease_id
