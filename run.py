import os
from project import app

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

def setUp(self):
	app.config['TESTING'] = True
	app.config['WTF_CSRF_ENABLED'] = False
	app.config['DEBUG'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
	self.app = app.test_client()
	db.create_all()

	self.assertEquals(app.debug, False)

