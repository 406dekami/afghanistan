from flask import Flask, request

app = Flask(__name__)


@app.route('/process_form', methods=['POST'])
def process_form():
    email = request.form['email']
    # 在这里对表单数据进行处理，例如将其保存到数据库中
    # ...
    return '表单已成功提交'


if __name__ == '__main__':
    app.run(debug=True)
