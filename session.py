import os
import glob
import json
from itertools import cycle


class Session(object):
    def __init__(self, session_id):
        self. _session_iterator = None
        self._session_id = session_id
        self._relative_path = 'sessions/{0}'.format(session_id)
        if not os.path.exists(self._relative_path):
            os.makedirs(self._relative_path)

        self._img_count = 0

    @property
    def session_id(self):
        return self._session_id

    @property
    def session_path(self):
        return self._relative_path

    def generate_file_name(self):
        """
        Generate the next filename (full path) to be used in capture
        """
        self._session_iterator = None  # New file invalidate old interator
        self._img_count += 1
        return '{0}/frame_{1}.jpg'.format(self._relative_path,self._img_count)

    def reset_counter(self):
        print "reset_counter"
        self._session_iterator = None
        self._img_count = 0

    def get_img_iterator(self):
        if self._session_iterator is None:
            files = glob.glob(self._relative_path + '/*.jpg')
            if len(files) > 0:
                files.sort()
                self._session_iterator = cycle(files)

        return self._session_iterator


