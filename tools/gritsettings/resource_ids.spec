# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# This file is used to assign starting resource ids for resources and strings
# used by Chromium.  This is done to ensure that resource ids are unique
# across all the grd files.  If you are adding a new grd file, please add
# a new entry to this file.
#
# The entries below are organized into sections. When adding new entries,
# please use the right section. Try to keep entries in alphabetical order.
#
# - chrome/app/
# - chrome/browser/
# - chrome/ WebUI
# - chrome/ miscellaneous
# - chromeos/
# - components/
# - ios/ (overlaps with chrome/)
# - content/
# - ios/web/ (overlaps with content/)
# - everything else
#
# The range of ID values, which is used by pak files, is from 0 to 2^16 - 1.
#
# IMPORTANT: For update instructions, see README.md.
{
  # The first entry in the file, SRCDIR, is special: It is a relative path from
  # this file to the base of your checkout.
  "SRCDIR": "../..",

  # START chrome/app section.
  # Previous versions of this file started with resource id 400, so stick with
  # that.
  #
  # chrome/ and ios/chrome/ must start at the same id.
  # App only use one file depending on whether it is iOS or other platform.
  # Chromium strings and Google Chrome strings must start at the same id.
  # We only use one file depending on whether we're building Chromium or
  # Google Chrome.
  "chrome/app/chromium_strings.grd": {
    "messages": [400],
  },
  "chrome/app/google_chrome_strings.grd": {
    "messages": [400],
  },

  # Leave lots of space for generated_resources since it has most of our
  # strings.
  "chrome/app/generated_resources.grd": {
    # Big alignment since strings (previous item) are frequently added.
    "META": {"join": 2, "align": 200},
    "messages": [600],
  },

  "chrome/app/resources/locale_settings.grd": {
    # Big alignment since strings (previous item) are frequently added.
    "META": {"align": 1000},
    "messages": [1000],
  },

  # These each start with the same resource id because we only use one
  # file for each build (chromiumos, google_chromeos, linux, mac, or win).
  "chrome/app/resources/locale_settings_chromiumos.grd": {
    # Big alignment since strings (previous item) are frequently added.
    "META": {"align": 100},
    "messages": [1100],
  },
  "chrome/app/resources/locale_settings_google_chromeos.grd": {
    "messages": [1100],
  },
  "chrome/app/resources/locale_settings_linux.grd": {
    "messages": [1100],
  },
  "chrome/app/resources/locale_settings_mac.grd": {
    "messages": [1100],
  },
  "chrome/app/resources/locale_settings_win.grd": {
    "messages": [1100],
  },

  "chrome/app/theme/chrome_unscaled_resources.grd": {
    "META": {"join": 5},
    "includes": [1120],
  },

  # Leave space for theme_resources since it has many structures.
  "chrome/app/theme/theme_resources.grd": {
    "structures": [1140],
  },
  # END chrome/app section.

  # START chrome/browser section.
  "chrome/browser/dev_ui_browser_resources.grd": {
    # Big alignment at start of section.
    "META": {"align": 100},
    "includes": [1200],
  },
  "chrome/browser/browser_resources.grd": {
    "includes": [1220],
    "structures": [1240],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/feedback_webui/resources.grd": {
    "META": {"sizes": {"includes": [20],}},
    "includes": [1260],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/app_service_internals/resources.grd": {
    "META": {"sizes": {"includes": [5],}},
    "includes": [1280],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/bookmarks/resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [1300],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/browser_switch/resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [1320],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/arc_account_picker/resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [1340],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/assistant_optin/assistant_optin_resources.grd": {
    "META": {"sizes": {"includes": [80]}},
    "includes": [1360],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/gaia_action_buttons/resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [1380],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/emoji_picker/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [1400],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/launcher_internals/resources.grd": {
    "META": {"sizes": {"includes": [50]}},
    "includes": [1420],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/profile_internals/resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [1440],
  },
  "chrome/browser/resources/chromeos/app_icon/app_icon_resources.grd": {
    "structures": [1460],
  },
  "chrome/browser/resources/chromeos/login/oobe_conditional_resources.grd": {
    "META": {"sizes": {"includes": [150], "structures": [300]}},
    "includes": [1480],
    "structures": [1500],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/login/oobe_unconditional_resources.grd": {
    "META": {"sizes": {"includes": [350]}},
    "includes": [1520],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/multidevice_internals/resources.grd": {
    "META": {"sizes": {"includes": [35]}},
    "includes": [1540],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/multidevice_setup/multidevice_setup_resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [1560],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/notification_tester/resources.grd": {
    "META": {"sizes": {"includes": [5]}},
    "includes": [1580],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/commander/commander_resources.grd": {
    "META": {"sizes": {"includes": [15]}},
    "includes": [1600],
  },
  "chrome/browser/resources/component_extension_resources.grd": {
    "includes": [1620],
    "structures": [1640],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/access_code_cast/resources.grd": {
    "META": {"sizes": {"includes": [50]}},
    "includes": [1660],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/connectors_internals/resources.grd": {
    "META": {"sizes": {"includes": [15]}},
    "includes": [1680],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/discards/discards_resources.grd": {
    "META": {"sizes": {"includes": [20],}},
    "includes": [1700],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/downloads/resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [1720],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/extensions/resources.grd": {
    "META": {"sizes": {"includes": [80],}},
    "includes": [1740],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/history/resources.grd": {
    "META": {"sizes": {"includes": [40]}},
    "includes": [1760],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/identity_internals/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [1780],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/image_editor/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [1800],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/image_editor/image_editor_untrusted_resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [1820],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/internals/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [1840],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/management/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [1860],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/new_tab_page_instant/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [1880],
  },
   "chrome/browser/resources/webid/webid_resources.grd": {
    "includes": [1900],
    "structures": [1920],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/nearby_internals/nearby_internals_resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [1940],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/nearby_share/nearby_share_dialog_resources.grd": {
    "META": {"sizes": {"includes": [100]}},
    "includes": [1960],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/media_router/cast_feedback/resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [1980],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/new_tab_page/resources.grd": {
    "META": {"sizes": {"includes": [200]}},
    "includes": [2000],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/new_tab_page_third_party/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2020],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/ntp4/apps_resources.grd": {
    "META": {"sizes": {"includes": [40]}},
    "includes": [2040],
  },
  "chrome/browser/resources/preinstalled_web_apps/resources.grd": {
    "includes": [2060],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/pdf/resources.grd": {
    "META": {"sizes": {"includes": [200]}},
    "includes": [2080],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/print_preview/resources.grd": {
    "META": {"sizes": {"includes": [500],}},
    "includes": [2100],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/privacy_sandbox/resources.grd": {
    "META": {"sizes": {"includes": [20],}},
    "includes": [2120],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/segmentation_internals/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2140],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/side_panel/customize_chrome/resources.grd": {
    "META": {"sizes": {"includes": [20],}},
    "includes": [2160],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/side_panel/side_panel_resources.grd": {
    "META": {"sizes": {"includes": [20],}},
    "includes": [2180],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/settings/chromeos/os_settings_resources.grd": {
    "META": {"sizes": {"includes": [1000],}},
    "includes": [2200],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/settings/settings_resources.grd": {
    "META": {"sizes": {"includes": [500],}},
    "includes": [2220],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/signin/profile_picker/resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [2240],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/signin/resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [2260],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/support_tool/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [2280],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/tab_search/tab_search_resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [2300],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/tab_strip/tab_strip_resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [2320],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/welcome/resources.grd": {
    "META": {"sizes": {"includes": [30]}},
    "includes": [2340],
  },
  "chrome/browser/supervised_user/supervised_user_unscaled_resources.grd": {
    "includes": [2360],
  },
  "chrome/browser/test_dummy/internal/android/resources/resources.grd": {
    "includes": [2380],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/webui_gallery/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [2400],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/whats_new/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2420],
  },
  # END chrome/browser section.

  # START chrome/ WebUI resources section
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/browsing_topics/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2440],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/bluetooth_internals/resources.grd": {
    "META": {"sizes": {"includes": [30],}},
    "includes": [2460],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/audio/resources.grd": {
    "META": {"sizes": {"includes": [30]}},
    "includes": [2480],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/bluetooth_pairing_dialog/bluetooth_pairing_dialog_resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [2500],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/chromebox_for_meetings/resources.grd": {
    "META": {"sizes": {"includes": [5]}},
    "includes": [2520],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/internet_config_dialog/internet_config_dialog_resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [2540],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/internet_detail_dialog/internet_detail_dialog_resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [2560],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/network_ui/network_ui_resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2580],
  },
  "<(SHARED_INTERMEDIATE_DIR)/components/history_clusters/history_clusters_internals/resources/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2600],
  },
  "<(SHARED_INTERMEDIATE_DIR)/components/download/resources/download_internals/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2620],
  },
  "<(SHARED_INTERMEDIATE_DIR)/components/optimization_guide/optimization_guide_internals/resources/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2640],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/gaia_auth_host/resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [2660],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/invalidations/resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [2680],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/media/resources.grd": {
    "META": {"sizes": {"includes": [20],}},
    "includes": [2700],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/net_internals/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [2720],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/omnibox/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [2740],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/quota_internals/quota_internals_resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [2760],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/sync_file_system_internals/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [2780],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/usb_internals/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [2800],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/webapks/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2820],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/webui_js_error/resources.grd": {
   "META": {"sizes": {"includes": [10],}},
   "includes": [2840],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/app_settings/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [2860],
  },
  "<(SHARED_INTERMEDIATE_DIR)/components/sync/driver/resources/resources.grd": {
   "META": {"sizes": {"includes": [30],}},
    "includes": [2880],
  },
  "components/resources/dev_ui_components_resources.grd": {
    "includes": [2900],
  },
  "<(SHARED_INTERMEDIATE_DIR)/content/browser/resources/media/resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [2920],
  },
  "<(SHARED_INTERMEDIATE_DIR)/content/browser/resources/quota/resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [2940],
  },
  "<(SHARED_INTERMEDIATE_DIR)/content/browser/webrtc/resources/resources.grd": {
    "META": {"sizes": {"includes": [20],}},
    "includes": [2960],
  },
  "content/dev_ui_content_resources.grd": {
    "includes": [2980],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/feed/resources.grd": {
    "META": {"sizes": {"includes": [20]}},
    "includes": [3000],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/browser/resources/chromeos/manage_mirrorsync/resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [3020],
  },
  # END chrome/ WebUI resources section

  # START chrome/ miscellaneous section.
  "chrome/common/common_resources.grd": {
    # Big alignment at start of section.
    "META": {"align": 100},
    "includes": [3100],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/common/chromeos/extensions/chromeos_system_extensions_resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [3120],
  },
  "chrome/credential_provider/gaiacp/gaia_resources.grd": {
    "includes": [3140],
    "messages": [3160],
  },
  "chrome/renderer/resources/renderer_resources.grd": {
    "includes": [3180],
    "structures": [3200],
  },
  "<(SHARED_INTERMEDIATE_DIR)/chrome/test/data/webui/resources.grd": {
    "META": {"sizes": {"includes": [900],}},
    "includes": [3220],
  },
  "chrome/test/data/webui_test_resources.grd": {
    "includes": [3240],
  },
  "chrome/test/data/chrome_test_resources.grd": {
    "messages": [3260],
  },
  # END chrome/ miscellaneous section.

  # START chromeos/ section.
  "chromeos/chromeos_strings.grd": {
    # Big alignment at start of section.
    "META": {"align": 100},
    "messages": [3300],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/ambient/resources/lottie_resources.grd": {
    "META": {"sizes": {"includes": [100],}},
    "includes": [3320],
  },
  "chromeos/ash/resources/ash_resources.grd": {
    "includes": [3340],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/camera_app_ui/ash_camera_app_resources.grd": {
    "META": {"sizes": {"includes": [300],}},
    "includes": [3360],
  },
  "ash/webui/camera_app_ui/resources/strings/camera_strings.grd": {
    "messages": [3380],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/color_internals/resources/ash_color_internals_resources.grd": {
    "META": {"sizes": {"includes": [20],}},
    "includes": [3400],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/connectivity_diagnostics/resources/connectivity_diagnostics_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [3420],
  },
  "ash/webui/diagnostics_ui/resources/diagnostics_app_resources.grd": {
    "includes": [3440],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/file_manager/resources/file_manager_swa_resources.grd": {
    "META": {"sizes": {"includes": [100]}},
    "includes": [3460],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/file_manager/untrusted_resources/file_manager_untrusted_resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [3480],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/guest_os_installer/resources/ash_guest_os_installer_resources.grd": {
    "META": {"sizes": {"includes": [10]}},
    "includes": [3500],
  },
  "ash/webui/help_app_ui/resources/help_app_resources.grd": {
    "includes": [3520],
  },
  # Both help_app_kids_magazine_bundle_resources.grd and
  # help_app_kids_magazine_bundle_mock_resources.grd start with the same id
  # because only one of them is built depending on if src_internal is available.
  # Lower bound for number of resource ids is the number of files, which is 3 in
  # in this case (HTML, JS and CSS file).
  "ash/webui/help_app_ui/resources/prod/help_app_kids_magazine_bundle_resources.grd": {
    "META": {"sizes": {"includes": [5],}},
    "includes": [3540],
  },
  "ash/webui/help_app_ui/resources/mock/help_app_kids_magazine_bundle_mock_resources.grd": {
    "includes": [3540],
  },
  # Both help_app_bundle_resources.grd and help_app_bundle_mock_resources.grd
  # start with the same id because only one of them is built depending on if
  # src_internal is available. Lower bound is that we bundle ~100 images for
  # offline articles with the app, as well as strings in every language (74),
  # and bundled content in the top 25 languages (25 x 2).
  "ash/webui/help_app_ui/resources/prod/help_app_bundle_resources.grd": {
    "META": {"sizes": {"includes": [300],}},  # Relies on src-internal.
    "includes": [3560],
  },
  "ash/webui/help_app_ui/resources/mock/help_app_bundle_mock_resources.grd": {
    "includes": [3560],
  },
  "ash/webui/media_app_ui/resources/media_app_resources.grd": {
    "META": {"join": 2},
    "includes": [3580],
  },
  # Both media_app_bundle_resources.grd and media_app_bundle_mock_resources.grd
  # start with the same id because only one of them is built depending on if
  # src_internal is available. Lower bound for number of resource ids is number
  # of languages (74).
  "ash/webui/media_app_ui/resources/prod/media_app_bundle_resources.grd": {
    "META": {"sizes": {"includes": [120],}},  # Relies on src-internal.
    "includes": [3600],
  },
  "ash/webui/media_app_ui/resources/mock/media_app_bundle_mock_resources.grd": {
    "includes": [3600],
  },
  "ash/webui/print_management/resources/print_management_resources.grd": {
    "META": {"join": 2},
    "includes": [3620],
    "structures": [3640],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/sample_system_web_app_ui/resources/trusted/ash_sample_system_web_app_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [3660],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/sample_system_web_app_ui/resources/untrusted/ash_sample_system_web_app_untrusted_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [3680],
  },
  "ash/webui/scanning/resources/scanning_app_resources.grd": {
    "includes": [3700],
    "structures": [3720],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/system_extensions_internals_ui/ash_system_extensions_internals_resources.grd": {
    "META": {"sizes": {"includes": [10],}},
    "includes": [3740],
  },
  "chromeos/resources/chromeos_resources.grd": {
    "includes": [3760],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/eche_app_ui/ash_eche_app_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [3780],
  },
  # Both ash_eche_bundle_resources.grd and ash_eche_bundle_mock_resources.grd
  # start with the same id because only one of them is built depending on if
  # src_internal is available.
  "ash/webui/eche_app_ui/resources/prod/ash_eche_bundle_resources.grd": {
    "META": {"sizes": {"includes": [120],}},
    "includes": [3800],
  },
  "ash/webui/eche_app_ui/resources/mock/ash_eche_bundle_mock_resources.grd": {
    "META": {"sizes": {"includes": [120],}},
    "includes": [3800],
  },
  "ash/webui/multidevice_debug/resources/multidevice_debug_resources.grd": {
    "META": {"join": 2},
    "includes": [3820],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/personalization_app/resources/ash_personalization_app_resources.grd": {
    "META": {"sizes": {"includes": [200],}},
    "includes": [3840],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/demo_mode_app_ui/ash_demo_mode_app_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
   "includes": [3860],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/projector_app/resources/ash_projector_app_untrusted_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [3880],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/projector_app/resources/ash_projector_app_trusted_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [3900],
  },
  # Both projector_app_bundle_resources.grd and projector_app_bundle_mock_resources.grd
  # start with the same id because only one of them is built depending on if
  # src_internal is available. Lower bound for number of resource ids is number
  # of languages (79).
  "ash/webui/projector_app/resources/prod/projector_app_bundle_resources.grd": {
    "META": {"sizes": {"includes": [120],}}, # Relies on src-internal.
    "includes": [3920],
  },
  "ash/webui/projector_app/resources/mock/projector_app_bundle_mock_resources.grd": {
    "includes": [3920],
  },
  # END chromeos/ section.

  # START components/ section.
  # TODO(b/207518736): Input overlay resources will be changed to proto soon,
  # thus not rushing to update it for now.
  "ash/components/arc/input_overlay/resources/input_overlay_resources.grd": {
    # Big alignment at start of section.
    "META": {"join": 2, "align": 1000},
    "includes": [4000],
  },
  # Chromium strings and Google Chrome strings must start at the same id.
  # We only use one file depending on whether we're building Chromium or
  # Google Chrome.
  "components/components_chromium_strings.grd": {
    "messages": [4020],
  },
  "components/components_google_chrome_strings.grd": {
    "messages": [4020],
  },
  "components/components_locale_settings.grd": {
    "META": {"join": 2},
    "includes": [4040],
    "messages": [4060],
  },
  "components/components_strings.grd": {
    "messages": [4080],
  },
  "components/omnibox/resources/omnibox_pedal_synonyms.grd": {
    "messages": [4100],
  },
  "components/omnibox/resources/omnibox_resources.grd": {
    "includes": [4120],
  },
  "components/policy/resources/policy_templates.grd": {
    "structures": [4140],
  },
  "components/resources/components_resources.grd": {
    "includes": [4160],
  },
  "components/resources/components_scaled_resources.grd": {
    "structures": [4180],
  },
  "components/embedder_support/android/java/strings/web_contents_delegate_android_strings.grd": {
    "messages": [4200],
  },
  "components/autofill/core/browser/autofill_address_rewriter_resources.grd":{
    "includes": [4220]
  },
  # END components/ section.

  # START ios/ section.
  #
  # chrome/ and ios/chrome/ must start at the same id.
  # App only use one file depending on whether it is iOS or other platform.
  "ios/chrome/app/resources/ios_resources.grd": {
    "includes": [400],
    "structures": [420],
  },

  # Chromium strings and Google Chrome strings must start at the same id.
  # We only use one file depending on whether we're building Chromium or
  # Google Chrome.
  "ios/chrome/app/strings/ios_chromium_strings.grd": {
    # Big alignment to make start IDs look nicer.
    "META": {"align": 100},
    "messages": [500],
  },
  "ios/chrome/app/strings/ios_google_chrome_strings.grd": {
    "messages": [500],
  },

  "ios/chrome/app/strings/ios_strings.grd": {
    # Big alignment since strings (previous item) are frequently added.
    "META": {"join": 2, "align": 200},
    "messages": [600],
  },
  "ios/chrome/app/theme/ios_theme_resources.grd": {
    # Big alignment since strings (previous item) are frequently added.
    "META": {"align": 100},
    "structures": [700],
  },
  "ios/chrome/share_extension/strings/ios_share_extension_strings.grd": {
    "messages": [720],
  },
  "ios/chrome/search_widget_extension/strings/ios_search_widget_extension_strings.grd": {
    "messages": [740],
  },
  "ios/chrome/search_widget_extension/strings/ios_search_widget_extension_chromium_strings.grd": {
    "messages": [760],
  },
  "ios/chrome/search_widget_extension/strings/ios_search_widget_extension_google_chrome_strings.grd": {
    "messages": [760],
  },
  "ios/chrome/content_widget_extension/strings/ios_content_widget_extension_chromium_strings.grd": {
    "META": {"join": 2},
    "messages": [780],
  },
  "ios/chrome/content_widget_extension/strings/ios_content_widget_extension_google_chrome_strings.grd": {
    "messages": [780],
  },
  "ios/chrome/credential_provider_extension/strings/ios_credential_provider_extension_strings.grd": {
    "META": {"join": 2},
    "messages": [800],
  },
  # END ios/ section.

  # START ios_internal/ section.
  "ios/chrome/widget_kit_extension/strings/ios_widget_kit_extension_strings.grd": {
    "messages": [820],
  },
  "ios_internal/chrome/app/ios_internal_strings.grd": {
    "messages": [840],
  },
  "ios_internal/chrome/app/theme/mobile_theme_resources.grd": {
    "structures": [860],
  },
  "ios_internal/chrome/app/ios_internal_chromium_strings.grd": {
    "META": {"join": 2},
    "messages": [4240],
  },
  "ios_internal/chrome/app/ios_internal_google_chrome_strings.grd": {
    "messages": [4240],
  },
  # END ios_internal/ section.

  # START content/ section.
  # content/ and ios/web/ must start at the same id.
  "content/content_resources.grd": {
    # Big alignment at start of section.
    "META": {"join": 2, "align": 100},
    "includes": [4300],
  },
  "content/shell/shell_resources.grd": {
    "includes": [4320],
  },
  "content/test/web_ui_mojo_test_resources.grd": {
    "includes": [4340],
  },

  # This file is generated during the build.
  "<(SHARED_INTERMEDIATE_DIR)/content/browser/tracing/tracing_resources.grd": {
    "META": {"sizes": {"includes": [20],}},
    "includes": [4360],
  },
  # END content/ section.

  # START ios/web/ section.
  # content/ and ios/web/ must start at the same id.
  # App only use one file depending on whether it is iOS or other platform.
  "ios/web/ios_web_resources.grd": {
    # Big alignment at start of section.
    "META": {"align": 100},
    "includes": [4300],
  },
  "ios/web/test/test_resources.grd": {
    "includes": [4320],
  },
  # END ios/web/ section.

  # START "everything else" section.
  # Everything but chrome/, chromeos/, components/, content/, and ios/
  "ash/app_list/resources/app_list_resources.grd": {
    # Big alignment at start of section.
    "META": {"join": 2, "align": 100},
    "structures": [4400],
  },
  "ash/ash_strings.grd": {
    "messages": [4420],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/os_feedback_ui/resources/ash_os_feedback_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [4440],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/os_feedback_ui/untrusted_resources/ash_os_feedback_untrusted_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [4460],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/firmware_update_ui/resources/ash_firmware_update_app_resources.grd": {
    "META": {"sizes": {"includes": [200],}},
    "includes": [4480],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/shortcut_customization_ui/resources/ash_shortcut_customization_app_resources.grd": {
    "META": {"sizes": {"includes": [200],}},
    "includes": [4500],
  },
  "ash/shortcut_viewer/shortcut_viewer_strings.grd": {
    "messages": [4520],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ash/webui/shimless_rma/resources/ash_shimless_rma_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [4540],
  },
  "ash/keyboard/ui/keyboard_resources.grd": {
    "includes": [4560],
  },
  "ash/login/resources/login_resources.grd": {
    "structures": [4580],
  },
  "ash/public/cpp/resources/ash_public_unscaled_resources.grd": {
    "includes": [4600],
    "structures": [4620],
  },
  "base/tracing/protos/resources.grd": {
    "includes": [4640],
  },
  "chromecast/app/resources/chromecast_settings.grd": {
    "messages": [4660],
  },
  "chromecast/app/resources/shell_resources.grd": {
    "includes": [4680],
  },
  "chromecast/renderer/resources/extensions_renderer_resources.grd": {
    "includes": [4700],
  },

  "device/bluetooth/bluetooth_strings.grd": {
    "messages": [4720],
  },

  "device/fido/fido_strings.grd": {
    "messages": [4740],
  },

  "extensions/browser/resources/extensions_browser_resources.grd": {
    "structures": [4760],
  },
  "extensions/extensions_resources.grd": {
    "includes": [4780],
  },
  "extensions/renderer/resources/extensions_renderer_resources.grd": {
    "includes": [4800],
    "structures": [4820],
  },
  "extensions/shell/app_shell_resources.grd": {
    "includes": [4840],
  },
  "extensions/strings/extensions_strings.grd": {
    "messages": [4860],
  },

  "mojo/public/js/mojo_bindings_resources.grd": {
    "includes": [4880],
  },

  "net/base/net_resources.grd": {
    "includes": [4900],
  },

  "remoting/resources/remoting_strings.grd": {
    "messages": [4920],
  },

  "services/services_strings.grd": {
    "messages": [4940],
  },
  "skia/skia_resources.grd": {
    "includes": [4960],
  },
  "third_party/blink/public/blink_image_resources.grd": {
    "structures": [4980],
  },
  "third_party/blink/public/blink_resources.grd": {
    "includes": [5000],
  },
  "third_party/blink/renderer/modules/media_controls/resources/media_controls_resources.grd": {
    "includes": [5020],
    "structures": [5040],
  },
  "third_party/blink/public/strings/blink_accessibility_strings.grd": {
    "messages": [5060],
  },
  "third_party/blink/public/strings/blink_strings.grd": {
    "messages": [5080],
  },
  "third_party/libaddressinput/chromium/address_input_strings.grd": {
    "messages": [5100],
  },

  "ui/base/test/ui_base_test_resources.grd": {
    "messages": [5120],
  },
  "ui/chromeos/resources/ui_chromeos_resources.grd": {
    "structures": [5140],
  },
  "ui/chromeos/ui_chromeos_strings.grd": {
    "messages": [5160],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ui/file_manager/file_manager_gen_resources.grd": {
    "META": {"sizes": {"includes": [2000]}},
    "includes": [5180],
  },
  "ui/file_manager/file_manager_resources.grd": {
    "includes": [5200],
  },
  "ui/resources/ui_resources.grd": {
    "structures": [5220],
  },
  "ui/resources/ui_unscaled_resources.grd": {
    "includes": [5240],
  },
  "ui/strings/app_locale_settings.grd": {
    "messages": [5260],
  },
  "ui/strings/ax_strings.grd": {
    "messages": [5280],
  },
  "ui/strings/ui_strings.grd": {
    "messages": [5300],
  },
  "ui/views/examples/views_examples_resources.grd": {
    "messages": [5320],
  },
  "ui/views/resources/views_resources.grd": {
    "structures": [5340],
  },
  "ui/webui/resources/webui_resources.grd": {
    "includes": [5360],
    "structures": [5380],
  },
  "<(SHARED_INTERMEDIATE_DIR)/ui/webui/resources/webui_generated_resources.grd": {
    "META": {"sizes": {"includes": [900]}},
    "includes": [5400],
  },
  "weblayer/weblayer_resources.grd": {
    "includes": [5420],
  },

  # This file is generated during the build.
  # .grd extension is required because it's checked before var interpolation.
  "<(DEVTOOLS_GRD_PATH).grd": {
    # In debug build, devtools frontend sources are not bundled and therefore
    # includes a lot of individual resources
    "META": {"sizes": {"includes": [2000],}},
    "includes": [5440],
  },

  # This file is generated during the build.
  "<(SHARED_INTERMEDIATE_DIR)/resources/inspector_overlay/inspector_overlay_resources.grd": {
    "META": {"sizes": {"includes": [50],}},
    "includes": [5460],
  },

  # END "everything else" section.
  # Everything but chrome/, components/, content/, and ios/

  # Thinking about appending to the end?
  # Please read the header and find the right section above instead.
}
