from flask import Flask, render_template, redirect, request, session
import csv
import os

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
    lst = len(read_csv())
    lst_real= read_csv()
    return render_template('index.html', lst=lst, lst_real=lst_real)
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
@app.route("/update/<int:post_id>", methods=["POST"])
def route_update_1(post_id):
    lst = read_csv()
    temporary_lst = []
    temporary_lst.append(request.form['storytitles'])
    temporary_lst.append(request.form['userstory'])
    temporary_lst.append(request.form['acceptance'])
    lst[post_id-1] = temporary_lst
    write_or_append_csv("w",lst[0])
    for i in range(1,(len(lst))):
        write_or_append_csv("a", lst[i])
    return redirect('/')
@app.route("/delete/<int:post_id>")
def route_delete(post_id):
    lst = read_csv()
    if len(lst)==1:
        lst = None
        filename = "save.csv"
        f = open(filename, "w+")
        f.close()
    else:
        lst.pop(post_id-1)
        write_or_append_csv("w",lst[0])
        for i in range(1,(len(lst))):
            write_or_append_csv("a", lst[i])
    return redirect('/')

@app.route("/reach/<int:post_id>")
def route_reach_1(post_id):
    lst = read_csv()
    return render_template("reach.html", note = lst[post_id-1], page="/update/%d"%post_id)
@app.route("/list")
def get_list():
    lst = read_csv()
    return render_template("list.html", lst=lst)

if __name__ == "__main__":
    app.secret_key = 'Scrublord123'
    app.run(
        debug=True, # Allow verbose error reports
        port=5006 # Set custom port
    )
