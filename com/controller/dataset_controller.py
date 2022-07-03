import datetime
import os

from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.dataset_dao import DatasetDAO
from base.com.dao.disease_dao import DiseaseDAO
from base.com.vo.dataset_vo import DatasetVO

DATASET_FOLDER = 'base/static/adminResources/dataset/'
app.config['DATASET_FOLDER'] = DATASET_FOLDER


@app.route("/admin/load_dataset", methods=['GET'])
def admin_load_dataset():
    try:
        if admin_login_session() == "admin":
            disease_dao = DiseaseDAO()
            disease_vo_list = disease_dao.view_disease()
            return render_template("admin/addDataset.html", disease_vo_list=disease_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_load_dataset route exception occured>>>>>>>>>>", ex)


@app.route("/admin/insert_dataset", methods=['POST'])
def admin_insert_dataset():
    try:
        if admin_login_session() == "admin":
            dataset_dao = DatasetDAO()
            dataset_vo = DatasetVO()
            dataset_disease_id = request.form.get("datasetDiseaseId")
            dataset_image = request.files.get("datasetImage")
            dataset_description = request.form.get("datasetDescription")
            dataset_imagename = secure_filename(dataset_image.filename)
            dataset_imagepath = os.path.join(app.config['DATASET_FOLDER'])
            dataset_image.save(os.path.join(dataset_imagepath, dataset_imagename))

            dataset_vo.dataset_description = dataset_description
            dataset_vo.dataset_disease_id = dataset_disease_id
            dataset_vo.dataset_imagename = dataset_imagename
            dataset_vo.dataset_imagepath = dataset_imagepath.replace("base", "..")
            date = str(datetime.datetime.now())

            dataset_vo.dataset_datetime = date

            dataset_dao.insert_dataset(dataset_vo)
            return redirect(url_for('admin_view_dataset'))
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_insert_dataset route exception occured>>>>>>>>>>", ex)


@app.route("/admin/view_dataset", methods=['GET'])
def admin_view_dataset():
    try:
        if admin_login_session() == "admin":
            dataset_dao = DatasetDAO()
            dataset_vo_list = dataset_dao.view_dataset()
            print(">>>>>>>>>>>>>", dataset_vo_list)
            return render_template("admin/viewDataset.html", dataset_vo_list=dataset_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_view_dataset route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_dataset', methods=['GET'])
def admin_delete_dataset():
    try:
        if admin_login_session() == "admin":
            dataset_dao = DatasetDAO()
            dataset_id = request.args.get('datasetId')
            dataset_vo = DatasetVO()
            dataset_vo.dataset_id = dataset_id
            dataset_vo_list = dataset_dao.delete_dataset(dataset_vo)
            imagepath = dataset_vo_list.dataset_imagepath.replace("..", "base") + dataset_vo_list.dataset_imagename
            os.remove(imagepath)
            return redirect(url_for('admin_view_dataset'))
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_delete_dataset route exception occured>>>>>>>>>>", ex)
