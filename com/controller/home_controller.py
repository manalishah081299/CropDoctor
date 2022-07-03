from flask import render_template

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session


# @app.route('/', methods=['GET'])
# def admin_load_dashboard():
#     try:
#         if admin_login_session() == "admin":
#             return render_template('admin/index.html')
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("home page route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_user', methods=['GET'])
def admin_view_User():
    try:
        if admin_login_session() == "admin":
            return render_template('admin/viewUser.html')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("viewUser route exception occured>>>>>>>>>>", ex)

# @app.route('/admin/insert_disease', methods=['GET'])
# def admin_load_addDisease():
#    try:
#        return render_template('admin/addDisease.html')
#    except Exception as ex:
#        print("addDisease route exception occured>>>>>>>>>>", ex)


# @app.route('/admin/view_disease', methods=['GET'])
# def admin_load_viewDisease():
#      try:
#        return render_template('admin/viewDisease.html')
#    except Exception as ex:
#        print("viewDisease route exception occured>>>>>>>>>>", ex)


# @app.route('/admin/insert_medicine', methods=['GET'])
# def admin_load_addMedicine():
#    try:
#        return render_template('admin/addMedicine.html')
#    except Exception as ex:
#        print("addMedicine route exception occured>>>>>>>>>>", ex)


# @app.route('/admin/view_medicine', methods=['GET'])
# def admin_load_viewMedicine():
#    try:
#        return render_template('admin/viewMedicine.html')
#    except Exception as ex:
#        print("viewMedicine route exception occured>>>>>>>>>>", ex)


# @app.route('/admin/insert_dataset', methods=['GET'])
# def admin_load_addDataset():
#     try:
#         return render_template('admin/addDataset.html')
#     except Exception as ex:
#         print("addDataset route exception occured>>>>>>>>>>", ex)
#
#
# @app.route('/admin/view_dataset', methods=['GET'])
# def admin_load_viewDataset():
#     try:
#         return render_template('admin/viewDataset.html')
#     except Exception as ex:
#         print("viewDataset route exception occured>>>>>>>>>>", ex)
#

# @app.route('/admin/view_complain', methods=['GET'])
# def admin_view_complain():
#     try:
#         if admin_login_session() == "admin":
#             return render_template('admin/viewComplain.html')
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("viewComplain route exception occured>>>>>>>>>>", ex)
#

# @app.route('/admin/load_complain_reply', methods=['GET'])
# def admin_load_addcomplainreply():
#     try:
#         if admin_login_session() == "admin":
#             return render_template('admin/addComplainReply.html')
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("add complain route exception occured>>>>>>>>>>", ex)


# @app.route('/admin/view_feedback', methods=['GET'])
# def admin_view_feedback():
#     try:
#         if admin_login_session() == "admin":
#             return render_template('admin/viewFeedback.html')
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("viewFeedback route exception occured>>>>>>>>>>", ex)

# @app.route("/user/load_dashboard")
# def user_view_user():
#     return render_template("user/index.html")

# @app.route('/user/add_image')
# def user_insert_image():
#     try:
#         if admin_login_session() == "user":
#             return render_template('user/addClassification.html')
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("add Image route exception occured>>>>>>>>>>", ex)
#
#
# @app.route('/user/view_image')
# def user_view_image():
#     try:
#         if admin_login_session() == "user":
#             return render_template('user/viewClassification.html')
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("view Image route exception occured>>>>>>>>>>", ex)

# @app.route('/user/add_feedback')
# def user_add_feedback():
#     try:
#         if admin_login_session() == "user":
#             return render_template('user/addFeedback.html')
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("add Feedback route exception occured>>>>>>>>>>", ex)
#
# @app.route('/user/add_complain')
# def user_add_complain():
#     try:
#         if admin_login_session() == "user":
#             return render_template('user/addComplain.html')
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("add Complain route exception occured>>>>>>>>>>", ex)


# @app.route('/admin/login', methods=['GET'])
# def admin_load_login():
#     try:
#         if admin_login_session() == "admin":
#             return render_template('admin/login.html')
#         else:
#             return admin_logout_session()
#     except Exception as ex:
#         print("login route exception occured>>>>>>>>>>", ex)
