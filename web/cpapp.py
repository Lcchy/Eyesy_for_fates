import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))
import time
import glob
import json
import cherrypy
import urllib
import liblo
import time
import socket
from os import listdir
from os.path import isfile, join
import imp
import sys
import subprocess

def run_cmd(cmd) :
    ret = False
    try:
        ret = subprocess.check_output(['bash', '-c', cmd], close_fds=True)
    except: pass
    return ret

reload(sys)
sys.setdefaultencoding('utf-8')

current_dir = os.path.dirname(os.path.abspath(__file__))

file_operations = imp.load_source('file_operations', current_dir + '/file_operations.py')


GRABS_PATH = "/home/we/sidekick/patches/Eyesy/presets/Grabs/"

try:
	osc_target = liblo.Address(4000)
except liblo.AddressError as err:
	print(err)
	sys.exit()

def get_immediate_subdirectories(dir) :
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

class Root():

    # loads a file
    def get_file(self, fpath):
        mode = open(file_operations.BASE_DIR + fpath, 'r').read()
        #liblo.send(osc_target, "/set", p)
        return mode
    get_file.exposed = True

    def start_video_engine(self, engine):
        # stop them both
        os.system("sudo systemctl stop eyesy-oflua.service")
        os.system("sudo systemctl stop eyesy-python.service")
        if engine == 'oflua' :
            os.system("sudo systemctl start eyesy-oflua.service")
            return 'started oflua'
        elif engine == 'python' :
            os.system("sudo systemctl start eyesy-python.service")
            return 'started python'
        else :
            return 'no video engine specified'
    start_video_engine.exposed = True

    def stop_video_engine(self, engine):
        # stop them both
        os.system("sudo systemctl stop eyesy-oflua.service")
        os.system("sudo systemctl stop eyesy-python.service")
    stop_video_engine.exposed = True

    def save_new(self, name, contents):
        pass
    save_new.exposed = True

    def reload_mode(self, name):
        liblo.send(osc_target, "/reload", 1)
        return "reloaded mode"
    reload_mode.exposed = True

    def save(self, fpath, contents):
        with open(file_operations.BASE_DIR + fpath, "w") as text_file:
            text_file.write(contents)
        print contents
        return "SAVED " + fpath
    save.exposed = True

    def get_grabs(self):
        images = []
        for filepath in sorted(glob.glob(GRABS_PATH+'*.jpg')):
            filename = os.path.basename(filepath)
            images.append(filename)
        return json.dumps(images)
    get_grabs.exposed = True

    def get_grab(self, name):
        grab_path = GRABS_PATH+name
        grab = open(grab_path, 'r').read()
        cherrypy.response.headers['Content-Type'] = "image/jpg"
        return grab
    get_grab.exposed = True

    def tester(self, name):
        return "TESTdf"
        print "cool"
    tester.exposed = True

    def media(self, fpath, cb):
        cherrypy.response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
        cherrypy.response.headers['Pragma'] = "no-cache"
        cherrypy.response.headers['Expires'] = "0"
        src = file_operations.BASE_DIR + fpath
        return static.serve_file(src)
    media.exposed = True

    def download(self, fpath, cb):
        src = file_operations.BASE_DIR + fpath
        dl = open(src, 'r').read()
        fname = os.path.basename(fpath)
        fname = urllib.quote(fname)
        cherrypy.response.headers['content-type']        = 'application/octet-stream'
        cherrypy.response.headers['content-disposition'] = 'attachment; filename={}'.format(fname)
        return dl
    download.exposed = True

    @cherrypy.config(**{'response.timeout': 3600}) # for large file
    def upload(self, dst, **fdata):
        upload = fdata['files[]']
        folder = dst
        filename = upload.filename
        size = 0
        filepath = file_operations.BASE_DIR + folder + '/' + filename
        filepath = file_operations.check_and_inc_name(filepath)
        with open(filepath, 'wb') as newfile:
            while True:
                data = upload.file.read(8192)
                if not data:
                    break
                size += len(data)
                newfile.write(data)
        print "saved file, size: " + str(size)
        p, ext = os.path.splitext(filepath)
        cherrypy.response.headers['Content-Type'] = "application/json"
        return '{"files":[{"name":"x","size":'+str(size)+',"url":"na","thumbnailUrl":"na","deleteUrl":"na","deleteType":"DELETE"}]}'

    upload.exposed = True

    def fmdata(self, **data):
        print "data op request"
        ret = ''
        if 'operation' in data :
            cherrypy.response.headers['Content-Type'] = "application/json"
            if data['operation'] == 'get_node' :
                return file_operations.get_node(data['path'])
            if data['operation'] == 'create_node' :
                return file_operations.create(data['path'], data['name'])
            if data['operation'] == 'create_file' :
                return file_operations.create_file(data['path'], data['name'])
            if data['operation'] == 'rename_node' :
                return file_operations.rename(data['path'], data['name'])
            if data['operation'] == 'delete_node' :
                return file_operations.delete(data['path'])
            if data['operation'] == 'move_node' :
                return file_operations.move(data['src'], data['dst'])
            if data['operation'] == 'copy_node' :
                return file_operations.copy(data['src'], data['dst'])
            if data['operation'] == 'unzip_node' :
                return file_operations.unzip(data['path'])
            if data['operation'] == 'download_node' :
                return file_operations.download(data['path'])
            if data['operation'] == 'zip_node' :
                return file_operations.zip(data['path'])
        else :
            cherrypy.response.headers['Content-Type'] = "application/json"
            return "no operation specified"

    fmdata.exposed = True




