# -*- coding: utf-8 -*-
__author__ = 'toopazo'

import picamera
import time


class RaspiCamIf():
    __camera = None


    @staticmethod
    def init():
        RaspiCamIf.__camera = picamera.PiCamera()

    @staticmethod
    def take_picture(pathfile):
        RaspiCamIf.__camera.capture(pathfile + ".jpg")
        time.sleep(5)
        # RaspiCamIf.__camera.hflip = True
        # RaspiCamIf.__camera.vflip = True

    @staticmethod
    def stop():
        RaspiCamIf.__camera.close()

    @staticmethod
    def reset_default_values():
        RaspiCamIf.__camera.sharpness = 0
        RaspiCamIf.__camera.contrast = 0
        RaspiCamIf.__camera.brightness = 50
        RaspiCamIf.__camera.saturation = 0
        RaspiCamIf.__camera.ISO = 0
        RaspiCamIf.__camera.video_stabilization = False
        RaspiCamIf.__camera.exposure_compensation = 0
        RaspiCamIf.__camera.exposure_mode = 'auto'
        RaspiCamIf.__camera.meter_mode = 'average'
        RaspiCamIf.__camera.awb_mode = 'auto'
        RaspiCamIf.__camera.image_effect = 'none'
        RaspiCamIf.__camera.color_effects = None
        RaspiCamIf.__camera.rotation = 0
        RaspiCamIf.__camera.hflip = False
        RaspiCamIf.__camera.vflip = False
        RaspiCamIf.__camera.crop = (0.0, 0.0, 1.0, 1.0)