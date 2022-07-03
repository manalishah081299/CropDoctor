import datetime
import os

from flask import render_template, redirect, request, url_for
from werkzeug.utils import secure_filename

from base import app
from base.com.controller.load_inference import load_classification
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.classification_dao import ClassificationDAO
from base.com.dao.crop_dao import CropDAO
from base.com.dao.disease_dao import DiseaseDAO
from base.com.dao.login_dao import LoginDAO
from base.com.vo.classification_vo import ClassificationVO
from base.com.vo.disease_vo import DiseaseVO
from base.com.vo.login_vo import LoginVO

INPUT_IMAGE_FOLDER = 'base/static/adminResources/input_image/'
app.config['INPUT_IMAGE_FOLDER'] = INPUT_IMAGE_FOLDER


@app.route('/user/load_classification')
def user_load_classification():
    try:
        if admin_login_session() == "user":
            crop_dao = CropDAO()
            crop_vo_list = crop_dao.view_crop()
            return render_template('user/addClassification.html', crop_vo_list=crop_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("add classification route exception occured>>>>>>>>>>", ex)


@app.route("/user/insert_classification", methods=['POST'])
def user_insert_classification():
    try:
        if admin_login_session() == "user":
            classification_dao = ClassificationDAO()
            classification_vo = ClassificationVO()
            disease_dao = DiseaseDAO()
            disease_vo = DiseaseVO()
            login_vo = LoginVO()
            login_dao = LoginDAO()
            classification_crop_id = request.form.get("classificationCropId")
            classification_image = request.files.get("classificationImage")
            classification_imagename = secure_filename(classification_image.filename)
            classification_imagepath = os.path.join(app.config['INPUT_IMAGE_FOLDER'])
            classification_image.save(os.path.join(classification_imagepath, classification_imagename))
            input_file = classification_imagepath + classification_imagename
            classification_status = load_classification(input_file)
            print("classification_status=", classification_status)
            disease_vo.disease_name = classification_status
            disease_id = disease_dao.find_disease_id(disease_vo)
            classification_vo.classification_disease_id = disease_id
            classification_vo.classification_crop_id = classification_crop_id
            login_username = request.cookies.get('login_username')
            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)
            classification_vo.classification_login_id = login_id
            classification_vo.classification_status = classification_status
            classification_vo.classification_imagename = classification_imagename
            classification_vo.classification_imagepath = classification_imagepath.replace("base", "..")
            classification_datetime = datetime.datetime.now()
            classification_vo.classification_datetime = classification_datetime
            classification_dao.insert_classification(classification_vo)
            return redirect(url_for('user_view_classification'))

        else:
            return admin_logout_session()
    except Exception as ex:
        print("insert classification route exception occured>>>>>>>>>>", ex)


@app.route('/user/view_classification')
def user_view_classification():
    try:
        if admin_login_session() == "user":
            classification_dao = ClassificationDAO()
            classification_vo = ClassificationVO()
            login_vo = LoginVO()
            login_dao = LoginDAO()
            login_username = request.cookies.get('login_username')
            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)
            classification_vo.classification_login_id = login_id
            classification_vo_list = classification_dao.view_classification(classification_vo)
            print(">>>>>>>>>>>>>", classification_vo_list)
            return render_template('user/viewClassification.html', classification_vo_list=classification_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("view classification route exception occured>>>>>>>>>>", ex)
