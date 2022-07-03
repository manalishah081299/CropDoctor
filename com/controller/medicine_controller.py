from flask import request, render_template, redirect, url_for

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.crop_dao import CropDAO
from base.com.dao.disease_dao import DiseaseDAO
from base.com.dao.medicine_dao import MedicineDAO
from base.com.vo.medicine_vo import MedicineVO


@app.route('/admin/load_medicine', methods=['GET'])
def admin_load_medicine():
    try:
        if admin_login_session() == "admin":
            crop_dao = CropDAO()
            crop_vo_list = crop_dao.view_crop()
            disease_dao = DiseaseDAO()
            disease_vo_list = disease_dao.view_disease()
            print(">>>>>>>>", disease_vo_list)
            return render_template('admin/addMedicine.html', crop_vo_list=crop_vo_list, disease_vo_list=disease_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_load_medicine route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_medicine', methods=['POST'])
def admin_insert_medicine():
    try:
        if admin_login_session() == "admin":
            medicine_name = request.form.get('medicineName')
            medicine_crop_id = request.form.get('medicineCropId')
            medicine_disease_id = request.form.get('medicineDiseaseId')

            medicine_vo = MedicineVO()
            medicine_dao = MedicineDAO()

            medicine_vo.medicine_name = medicine_name
            medicine_vo.medicine_crop_id = medicine_crop_id
            medicine_vo.medicine_disease_id = medicine_disease_id
            medicine_dao.insert_medicine(medicine_vo)
            return redirect(url_for('admin_view_medicine'))
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_insert_medicine route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_medicine', methods=['GET'])
def admin_view_medicine():
    try:
        if admin_login_session() == "admin":
            medicine_dao = MedicineDAO()
            medicine_vo_list = medicine_dao.view_medicine()
            print("medicine_vo_list>>>>>>>>>>", medicine_vo_list)
            return render_template('admin/viewMedicine.html', medicine_vo_list=medicine_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_view_medicine route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_medicine', methods=['GET'])
def admin_delete_medicine():
    try:
        if admin_login_session() == "admin":
            medicine_vo = MedicineVO()
            medicine_dao = MedicineDAO()

            medicine_id = request.args.get('medicineId')
            print(">>>>>>>>>>>>>>", medicine_id)
            medicine_vo.medicine_id = medicine_id
            medicine_dao.delete_medicine(medicine_vo)
            return redirect('/admin/view_medicine')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_delete_medicine route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_medicine', methods=['GET'])
def admin_edit_medicine():
    try:
        if admin_login_session() == "admin":
            medicine_vo = MedicineVO()
            medicine_dao = MedicineDAO()
            crop_dao = CropDAO()
            disease_dao = DiseaseDAO()

            medicine_id = request.args.get('medicineId')
            print(">>>>>>>>>>>>>", medicine_id)
            medicine_vo.medicine_id = medicine_id
            medicine_vo_list = medicine_dao.edit_medicine(medicine_vo)
            crop_vo_list = crop_dao.view_crop()
            disease_vo_list = disease_dao.view_disease()
            return render_template('admin/editMedicine.html', medicine_vo_list=medicine_vo_list,
                                   disease_vo_list=disease_vo_list,
                                   crop_vo_list=crop_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_edit_medicine route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_medicine', methods=['POST'])
def admin_update_medicine():
    try:
        if admin_login_session() == "admin":
            medicine_id = request.form.get('medicineId')
            medicine_name = request.form.get('medicineName')
            medicine_disease_id = request.form.get('medicineDiseaseId')
            medicine_crop_id = request.form.get('medicineCropId')

            medicine_vo = MedicineVO()
            medicine_dao = MedicineDAO()

            medicine_vo.medicine_id = medicine_id
            medicine_vo.medicine_name = medicine_name
            medicine_vo.medicine_crop_id = medicine_crop_id
            medicine_vo.medicine_disease_id = medicine_disease_id
            medicine_dao.update_medicine(medicine_vo)
            return redirect('/admin/view_medicine')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_update_medicine route exception occured>>>>>>>>>>", ex)
