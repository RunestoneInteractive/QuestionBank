.. mchoice:: flask-mc-3
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :correct: d
   :answer_a: Hello Root!
   :answer_b: Hello Index!
   :answer_c: Hello Barb
   :answer_d: Test Barb
   :feedback_a: This would be true if it was http://127.0.0.1:5000/
   :feedback_b: This would be true if it was http://127.0.0.1:5000/index.html
   :feedback_c: This would be true if it was http://127.0.0.1:5000/user/Barb
   :feedback_d: This is what happens when the request is for http://127.0.0.1:5000/test/Barb
   :pct_on_first: 0.3555555556
   :total_students_attempting: 90
   :num_students_correct: 90.0
   :mean_clicks_to_correct: 2.1333333333

   What will http://127.0.0.1:5000/test/Barb display?
   
   ::
   
       @app.route('/')
       def root():
           return '<h1>Hello Root!</h1>'
   
       @app.route('/index.html')
       def index():
           return '<h1>Hello Index!</h1>
   
       @app.route('/user/<name>')
       def user(name):
           return '<h1>Hello %s</h1>' % name
   
       @app.route('/test/<value>')
       def test(value):
           return '<h1>Test %s</h1>' % value