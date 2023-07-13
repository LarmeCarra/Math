[app]

# (str) Title of your application
title = Lustio

# (str) Package name
package.name = myapp.lustio

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py file is located
source.dir = .

# (str) Source code where the main.py file is located
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) Application requirements
requirements = kivy==2.2.0,kivymd==1.1.1,pillow,python3

# (str) Custom source folders for requirements
# separate with commas (app_folder = source_folder,app_folder2 = source_folder2)
source.custom_data = assets/fonts,assets/images

# (str) Presplash of the application
presplash.filename = iii.jpg

# (str) Icon of the application
icon.filename = icon.jpg

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

# (str) Path to the directory containing the build python3 binary (optional)
# python3 = /usr/bin/python3

# (bool) if true, the application will run on the top of another
# already visible application. (windows only)
# overlay = False

# (str) macOS framework to include other than default Kivy framework
# macos.frameworks =


# (str) iOS framework to include (comma separated values) (eg.  = sqlite3,avfoundation)
# ios.frameworks =


# (str) Name of the iOS/Android project
# (must be pure ascii, no special characters, to match the project filename in the SDK)
# package.name = myapp

# (str) URL pointing to the source code repository
# source.url =


# (str) Version (human-readable, not required)
# version = 0.1

# (str) Application versioning scheme (parseable by distutils.version.parse)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements for development
# comma separated e.g. requirements = sqlite3,kivy
requirements.dev = sqlite3,kivy==2.2.0,kivymd==1.1.1

# (str) Custom source folders for development requirements
# separate with commas (app_folder = source_folder,app_folder2 = source_folder2)
# source.custom_data = app_data_folder:data

# (str) Extra commands to run customizing build process
# commands =


# (bool) Whether to skip building android
# skip_build_android = False

# (bool) Whether to skip building ios
# skip_build_ios = False

# (str) iOS SDK to use
# ios.sdk =


# (str) Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# arch = armeabi-v7a

# (int) Android API to use
# android.api = 27

# (int) Minimum API required for the application
# android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 27

# (str) Android NDK version to use
# android.ndk = 19b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
# android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path =


# (bool) Use a black overlay (private storage) for bundled python
# black_overlay = False

# (str) The --permission argument for the Python interpreter
# android.permissions = INTERNET

# (bool) If true, then skip trying to update the Android sdk
# android.skip_update = False

# (bool) If true, then automatically accept SDK license
android.accept_sdk_license = True

# (str) iOS deployment target
# ios.deployment_target = 10.0

# (str) iOS app ID
# ios.appid =


# (str) iOS bundle name
# ios.bundle_name =

# (str) iOS bundle identifier
# ios.bundle_identifier =

# (str) iOS bundle version
# ios.bundle_version =

# (str) iOS build number
# ios.build_number = 1.0

# (list) Custom xcodebuild arguments
# ios.custom_xcodebuild_args = -UseModernBuildSystem=0

# (str) Plist additions that will be made to Info.plist
# ios.plist_extras =

# (str) Path to a custom Entitlements.plist
# ios.entitlements =

# (str) Path to a custom debug keystore to use for signing the debug version of the app
# ios.debug.keystore = %(USER_HOME)s/.android/debug.keystore

# (str) The iOS code signing identity to use
# ios.codesign.identity = iPhone Developer

# (str) The iOS mobile provision to use for signing the app
# ios.codesign.provisioning_profile =

# (str) The iOS bundle version
# ios.bundle_version = 1.0

# (list) Permissions
# android.permissions = INTERNET

# (str) Name of the application stack in case you are using st2 instead of st (must be pure ascii, no special characters)
# st2.name = myapp

# (str) Title of the application stack in case you are using st2 instead of st (human-readable)
# st2.title = My App

# (str) Name of the application binary file (without extension)
# app_id = myapp

# (str) Package name
# package.name = myapp

# (str) Package domain (needed for android/ios packaging)
# package.domain = org.test

# (str) Source code where the main.py file is located
# source.dir =


# (str) Source code where the main.py file is located
# source.include_exts = py,png,jpg,kv,atlas


# (list) List of inclusions using pattern matching
# include_patterns = *.py,*.kv,*.atlas,*.png,*.jpg

# (list) List of exclusions using pattern matching
# exclude_patterns = licenses/*.txt,images/*/*.jpg

# (str) Application versioning scheme (parseable by distutils.version.parse)
# version.regex = __version__ = ['"](.*)['"]
# version.filename =

 %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# requirements = kivy

# (str) Custom source folders for requirements
# separate with commas (app_folder = source_folder,app_folder2 = source_folder2)
# source.custom_data = assets/fonts,assets/images

# (bool) Enable / disable build mode (default: False)
# edit = False

# (str) Path to a custom blacklist file (default: blacklist.txt)
# ignore_path = blacklist.txt

# (str) Path to a custom whitelist file (default: whitelist.txt)
# whitelist_path = whitelist.txt
