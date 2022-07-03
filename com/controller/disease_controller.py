from flask import request, render_template, redirect, url_for

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.crop_dao import CropDAO
from base.com.dao.disease_dao import DiseaseDAO
from base.com.vo.disease_vo import DiseaseVO


@app.route('/admin/load_disease', methods=['GET'])
def admin_load_disease():
    try:
        if admin_login_session() == "admin":
            crop_dao = CropDAO()
            crop_vo_list = crop_dao.view_crop()
            return render_template('admin/addDisease.html', crop_vo_list=crop_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_load_disease route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_disease', methods=['POST'])
def admin_insert_disease():
    try:
        if admin_login_session() == "admin":
            disease_name = request.form.get('diseaseName')
            disease_description = request.form.get('diseaseDescription')
            disease_crop_id = request.form.get('diseaseCropId')

            disease_vo = DiseaseVO()
            disease_dao = DiseaseDAO()

            disease_vo.disease_name = disease_name
            disease_vo.disease_description = disease_description
            disease_vo.disease_crop_id = disease_crop_id
            disease_dao.insert_disease(disease_vo)
            return redirect(url_for('admin_view_disease'))
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_insert_disease route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_disease', methods=['GET'])
def admin_view_disease():
    try:
        if admin_login_session() == "admin":
            disease_dao = DiseaseDAO()
            disease_vo_list = disease_dao.view_disease()
            print("disease_vo_list>>>>>>>>>>", disease_vo_list)
            return render_template('admin/viewDisease.html', disease_vo_list=disease_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_view_disease route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_disease', methods=['GET'])
def admin_delete_disease():
    try:
        if admin_login_session() == "admin":
            disease_vo = DiseaseVO()
            disease_dao = DiseaseDAO()

            disease_id = request.args.get('diseaseId')
            print(">>>>>>>>>>>>>>", disease_id)
            disease_vo.disease_id = disease_id
            disease_dao.delete_disease(disease_vo)
            return redirect('/admin/view_disease')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_delete_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_disease', methods=['GET'])
def admin_edit_disease():
    try:
        if admin_login_session() == "admin":
            disease_vo = DiseaseVO()
            disease_dao = DiseaseDAO()
            crop_dao = CropDAO()

            disease_id = request.args.get('diseaseId')
            print(">>>>>>>>>>>>>", disease_id)
            disease_vo.disease_id = disease_id
            disease_vo_list = disease_dao.edit_disease(disease_vo)
            crop_vo_list = crop_dao.view_crop()

            return render_template('admin/editDisease.html', disease_vo_list=disease_vo_list,
                                   crop_vo_list=crop_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_edit_disease route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_disease', methods=['POST'])
def admin_update_disease():
    try:
        if admin_login_session() == "admin":
            disease_id = request.form.get('diseaseId')
            disease_name = request.form.get('diseaseName')
            disease_description = request.form.get('diseaseDescription')
            disease_crop_id = request.form.get('diseaseCropId')

            disease_vo = DiseaseVO()
            disease_dao = DiseaseDAO()

            disease_vo.disease_id = disease_id
            disease_vo.disease_name = disease_name
            disease_vo.disease_description = disease_description
            disease_vo.disease_crop_id = disease_crop_id
            disease_dao.update_disease(disease_vo)
            return redirect('/admin/view_disease')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_update_disease route exception occured>>>>>>>>>>", ex)
