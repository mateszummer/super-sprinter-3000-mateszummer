from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)

def write_or_append_csv(mode, lst):
    with open("save.csv", mode) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(lst)
def read_csv():
    lst = []
    with open("save.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lst.append(row)
    return lst

@app.route('/')
def route_index():
    return render_template('index.html')
@app.route('/edit-note')
def route_edit():
    return render_template('edit.html')
@app.route('/save-note', methods=['POST'])
def route_save():
    lst = []
    lst.append(request.form['storytitles'])
    lst.append(request.form['userstory'])
    lst.append(request.form['acceptance'])
    write_or_append_csv("a", lst)
    return redirect('/')
@app.route("/update/1", methods=["POST"])
def route_update_1():
    lst = read_csv()
    temporary_lst = []
    temporary_lst.append(request.form['storytitles'])
    temporary_lst.append(request.form['userstory'])
    temporary_lst.append(request.form['acceptance'])
    lst[0] = temporary_lst
    write_or_append_csv("w",lst[0])
    for i in range(1,(len(lst))):
        write_or_append_csv("a", lst[i])
    return redirect('/')
@app.route("/update/2", methods=["POST"])
def route_update_2():
    lst = read_csv()
    temporary_lst = []
    temporary_lst.append(request.form['storytitles'])
    temporary_lst.append(request.form['userstory'])
    temporary_lst.append(request.form['acceptance'])
    lst[1] = temporary_lst
    write_or_append_csv("w",lst[0])
    for i in range(1,(len(lst))):
        write_or_append_csv("a", lst[i])
    return redirect('/')
@app.route("/reach/1")
def route_reach_1():
    lst = read_csv()
    return render_template("reach.html", note = lst[0], page="/update/1")
@app.route("/reach/2")
def route_reach_2():
    lst = read_csv()
    return render_template("reach.html", note = lst[1], page="/update/2")

if __name__ == "__main__":
    app.secret_key = 'Scrublord123'
    app.run(
        debug=True, # Allow verbose error reports
        port=5006 # Set custom port
    )
