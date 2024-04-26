app_name = "al_sulati"
app_title = "Al Sulati"
app_publisher = "Hybrowlabs Technologies"
app_description = "Al Sulati Customisations"
app_email = "grawish@hybrowlabs.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

fixtures = [
    {
        "dt": "Print Format",
        "filters": [
            ["name", "in", ["Quotation Custom"]]
        ],
    },
    {
        "doctype":"Client Script",
        "or_filters": [
           {"name": "EMPLOYEE OPERATOR(Status)"},
           {"name": "Quotation signature"},
           {"name": "Sales Order Amount"},
           {"name": "sales order button"},
           {"name":"project Connection Removal"},
           {"name":"Project rate and type"},
           {"name":"Engagement Record Fetch"},
           {"name":"Serial Filtering Custom"},
           {"name":"Serial No Fetch"}
        ],
    }
]

# include js, css files in header of desk.html
# app_include_css = "/assets/al_sulati/css/al_sulati.css"
# app_include_js = "/assets/al_sulati/js/al_sulati.js"

# include js, css files in header of web template
# web_include_css = "/assets/al_sulati/css/al_sulati.css"
# web_include_js = "/assets/al_sulati/js/al_sulati.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "al_sulati/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Purchase Receipt": "public/js/purchase_receipt.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "al_sulati/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "al_sulati.utils.jinja_methods",
# 	"filters": "al_sulati.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "al_sulati.install.before_install"
# after_install = "al_sulati.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "al_sulati.uninstall.before_uninstall"
# after_uninstall = "al_sulati.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "al_sulati.utils.before_app_install"
# after_app_install = "al_sulati.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "al_sulati.utils.before_app_uninstall"
# after_app_uninstall = "al_sulati.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "al_sulati.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
#     "Purchase Receipt": {
#         "on_update": "al_sulati.al_sulati.doc_events.purchase_receipt.on_update",
#     },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"al_sulati.tasks.all"
# 	],
# 	"daily": [
# 		"al_sulati.tasks.daily"
# 	],
# 	"hourly": [
# 		"al_sulati.tasks.hourly"
# 	],
# 	"weekly": [
# 		"al_sulati.tasks.weekly"
# 	],
# 	"monthly": [
# 		"al_sulati.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "al_sulati.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "al_sulati.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "al_sulati.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["al_sulati.utils.before_request"]
# after_request = ["al_sulati.utils.after_request"]

# Job Events
# ----------
# before_job = ["al_sulati.utils.before_job"]
# after_job = ["al_sulati.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"al_sulati.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

