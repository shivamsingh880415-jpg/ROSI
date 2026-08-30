[app]

# (str) Title of your application
title = ROSI AI Assistant

# (str) Package name
package.name = rosiai

# (str) Package domain (needed for android/ios packaging)
package.domain = com.rosi.ai

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (int) Android API to use
android.api = 31

# (int) Android min API to use
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 23b

# (bool) Indicate if you accept the Android SDK license
android.accept_sdk_license = True

# (list) Target architectures to build for
android.archs = arm64-v8a

# (list) Supported orientations
orientation = portrait
