from flask import Flask, render_template, jsonify
from connect_mysql import get_connection

app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        # 'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    },
]

def get_jobs_data():
    conn = get_connection() # adjust DB path
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()

    # Convert rows to list of dicts
    jobs = []
    for row in rows:
        job = {}
        for col_name, value in zip(columns, row):
            job[col_name] = value
        jobs.append(job)

    return jobs

@app.route("/")
def hello_world():
    jobs = get_jobs_data()
    return render_template('home.html',jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    jobs = get_jobs_data()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    jobs = get_jobs_data()
    job = next((job for job in jobs if str(job['id']) == str(id)), None)
    if job:
        return render_template('jobpage.html', job = job)
    else:
        return "Not found", 404

if __name__ == "__main__":
  app.run(debug=True)
