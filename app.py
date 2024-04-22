from flask import Flask , render_template
app = Flask(__name__)
job = [
    {
    "id":"1",
    "position":"Data analayst",
    "salary":"$2,05,000",
    "location":"banglore,india"
  },
     {
    "id":"2",
    "position":"Data scienctist",
    "salary":"$10,05,000",
    "location":"pune,india"
  },
     {
    "id":"3",
   "position":"mining engineer",
    "salary":"$1,05,000",
    "location":"chennai,india"
  }]
@app.route("/")
def first():
    return render_template('home.html',jobs=job)
if __name__ == '__main__':
    app.run(debug=True,port=8000)                  #we can change port also port = 8000 and host also host = :"0.0.0.0"