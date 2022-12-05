# coding=utf-8

import octoprint.plugin


class SettingsCacheTest(octoprint.plugin.SettingsPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.StartupPlugin, octoprint.plugin.AssetPlugin):
	def __init__(self):
		pass

	def on_after_startup(self):
		self._logger.info("Settings Cache Test Loaded")

	def get_template_configS(self):
		return [{"type": "settings", "custom_bindings": False}]

	def get_settings_defaults(self):
		return {"setting1": "setting1 value"}

	def on_settings_save(self, data):
		self._logger.info(self._settings.get([],merged=True, asdict=True))
		data["setting2"] = "setting2 value"
		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
		self._logger.info(self._settings.get([],merged=True, asdict=True))

	def get_assets(self):
		return dict(
			js=["js/SettingsCacheTest.js"]
		)

__plugin_name__ = "Settings Cache Test"
__plugin_pythoncompat__ = ">=3,<4"
__plugin_version__ = "0.1.0"
__plugin_implementation__ = SettingsCacheTest()