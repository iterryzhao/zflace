#!/user/bin/python
from app import app
#app.run(debug = True, host="0.0.0.0", port=80)
#app.run()
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)