"""
General functions that all modules might need. Created by Emmanuel Azadze on 12/29/2023 (Fri).
"""
import os, sys, time, string, random, re, logging
from math import pi, log, ceil
from datetime import datetime as dt, timedelta as td

#################################################################################################################################################
#                                                         Environment Variables                                                                 #
#################################################################################################################################################
TESTFILE = 'test.txt'
COMPUTERNAME = os.environ.get('COMPUTERNAME')
USER = os.environ.get("USERNAME")
HOME = os.environ.get("USERPROFILE").replace('\\', '/')
DESKTOPPATH = os.path.join(HOME, 'Desktop').replace('\\', '/')
LOGFORMAT = '>> %(asctime)s %(levelname)s:%(message)s...'
DATEFORMAT = '%Y%m%d %I:%M:%S %p'
LOGLEVEL = 'info'

def resolve(variable: str) -> str:
    """
    Resolves user environment variables such as user home ~
    """
    return fixpath(os.environ.get(key = variable, default = os.path.expanduser(f'{variable}')))
    
def resolvepath(filename: str, folder: str = os.getcwd()) -> str:
    """
    Converts filename or foldername to full path. Assumes file exists in current directory.
    """
    fullpath = os.path.join(r'{folder}'.format(folder = folder), r'{filename}'.format(filename = filename))
    
    return fixpath(fullpath)
    
def fixpath(filepath: str, illegal_character: str = '\\', replacement: str = '/') -> str:
    """
    Replaces '\' with '/' in filepath and returns it.
    """
    return filepath.replace(illegal_character, replacement)

def lognamer(modulename: str = __file__, fullpath: bool = True) -> str:
    """
    Returns the full path log file name using the module's directory.
    """
    return r'{}.log'.format(os.path.splitext(modulename)[0])

def loglevelconverter(loglevel: str | int = LOGLEVEL) -> int:
    """
    Converts loglevel from string to the proper logging.level value. Returns input if it is an integer.
    """
    loglevel = str(loglevel).lower()
    loglevels = ['debug', 'info', 'warning', 'error', 'critical', 'fatal']
    loglevelsint = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL, logging.FATAL]
    try:
        newloglevel = int(loglevel)
    except ValueError:
        try:
            if loglevel in ['highest', 'max', 'maximum', 'greatest']:
                newloglevel = loglevelsint[-1]
            elif loglevel in ['finest', 'lowest', 'min', 'minimum']:
                newloglevel = loglevelsint[0]
            else:
                newloglevel = loglevelsint[loglevels.index(loglevel)]
        except ValueError:
            newloglevel = logging.NOTSET
    
    return newloglevel
    
def getlogger(logfile: str | None = None, logformat: str = LOGFORMAT, dateformat: str = DATEFORMAT, loglevel: str = LOGLEVEL) -> logging.getLoggerClass:
    """
    Creates and returns a logger object from the logging module with the specified format and log level.
    """
    logger = logging.getLogger()
    logfmt = logging.Formatter(fmt = logformat, datefmt = dateformat)
    
    if not logfile == None:
        logging.basicConfig(filename = lognamer(logfile), format = logformat, datefmt = dateformat, force = True)
        streamhandler = logging.StreamHandler()
        streamhandler.setFormatter(fmt = logfmt)
        # streamhandler.setLevel(level = loglevelconverter(loglevel))
        logger.addHandler(streamhandler)
        
    else:
        logging.basicConfig(stream = logfile, format = logformat, datefmt = dateformat, force = True)
        # filehandler = logging.FileHandler(logfile)
        # filehandler.setFormatter(fmt = logformat)
        # filehandler.setLevel(level = loglevelconverter(loglevel))
        # logger.addHandler(filehandler)
        
    return logger
    
def timetill(hours: int = 8, minutes: int = 1, seconds: int = 0, utcbool: bool = True, max_random_time: int = 0):
    """
    Returns time till specified time in seconds. Can offer in utc time if desired.
    """
    if bool(int(utcbool)):
        now = dt.utcnow()
    else:
        now = dt.now()
    dhour, dminute, dsecond = now.hour, now.minute, now.second
    future0 = now + td(hours = -dhour, minutes = -dminute, seconds = -dsecond)
    future = future0 + td(hours = hours, minutes = minutes, seconds = seconds)
    newseconds = (future - now).total_seconds()
    if newseconds < 0:
        newseconds += td(days = 1).total_seconds()
    
    return int(newseconds + random.randint(0, max_random_time))

def timer(seconds: int = 0, minutes: int = 0, hours: int = 0):
    """
    Countdown timer.
    """
    total_time = int(3600*int(hours) + 60*int(minutes) + int(seconds))
    print(f'>> Timer set for {time.strftime("%H hours, %M minutes, and %S seconds...", time.gmtime(total_time))}')
    time_left = total_time
    while time_left:
        dtime = 1
        print(f'\r>> Time left: {time.strftime("%H hours, %M minutes, and %S seconds...", time.gmtime(time_left))}', end = '')
        time.sleep(dtime)
        time_left -= dtime
    print(f'\r>> Timer complete.', f' '*40)
    
def intisolator(item: str) -> int:
    """
    Strips integers of everything else around them and converts *int* to int.
    """
    return int(re.sub('\D', '', str(item)))

def two_num_fun(num: int) -> str|int:
    """
    Checks and returns number with 0 in front if one digit.
    """
    return int(num) if len(str(int(num))) > 1 else f'0{int(num)}'
    
def newfilenamefun(inputfile: str, appendage: str = '_out', origin: bool = False, extension: str = '') -> str:
    """
    Creates and returns a new file name given a file name as input. Modifies the new file extension if one is provided.
    Appends appendage to file name till the new file name does not exist on the system.
    """
    if len(str(appendage)):
        filename, ext = os.path.splitext(inputfile)
        filenamebase = filename.split(appendage)[0]
        
        if not bool(int(origin)):
            try:
                filenumber = int(filename.split(appendage)[1])
            except:
                filenumber = -1
            
            if len(str(extension)):
                newfilename = r'{base}{appendage}{num}.{extension}'.format(base = filenamebase, appendage = appendage, num = filenumber+1, extension = extension.strip('.'))
            else:
                newfilename = r'{base}{appendage}{num}.{ext}'.format(base = filenamebase, appendage = appendage, num = filenumber+1, ext = ext.strip('.'))
        
        else:
            if len(str(extension)):
                newfilename = r'{base}{appendage}.{extension}'.format(base = filenamebase, appendage = appendage, extension = extension.strip('.'))
            else:
                newfilename = r'{base}{appendage}.{ext}'.format(base = filenamebase, appendage = appendage, ext = ext.strip('.'))
        
        if os.path.exists(newfilename):
            newfilename = newfilenamefun(inputfile = newfilename, appendage = appendage, extension = extension)
    
    return newfilename

def getfilesize(file: str = __file__, fmt: str = 'byte', kb2b: int = 1024) -> int:
    """
    Returns file or folder size in specified units. Default is bytes.
    """
    filesize = os.stat(r'{}'.format(file)).st_size
    
    if fmt.lower() in ['b', 'byte', 'bytes']:
        pass
    elif fmt.lower() in ['kb', 'kilobyte', 'kilobytes']:
        filesize /= kb2b
    elif fmt.lower() in ['mb', 'megabyte', 'megabytes']:
        filesize /= kb2b**2
    elif fmt.lower() in ['gb', 'gigabyte', 'gigabytes']:
        filesize /= kb2b**3
    elif fmt.lower() in ['tb', 'terabyte', 'terabytes']:
        filesize /= kb2b**4
    elif fmt.lower() in ['pb', 'petabyte', 'petabytes']:
        filesize /= kb2b**5
    else:
        pass
    
    return filesize
    
# End of file.