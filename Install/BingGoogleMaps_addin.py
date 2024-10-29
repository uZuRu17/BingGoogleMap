import pythonaddins
import arcpy
import webbrowser
import functools
import threading
import time

class BingAerial(object):
    """Implementation for BingGoogleMaps_addin.tool_6 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = "NONE"

    def onMouseDownMap(self, x, y, button, shift):

        mxd = arcpy.mapping.MapDocument("CURRENT")
        view = mxd.activeView

        sr = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
        code = sr.factoryCode

        if view == "PAGE_LAYOUT":
            pythonaddins.MessageBox("This tool will not work in Layout View. Please change to Data View.", "Warning", 0)

        elif code == 0:
            pythonaddins.MessageBox("The current Data Frame coordinate system is not an ESRI standard. \n\nThe coordinate system cannot be custom, or undefined.", "Warning", 0)

        else:
            click = arcpy.Point(x, y)

            mxd = arcpy.mapping.MapDocument("CURRENT")
            sr_old = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
            sr_new = arcpy.SpatialReference(4326)
            click_geom = arcpy.PointGeometry(click, sr_old)
            coords = click_geom.projectAs(sr_new)

            scale = float(mxd.activeDataFrame.scale)

            x_coord = coords.firstPoint.X
            y_coord = coords.firstPoint.Y

            if scale <= 500:
                level = 20
            elif 500 < scale <= 1500:
                level = 19
            elif 1500 < scale <= 3000:
                level = 18
            elif 3000 < scale <= 5000:
                level = 17
            elif 5000 < scale <= 15000:
                level = 16
            elif 15000 < scale <= 24000:
                level = 15
            elif 24000 < scale <= 32000:
                level = 14
            elif 32000 < scale <= 80000:
                level = 13
            elif 80000 < scale <= 200000:
                level = 12
            elif 200000 < scale <= 400000:
                level = 11
            else:
                level = 10

            url = "http://www.bing.com/maps/?v=2&cp={0}~{1}&lvl={2}&sty=h".format(y_coord, x_coord, level)

            def run_in_other_thread(function):
                @functools.wraps(function)
                def fn_(*args, **kwargs):
                    thread = threading.Thread(target=function, args=args, kwargs=kwargs)
                    thread.start()
                    thread.join()
                return fn_

            openbrowser = run_in_other_thread(webbrowser.open)
            openbrowser(url, new=2)

            del click
            del click_geom
            del coords
            del openbrowser

class BingBirdsEye(object):
    """Implementation for BingGoogleMaps_addin.tool_5 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = "NONE"

    def onMouseDownMap(self, x, y, button, shift):

        mxd = arcpy.mapping.MapDocument("CURRENT")
        view = mxd.activeView

        sr = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
        code = sr.factoryCode

        if view == "PAGE_LAYOUT":
            pythonaddins.MessageBox("This tool will not work in Layout View. Please change to Data View.", "Warning", 0)

        elif code == 0:
            pythonaddins.MessageBox("The current Data Frame coordinate system is not an ESRI standard. \n\nThe coordinate system cannot be custom, or undefined.", "Warning", 0)

        else:
            click = arcpy.Point(x, y)

            mxd = arcpy.mapping.MapDocument("CURRENT")
            sr_old = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
            sr_new = arcpy.SpatialReference(4326)
            click_geom = arcpy.PointGeometry(click, sr_old)
            coords = click_geom.projectAs(sr_new)

            scale = float(mxd.activeDataFrame.scale)

            x_coord = coords.firstPoint.X
            y_coord = coords.firstPoint.Y

            if scale <= 500:
                level = 20
            elif 500 < scale <= 1500:
                level = 19
            elif 1500 < scale <= 3000:
                level = 18
            elif 3000 < scale <= 5000:
                level = 17
            elif 5000 < scale <= 15000:
                level = 16
            elif 15000 < scale <= 24000:
                level = 15
            elif 24000 < scale <= 32000:
                level = 14
            elif 32000 < scale <= 80000:
                level = 13
            elif 80000 < scale <= 200000:
                level = 12
            elif 200000 < scale <= 400000:
                level = 11
            else:
                level = 10

            url = "http://www.bing.com/maps/?v=2&cp={0}~{1}&lvl={2}&sty=b".format(y_coord, x_coord, level)

            def run_in_other_thread(function):
                @functools.wraps(function)
                def fn_(*args, **kwargs):
                    thread = threading.Thread(target=function, args=args, kwargs=kwargs)
                    thread.start()
                    thread.join()
                return fn_

            openbrowser = run_in_other_thread(webbrowser.open)
            openbrowser(url, new=2)

            del click
            del click_geom
            del coords
            del openbrowser

class BingRoads(object):
    """Implementation for BingGoogleMaps_addin.tool_4 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = "NONE"

    def onMouseDownMap(self, x, y, button, shift):

        mxd = arcpy.mapping.MapDocument("CURRENT")
        view = mxd.activeView

        sr = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
        code = sr.factoryCode

        if view == "PAGE_LAYOUT":
            pythonaddins.MessageBox("This tool will not work in Layout View. Please change to Data View.", "Warning", 0)

        elif code == 0:
            pythonaddins.MessageBox("The current Data Frame coordinate system is not an ESRI standard. \n\nThe coordinate system cannot be custom, or undefined.", "Warning", 0)

        else:
            click = arcpy.Point(x, y)

            mxd = arcpy.mapping.MapDocument("CURRENT")
            sr_old = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
            sr_new = arcpy.SpatialReference(4326)
            click_geom = arcpy.PointGeometry(click, sr_old)
            coords = click_geom.projectAs(sr_new)

            scale = float(mxd.activeDataFrame.scale)

            x_coord = coords.firstPoint.X
            y_coord = coords.firstPoint.Y

            if scale <= 500:
                level = 20
            elif 500 < scale <= 1500:
                level = 19
            elif 1500 < scale <= 3000:
                level = 18
            elif 3000 < scale <= 5000:
                level = 17
            elif 5000 < scale <= 15000:
                level = 16
            elif 15000 < scale <= 24000:
                level = 15
            elif 24000 < scale <= 32000:
                level = 14
            elif 32000 < scale <= 80000:
                level = 13
            elif 80000 < scale <= 200000:
                level = 12
            elif 200000 < scale <= 400000:
                level = 11
            else:
                level = 10

            url = "http://www.bing.com/maps/?v=2&cp={0}~{1}&lvl={2}&sty=r".format(y_coord, x_coord, level)

            def run_in_other_thread(function):
                @functools.wraps(function)
                def fn_(*args, **kwargs):
                    thread = threading.Thread(target=function, args=args, kwargs=kwargs)
                    thread.start()
                    thread.join()
                return fn_

            openbrowser = run_in_other_thread(webbrowser.open)
            openbrowser(url, new=2)

            del click
            del click_geom
            del coords
            del openbrowser

class GoogleMaps(object):
    """Implementation for BingGoogleMaps_addin.tool_1 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = "NONE"

    def onMouseDownMap(self, x, y, button, shift):

        mxd = arcpy.mapping.MapDocument("CURRENT")
        view = mxd.activeView

        sr = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
        code = sr.factoryCode

        if view == "PAGE_LAYOUT":
            pythonaddins.MessageBox("This tool will not work in Layout View. Please change to Data View.", "Warning", 0)

        elif code == 0:
            pythonaddins.MessageBox("The current Data Frame coordinate system is not an ESRI standard. \n\nThe coordinate system cannot be custom, or undefined.", "Warning", 0)

        else:
            click = arcpy.Point(x, y)

            mxd = arcpy.mapping.MapDocument("CURRENT")
            sr_old = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
            sr_new = arcpy.SpatialReference(4326)
            click_geom = arcpy.PointGeometry(click, sr_old)
            coords = click_geom.projectAs(sr_new)

            scale = float(mxd.activeDataFrame.scale)

            x_coord = coords.firstPoint.X
            y_coord = coords.firstPoint.Y

            if scale <= 564 :
                level = 21
            elif 564  < scale <= 1128:
                level = 20
            elif 1128 < scale <= 2257:
                level = 19
            elif 2257 < scale <= 4514:
                level = 18
            elif 4514 < scale <= 9028:
                level = 17
            elif 9028 < scale <= 18056:
                level = 16
            elif 18056 < scale <= 36112:
                level = 15
            elif 36112 < scale <= 72224:
                level = 14
            elif 72224 < scale <= 144448:
                level = 13
            elif 144448 < scale <= 288895:
                level = 12
            elif 288895 < scale <= 577791:
                level = 11
            elif 577791 < scale <= 1155581:
                level = 10
            elif 1155581 < scale <= 2311162:
                level = 9
            elif 2311162 < scale <= 4622325:
                level = 8
            elif 4622325 < scale <= 9244649:
                level = 7
            elif 9244649 < scale <= 18489298:
                level = 6
            elif 18489298 < scale <= 36978597:
                level = 5
            elif 36978597 < scale <= 73957194:
                level = 4
            else:
                level = 3

            url = "https://www.google.com/maps/@{0},{1},{2}z".format(y_coord, x_coord, level)

            def run_in_other_thread(function):
                @functools.wraps(function)
                def fn_(*args, **kwargs):
                    thread = threading.Thread(target=function, args=args, kwargs=kwargs)
                    thread.start()
                    thread.join()
                return fn_

            openbrowser = run_in_other_thread(webbrowser.open)
            openbrowser(url, new=2)

            del click
            del click_geom
            del coords
            del openbrowser

class GoogleSatellite(object):
    """Implementation for BingGoogleMaps_addin.tool_2 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = "NONE"

    def onMouseDownMap(self, x, y, button, shift):

        mxd = arcpy.mapping.MapDocument("CURRENT")
        view = mxd.activeView

        sr = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
        code = sr.factoryCode

        if view == "PAGE_LAYOUT":
            pythonaddins.MessageBox("This tool will not work in Layout View. Please change to Data View.", "Warning", 0)

        elif code == 0:
            pythonaddins.MessageBox("The current Data Frame coordinate system is not an ESRI standard. \n\nThe coordinate system cannot be custom, or undefined.", "Warning", 0)

        else:
            click = arcpy.Point(x, y)

            mxd = arcpy.mapping.MapDocument("CURRENT")
            sr_old = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
            sr_new = arcpy.SpatialReference(4326)
            click_geom = arcpy.PointGeometry(click, sr_old)
            coords = click_geom.projectAs(sr_new)

            scale = float(mxd.activeDataFrame.scale)

            x_coord = coords.firstPoint.X
            y_coord = coords.firstPoint.Y

            if scale <= 564 :
                level = 51
            elif 564  < scale <= 1128:
                level = 101
            elif 1128 < scale <= 2257:
                level = 202
            elif 2257 < scale <= 4514:
                level = 405
            elif 4514 < scale <= 9028:
                level = 809
            elif 9028 < scale <= 18056:
                level = 1619
            elif 18056 < scale <= 36112:
                level = 3238
            elif 36112 < scale <= 72224:
                level = 6476
            elif 72224 < scale <= 144448:
                level = 12951
            elif 144448 < scale <= 288895:
                level = 25902
            elif 288895 < scale <= 577791:
                level = 51805
            elif 577791 < scale <= 1155581:
                level = 103610
            elif 1155581 < scale <= 2311162:
                level = 207220
            elif 2311162 < scale <= 4622325:
                level = 414439
            elif 4622325 < scale <= 9244649:
                level = 828878
            elif 9244649 < scale <= 18489298:
                level = 1657756
            elif 18489298 < scale <= 36978597:
                level = 3315513
            elif 36978597 < scale <= 73957194:
                level = 6631025
            else:
                level = 13262051

            url = "https://www.google.com/maps/@{0},{1},{2}m/data=!3m1!1e3!5m1!1e4".format(y_coord, x_coord, level)

            def run_in_other_thread(function):
                @functools.wraps(function)
                def fn_(*args, **kwargs):
                    thread = threading.Thread(target=function, args=args, kwargs=kwargs)
                    thread.start()
                    thread.join()
                return fn_

            openbrowser = run_in_other_thread(webbrowser.open)
            openbrowser(url, new=2)

            del click
            del click_geom
            del coords
            del openbrowser

class GoogleStreetView(object):
    """Implementation for BingGoogleMaps_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = "NONE"

    def onMouseDownMap(self, x, y, button, shift):

        mxd = arcpy.mapping.MapDocument("CURRENT")
        view = mxd.activeView

        sr = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
        code = sr.factoryCode

        if view == "PAGE_LAYOUT":
            pythonaddins.MessageBox("This tool will not work in Layout View. Please change to Data View.", "Warning", 0)

        elif code == 0:
            pythonaddins.MessageBox("The current Data Frame coordinate system is not an ESRI standard. \n\nThe coordinate system cannot be custom, or undefined.", "Warning", 0)

        else:
            click = arcpy.Point(x, y)

            mxd = arcpy.mapping.MapDocument("CURRENT")
            sr_old = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
            sr_new = arcpy.SpatialReference(4326)
            click_geom = arcpy.PointGeometry(click, sr_old)
            coords = click_geom.projectAs(sr_new)

            scale = float(mxd.activeDataFrame.scale)

            x_coord = coords.firstPoint.X
            y_coord = coords.firstPoint.Y

            url = "http://maps.google.com/?cbll={0},{1}&cbp=12,90,0,0,5&layer=c".format(y_coord, x_coord)

            def run_in_other_thread(function):
                @functools.wraps(function)
                def fn_(*args, **kwargs):
                    thread = threading.Thread(target=function, args=args, kwargs=kwargs)
                    thread.start()
                    thread.join()
                return fn_

            openbrowser = run_in_other_thread(webbrowser.open)
            openbrowser(url, new=2)

            del click
            del click_geom
            del coords
            del openbrowser

class GoogleTerrain(object):
    """Implementation for BingGoogleMaps_addin.tool_3 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = "NONE"

    def onMouseDownMap(self, x, y, button, shift):

        mxd = arcpy.mapping.MapDocument("CURRENT")
        view = mxd.activeView

        sr = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
        code = sr.factoryCode

        if view == "PAGE_LAYOUT":
            pythonaddins.MessageBox("This tool will not work in Layout View. Please change to Data View.", "Warning", 0)

        elif code == 0:
            pythonaddins.MessageBox("The current Data Frame coordinate system is not an ESRI standard. \n\nThe coordinate system cannot be custom, or undefined.", "Warning", 0)

        else:
            click = arcpy.Point(x, y)

            mxd = arcpy.mapping.MapDocument("CURRENT")
            sr_old = arcpy.mapping.ListDataFrames(mxd)[0].spatialReference
            sr_new = arcpy.SpatialReference(4326)
            click_geom = arcpy.PointGeometry(click, sr_old)
            coords = click_geom.projectAs(sr_new)

            scale = float(mxd.activeDataFrame.scale)

            x_coord = coords.firstPoint.X
            y_coord = coords.firstPoint.Y

            if scale <= 564 :
                level = 21
            elif 564  < scale <= 1128:
                level = 20
            elif 1128 < scale <= 2257:
                level = 19
            elif 2257 < scale <= 4514:
                level = 18
            elif 4514 < scale <= 9028:
                level = 17
            elif 9028 < scale <= 18056:
                level = 16
            elif 18056 < scale <= 36112:
                level = 15
            elif 36112 < scale <= 72224:
                level = 14
            elif 72224 < scale <= 144448:
                level = 13
            elif 144448 < scale <= 288895:
                level = 12
            elif 288895 < scale <= 577791:
                level = 11
            elif 577791 < scale <= 1155581:
                level = 10
            elif 1155581 < scale <= 2311162:
                level = 9
            elif 2311162 < scale <= 4622325:
                level = 8
            elif 4622325 < scale <= 9244649:
                level = 7
            elif 9244649 < scale <= 18489298:
                level = 6
            elif 18489298 < scale <= 36978597:
                level = 5
            elif 36978597 < scale <= 73957194:
                level = 4
            else:
                level = 3

            url = "https://www.google.com/maps/@{0},{1},{2}z/data=!5m1!1e4".format(y_coord, x_coord, level)

            def run_in_other_thread(function):
                @functools.wraps(function)
                def fn_(*args, **kwargs):
                    thread = threading.Thread(target=function, args=args, kwargs=kwargs)
                    thread.start()
                    thread.join()
                return fn_

            openbrowser = run_in_other_thread(webbrowser.open)
            openbrowser(url, new=2)

            del click
            del click_geom
            del coords
            del openbrowser

class Information(object):
    """Implementation for BingGoogleMaps_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        current_date = str(time.strftime("%b %d, %Y"))
        pythonaddins.MessageBox("Last Updated:\nFeb 04, 2015\n\nCurrent Date:\n{0}\n\n------------------------\nStreet View\n1.0v2\n------------------------\n\nFor updates visit:\nwww.ianbroad.com".format(current_date), "Information", 0)
