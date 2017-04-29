# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "quality"
app_title = "Quality"
app_publisher = "Mayur"
app_description = "Quality Analysis"
app_icon = "octicon octicon-check"
app_color = "#1760da"
app_email = "mayur@mittalclothing.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/quality/css/quality.css"
# app_include_js = "/assets/quality/js/quality.js"

# include js, css files in header of web template
# web_include_css = "/assets/quality/css/quality.css"
# web_include_js = "/assets/quality/js/quality.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "quality.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "quality.install.before_install"
# after_install = "quality.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "quality.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"quality.tasks.all"
# 	],
# 	"daily": [
# 		"quality.tasks.daily"
# 	],
# 	"hourly": [
# 		"quality.tasks.hourly"
# 	],
# 	"weekly": [
# 		"quality.tasks.weekly"
# 	]
# 	"monthly": [
# 		"quality.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "quality.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "quality.event.get_events"
# }

