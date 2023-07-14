from flask import Blueprint, render_template

report_views = Blueprint('report',__name__)

@report_views .route("/reports")
def reports ():
    return render_template('reports/reports.html')