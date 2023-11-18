from flask import Blueprint, render_template, request, redirect, url_for

ce = Blueprint('ce', __name__, url_prefix='/course_evaluation')


@ce.route('/')
def course_evaluation():
    # 등록되어진 강의 평가 업록드해서 course_evaluation.html 에 보여주기
    # course_evaluation_db 에서 가져오기 나중에 db 만드면
    ce_list = []
    return render_template('course_evaluation.html', ce_list=ce_list)


@ce.route('/search/')
def search():
    ce_list = []
    search_word = request.args.get('course_evaluation_search')
    # 등록되어진 강의 평가에서 search_word 로 내용 필터링한 후 course_evaluation.html 에 보여주기
    # course_evaluation_db 에서 가져오기 나중에 db 만드면
    return render_template('course_evaluation.html', ce_list=ce_list)


@ce.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        course_number = request.form['course_number']
        course_name = request.form['course_name']
        course_coordinate_name = request.form['course_coordinate_name']
        course_review = request.form['course_review']

        print(course_number, course_name, course_coordinate_name, course_review)
        return redirect(url_for('ce.course_evaluation'))
    else:
        return render_template('course_evaluation_add.html')
