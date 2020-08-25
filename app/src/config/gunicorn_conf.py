import os

bind = '0.0.0.0:' + str(os.getenv('PORT', 5000))
accesslog = '-'
timeout = 120