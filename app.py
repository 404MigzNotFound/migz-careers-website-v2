from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Manila, Philippines',
  'salary': 'P1,000,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'QC, Philippines',
  'salary': 'P2,000,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  'salary': 'P3,000,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Antips, Philippines',
  'salary': 'P5,000,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Migz')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
