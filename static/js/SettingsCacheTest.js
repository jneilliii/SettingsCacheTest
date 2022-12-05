$(function() {
	function SettingsCacheTestViewModel(parameters) {
		var self = this;

		self.settingsViewModel = parameters[0];
		
		self.onEventSettingsUpdated = function (payload) {
			console.log(payload);
			console.log(ko.toJSON(self.settingsViewModel.settings.plugins.SettingsCacheTest));
		}
    };

	OCTOPRINT_VIEWMODELS.push({
		construct: SettingsCacheTestViewModel,
		dependencies: ["settingsViewModel"],
		elements: ["#settings_plugin_SettingsCacheTest"]
	});
});
