from flask import request, render_template, redirect

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.crop_dao import CropDAO
from base.com.vo.crop_vo import CropVO


@app.route('/admin/load_crop', methods=['GET'])
def admin_load_crop():
    try:
        if admin_login_session() == "admin":
            return render_template('admin/addCrop.html')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_load_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_crop', methods=['POST'])
def admin_insert_crop():
    try:
        if admin_login_session() == "admin":
            crop_name = request.form.get('cropName')
            crop_description = request.form.get('cropDescription')

            crop_vo = CropVO()
            crop_dao = CropDAO()

            crop_vo.crop_name = crop_name
            crop_vo.crop_description = crop_description
            crop_dao.insert_crop(crop_vo)
            return redirect('/admin/view_crop')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_insert_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_crop', methods=['GET'])
def admin_view_crop():
    try:
        if admin_login_session() == "admin":
            crop_dao = CropDAO()
            crop_vo_list = crop_dao.view_crop()
            print("in admin_view_crop crop_vo_list >>>>>>>>>>>>>>", crop_vo_list)
            return render_template('admin/viewCrop.html', crop_vo_list=crop_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_crop', methods=['GET'])
def admin_delete_crop():
    try:
        if admin_login_session() == "admin":
            crop_vo = CropVO()
            crop_dao = CropDAO()

            crop_id = request.args.get('cropId')
            crop_vo.crop_id = crop_id
            crop_dao.delete_crop(crop_vo)
            return redirect('/admin/view_crop')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_delete_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_crop', methods=['GET'])
def admin_edit_crop():
    try:
        if admin_login_session() == "admin":
            crop_vo = CropVO()
            crop_dao = CropDAO()

            crop_id = request.args.get('cropId')
            print(">>>>>>>>>>>>>", crop_id)
            crop_vo.crop_id = crop_id
            crop_vo_list = crop_dao.edit_crop(crop_vo)

            return render_template('admin/editCrop.html', crop_vo_list=crop_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_edit_crop route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_crop', methods=['POST'])
def admin_update_crop():
    try:
        if admin_login_session() == "admin":
            crop_id = request.form.get('cropId')
            crop_name = request.form.get('cropName')
            crop_description = request.form.get('cropDescription')

            crop_vo = CropVO()
            crop_dao = CropDAO()

            crop_vo.crop_id = crop_id
            crop_vo.crop_name = crop_name
            crop_vo.crop_description = crop_description
            crop_dao.update_crop(crop_vo)
            return redirect('/admin/view_crop')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_update_crop route exception occured>>>>>>>>>>", ex)
