#!/usr/bin/env python3
"""Append macOS arm64 export preset to export_presets.cfg
Based on Godot 4.2.2 source: platform/macos/export/export_plugin.cpp"""

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

export/distribution_type=1
binary_format/architecture="arm64"
custom_template/debug=""
custom_template/release=""
debug/export_console_wrapper=1
application/icon=""
application/icon_interpolation=4
application/bundle_identifier="com.bussin.griddycode"
application/signature=""
application/app_category="Games"
application/short_version="1.0"
application/version="1.0"
application/copyright=""
application/min_macos_version="10.12"
application/export_angle=0
display/high_res=true
xcode/platform_build="14C18"
xcode/sdk_version="13.1"
xcode/sdk_build="22C55"
xcode/sdk_name="macosx13.1"
xcode/xcode_version="1420"
xcode/xcode_build="14C18"
codesign/codesign=0
codesign/installer_identity=""
codesign/apple_team_id=""
codesign/identity=""
codesign/certificate_file=""
codesign/certificate_password=""
codesign/provisioning_profile=""
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
codesign/entitlements/app_sandbox/device_bluetooth=false
"""

with open("export_presets.cfg", "a") as f:
    f.write(preset)

print("macOS export preset appended successfully.")
