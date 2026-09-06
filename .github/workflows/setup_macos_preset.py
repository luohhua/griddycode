#!/usr/bin/env python3
"""Append macOS arm64 export preset to export_presets.cfg"""

preset = """
[preset.2]

name="macOS"
platform="macOS"
runnable=true
dedicated_server=false
custom_features=""
export_filter="all_resources"
include_filter="*.lua"
exclude_filter=""
export_path="Builds/macOS/GriddyCode.zip"
encryption_include_filters=""
encryption_exclude_filters=""
encrypt_pck=false
encrypt_directory=false

[preset.2.options]

custom_template/debug=""
custom_template/release=""
debug/export_console_wrapper=0
texture_format/s3tc_bptc=true
texture_format/etc2_astc=false
binary_format/architecture="arm64"
codesign/enable=false
codesign/identity=""
codesign/timestamp=true
codesign/hardened_runtime=false
codesign/replace_existing_signature=true
codesign/entitlements/custom_file=""
codesign/entitlements/allow_jit_code_execution=false
codesign/entitlements/allow_unsigned_executable_memory=false
codesign/entitlements/allow_dyld_environment_variables=false
codesign/entitlements/disable_library_validation=false
codesign/entitlements/audio_input=false
codesign/entitlements/camera=false
codesign/entitlements/location=false
codesign/entitlements/address_book=false
codesign/entitlements/calendars=false
codesign/entitlements/photos_library=false
codesign/entitlements/apple_events=false
codesign/entitlements/debugging=false
codesign/entitlements/app_sandbox/enabled=false
codesign/entitlements/app_sandbox/network_server=false
codesign/entitlements/app_sandbox/network_client=false
codesign/entitlements/app_sandbox/device_usb=false
codesign/entitlements/app_sandbox/files_downloads=0
codesign/entitlements/app_sandbox/files_pictures=0
codesign/entitlements/app_sandbox/files_music=0
codesign/entitlements/app_sandbox/files_movies=0
codesign/custom_options=PackedStringArray()
notarization/enable=false
notarization/apple_id=""
notarization/apple_id_password=""
notarization/team_id=""
application/icon=""
application/icon_interpolation=4
application/bundle_identifier="com.bussin.griddycode"
application/app_category=""
application/short_version="1.0"
application/version="1.0"
application/copyright=""
application/min_macos_version="15.0"
application/export_angle=0
ssh_remote_deploy/enabled=false
"""

with open("export_presets.cfg", "a") as f:
    f.write(preset)

print("macOS export preset appended successfully.")
