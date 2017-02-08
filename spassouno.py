# coding=utf-8

# Progetto: SpassoUno

import time
import shutil
import logging
import os

from camera_manager import Camera
from session_manager import SessionManager
from utility import init_key_read, restore_key_read, read_key, find_usb_path
from periodic_thread import PeriodicThread

__version__ = '0.1'
__author__ = 'Fabrizio Guglielmino'


class Keys(object):
    UP_KEY = '\x1b[A'  # Decelerate preview
    DOWN_KEY = '\x1b[B'  # Accelerate preview
    SPACE_KEY = ' '  # Take a snapshot
    X_KEY = 'x'  # Delete a frame
    M_KEY = 'm'  # Make video
    G_KEY = 'g'  # Make animated GIF
    Q_KEY = 'q'  # Quit
    D_KEY = 'd'  # Delete session (new session)
    F_KEY = 'f'  # Toggle fullscreen
    PLUS_KEY = '+'  # Zoom preview in
    MIN_KEY = '-'  # Zoom preview out


class SpassoUno(object):
    _camera = None
    _session_manager = None
    _periodic_thread = None
    _is_running = False
    _frame_delay = 0.5
    DELAY_INCR_STEP = 0.05
    INCR_MUL = 100
    _functions = {}

    def __init__(self, session_manager, camera, periodic_thread):
        try:
            self._old_settings = init_key_read()
        except:
            logging.error("init_key_read failed")
            pass

        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename='app.log', level=logging.INFO)

        self.__map_key_methods()

        self._periodic_thread = periodic_thread
        self._periodic_thread.callback = self.__show_next_frame
        self._periodic_thread.start()

        self._session_manager = session_manager
        self._camera = camera

        self._camera.start_preview()

    def cleanup(self):
        restore_key_read(self._old_settings)
        self._periodic_thread.cancel()

        if self._camera:
            self._camera.stop_preview()
            self._camera.close()

    def run(self):
        self._is_running = True
        while self._is_running:
            self.__process_input()
            time.sleep(0.05)

    def __map_key_methods(self):
        self._functions[Keys.SPACE_KEY] = self.__capture_frame
        self._functions[Keys.X_KEY] = self.__delete_last_frame
        self._functions[Keys.M_KEY] = self.__make_video
        self._functions[Keys.G_KEY] = self.__make_animated_GIF
        self._functions[Keys.UP_KEY] = self.__inc_prev_speed
        self._functions[Keys.DOWN_KEY] = self.__dec_prev_speed
        self._functions[Keys.D_KEY] = self.__delete_cur_session
        self._functions[Keys.F_KEY] = self.__toggle_fullscreen
        self._functions[Keys.PLUS_KEY] = self.__zoom_in
        self._functions[Keys.MIN_KEY] = self.__zoom_out

        self._functions[Keys.Q_KEY] = self.__quit_app

    def __process_input(self):
        key = read_key()

        if key in self._functions:
            self._functions[key]()

    def __quit_app(self):
        self.__delete_cur_session()
        self._is_running = False

    def __capture_frame(self):
        self._camera.annotate_text('')
        filename = self._session_manager \
            .current_session \
            .generate_file_name()

        self._camera.capture_to_file(filename)

    def __inc_prev_speed(self):
        if int(self._frame_delay * self.INCR_MUL) > int(self.DELAY_INCR_STEP * self.INCR_MUL):
            self._frame_delay -= self.DELAY_INCR_STEP

        self._camera.annotate_text('Inc {0}'.format(self._frame_delay))
        self._periodic_thread.change_period(self._frame_delay)

    def __dec_prev_speed(self):
        self._frame_delay += self.DELAY_INCR_STEP

        self._camera.annotate_text('Dec {0}'.format(self._frame_delay))
        self._periodic_thread.change_period(self._frame_delay)

    def __delete_last_frame(self):
        print "deleting {0}".format(self._session_manager.current_session.current_file)
        if self._session_manager.current_session.current_file != '' and \
                os.path.isfile(self._session_manager.current_session.current_file):
            os.unlink(self._session_manager.current_session.current_file)
            self._session_manager.current_session.dec_counter()

    def __make_video(self):
        usb_path=find_usb_path()
        if not usb_path==None:
            #os.system(
            print 'convert -delay 100 {0}/*.jpg {1}/video.mp4'.format(\
                os.getcwd()+"/"+self._session_manager.current_session.session_path,\
                usb_path)
        else:
            print "please Insert USB Drive and Retry"

    def __make_animated_GIF(self):
        usb_path=find_usb_path()
        if not usb_path==None:
            #os.system(
            print 'convert -delay 100 -loop 0 {0}/*.jpg {1}/animation.gif'.format(\
                os.getcwd()+"/"+self._session_manager.current_session.session_path,\
                usb_path)
        else:
            print "please Insert USB Drive and Retry"

    def __toggle_fullscreen(self):
        self._camera.fullscreen = not self._camera.fullscreen

    def __zoom_in(self):
        self._camera.zoom_in()


    def __zoom_out(self):
        self._camera.zoom_out()


    def __delete_cur_session(self):
        self._periodic_thread.cancel()
        shutil.rmtree(self._session_manager.current_session.session_path)
        self._session_manager.reset_cur_session()
        self._periodic_thread.start()


    def __show_frame(self, image_name):
        return self._camera.show_frame(image_name)


    def __show_next_frame(self):
        img_iter = self._session_manager.current_session.get_img_iterator()
        if img_iter:
            img = next(img_iter)
            if img:
                self.__show_frame(img)
        else:
            self.__show_frame('res/logo.jpg')


if __name__ == '__main__':
    spasso1 = SpassoUno(SessionManager(), Camera(), PeriodicThread(period=1.5))
    spasso1.run()
    spasso1.cleanup()
