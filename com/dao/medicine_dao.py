from base import db
from base.com.vo.crop_vo import CropVO
from base.com.vo.disease_vo import DiseaseVO
from base.com.vo.medicine_vo import MedicineVO


class MedicineDAO:
    def insert_medicine(self, medicine_vo):
        db.session.add(medicine_vo)
        db.session.commit()

    def view_medicine(self):
        medicine_vo_list = db.session.query(MedicineVO, DiseaseVO, CropVO) \
            .join(DiseaseVO, MedicineVO.medicine_disease_id == DiseaseVO.disease_id) \
            .join(CropVO, MedicineVO.medicine_crop_id == CropVO.crop_id) \
            .all()
        return medicine_vo_list

    def delete_medicine(self, medicine_vo):
        medicine_vo_list = MedicineVO.query.get(medicine_vo.medicine_id)
        db.session.delete(medicine_vo_list)
        db.session.commit()

    def edit_medicine(self, medicine_vo):
        medicine_vo_list = MedicineVO.query.filter_by(medicine_id=medicine_vo.medicine_id).all()
        return medicine_vo_list

    def update_medicine(self, medicine_vo):
        db.session.merge(medicine_vo)
        db.session.commit()
