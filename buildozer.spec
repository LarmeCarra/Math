[app]

# (str) Title of your application
title = Lustio test

# (str) Package name
package.name = myapp.lustio

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 2)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = kivy==2.2.0,kivymd==1.1.1,python3

# (str) Custom source folders for requirements
requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Custom source folders for garden requirements
#garden_requirements.source.somegardenname = ../../somelocalpath/somegardenname

# (list) List of inclusions using pattern matching
include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of directory to include (relative to the current directory)
include_dirs = ./

# (list) List of inclusions using pattern matching
include_patterns = assets/*,images/*.png

# (list) List of exclusions using pattern matching
exclude_patterns =

# (str) Path to a custom icon
icon.filename = %(source.dir)s/icon.jpg

# (str) Path to a custom loading spinner logo
;presplash.filename = %(source.dir)s/iii.png

# (str) Path to a custom background image/logo
;android.background_image =

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug [recommended])
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

