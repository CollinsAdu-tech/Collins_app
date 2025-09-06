[app]
title = Collins App
package.name = collinsapp
package.domain = org.collins
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,yt-dlp
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = armeabi-v7a,arm64-v8a
