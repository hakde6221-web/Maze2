[app]

title = Maze
package.name = maze2
package.domain = org.maze

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav

version = 1.0.0

requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 1

android.permissions = 

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.enable_androidx = True
android.private_storage = True

android.logcat_filters = *:S python:D

icon.filename = %(source.dir)s/icon.png

[buildozer]

log_level = 2
warn_on_root = 0
