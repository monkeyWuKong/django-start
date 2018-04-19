import logging
import os

#get project name, here is mysite.
projectPath = os.getcwd().split('/')[-1]
log = logging.getLogger(projectPath + '.' + __name__)