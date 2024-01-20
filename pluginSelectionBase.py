from pluginLoader import plugin_loader
import gradio as gr


class Provider():
    plugin = None
    name = ""
    ui = None


class PluginSelectionBase():
    provider_list = []
    current_plugin = None

    def __init__(self, plugin_type) -> None:
        # load plugin
        self.plugin_type = plugin_type
        self.category_name = plugin_loader.interface_to_category[self.plugin_type]
        for plugin in plugin_loader.plugins[self.category_name]:
            provider = Provider()
            provider.plugin = plugin
            provider.name = plugin.__class__.__name__
            self.provider_list.append(provider)
        self.default_provider = self.provider_list[0]  # todo load from save
        self.current_plugin = self.default_provider.plugin
        for provider in self.provider_list:
            self.load_provider(provider.name)

    # Creates the dropdown menu for selecting current plugin
    def create_plugin_selection_ui(self):
        self.provider_dropdown = gr.Dropdown(

            choices=[provider.name for provider in self.provider_list],
            value=self.default_provider.name,
            type="value",
            label="Provider: ",
            info="",
            interactive=True)
        self.provider_dropdown.change(
            self.on_dropdown_change, inputs=self.provider_dropdown)

    # Creates the custom UI from each plugin
    def create_plugin_ui(self):
        for provider in self.provider_list:
            provider.ui = provider.plugin.create_ui()

    def on_dropdown_change(self, provider_name):
        self.current_plugin = self.find_provider_by_name(
            self.provider_list, provider_name).plugin

    def load_provider(self, provider_name):
        # print(f"Loading {self.plugin_type} Module...")
        # print(f"Looking for {provider_name} in installed plugins...")
        found_provider = self.find_provider_by_name(
            self.provider_list, provider_name)
        # print(f"Found {found_provider} .")
        if issubclass(type(found_provider.plugin), self.plugin_type):
            found_provider.plugin.init()

            # return self.hide_other_ui(provider_name)

    # Gradio doesn't support dynamic showing/hiding of elements
    # def hide_other_ui(self, provider_name):
    #     for provider in self.provider_list:
    #         print(
    #             f"updating {provider.name} to {provider.name == provider_name}")
    #         provider.ui = provider.name == provider_name
    #     return [provider.ui for provider in self.provider_list]

    def find_provider_by_name(self, providers, name):
        for provider in providers:
            if provider.name == name:
                return provider
        return None