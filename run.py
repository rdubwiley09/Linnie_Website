from flask import Flask
from views.views import application

if __name__ == "__main__":
	application.run(host='0.0.0.0')
