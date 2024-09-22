from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from config import Config
from models import Member
from bson.objectid import ObjectId

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)
members = mongo.db.members

@app.route('/')
def index():
    all_members = members.find()
    return render_template('index.html', members=all_members)

@app.route('/member/<id>')
def member_details(id):
    member = members.find_one({"_id": ObjectId(id)})
    return render_template('member_details.html', member=member)

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        new_member = Member(
            name=request.form['name'],
            age=request.form['age'],
            membership_type=request.form['membership_type'],
            start_date=request.form['start_date']
        )
        members.insert_one(new_member.to_dict())
        return redirect(url_for('index'))
    return render_template('add_member.html')

@app.route('/edit_member/<id>', methods=['GET', 'POST'])
def edit_member(id):
    member = members.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        updated_member = {
            "name": request.form['name'],
            "age": request.form['age'],
            "membership_type": request.form['membership_type'],
            "start_date": request.form['start_date']
        }
        members.update_one({"_id": ObjectId(id)}, {"$set": updated_member})
        return redirect(url_for('index'))
    return render_template('edit_member.html', member=member)

@app.route('/delete_member/<id>', methods=['POST'])
def delete_member(id):
    members.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


