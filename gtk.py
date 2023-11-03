import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyApplication(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("My Modern App")
        self.set_default_size(800, 400)
        self.connect("destroy", Gtk.main_quit)

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(False)  # Allow columns to have different widths

        # Create the three columns as frames
        self.column1 = Gtk.Frame()
        self.column2 = Gtk.Frame()
        self.column3 = Gtk.Frame()

        # Set labels for the frames
        self.column1.set_label("Features")
        self.column2.set_label("Options")
        self.column3.set_label("Output Window")

        # Create a box for each column
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Set margins for the boxes (added for padding)
        margin = 10
        self.box1.set_margin_top(margin)
        self.box1.set_margin_bottom(margin)
        self.box1.set_margin_start(margin)
        self.box1.set_margin_end(margin)

        self.box2.set_margin_top(margin)
        self.box2.set_margin_bottom(margin)
        self.box2.set_margin_start(margin)
        self.box2.set_margin_end(margin)

        self.box3.set_margin_top(margin)
        self.box3.set_margin_bottom(margin)
        self.box3.set_margin_start(margin)
        self.box3.set_margin_end(margin)

        # Create buttons for the "Features" column
        self.button1 = Gtk.Button(label="Firewall Configuration")
        self.button2 = Gtk.Button(label="Patch Management")

        # Add buttons to the "Features" column
        self.box1.pack_start(self.button1, False, False, 5)
        self.box1.pack_start(self.button2, False, False, 5)

        # Add boxes to the columns
        self.column1.add(self.box1)
        self.column2.add(self.box2)
        self.column3.add(self.box3)

        # Add borders around the content of the columns
        self.column1.set_border_width(5)
        self.column2.set_border_width(5)
        self.column3.set_border_width(5)

        # Add columns to the grid
        self.grid.attach(self.column1, 0, 0, 1, 1)
        self.grid.attach(self.column2, 1, 0, 1, 1)
        self.grid.attach(self.column3, 2, 0, 2, 1)  # The "Output Window" column occupies two columns

        self.add(self.grid)

        # Connect to the "size-allocate" signal to adjust column sizes when the window is resized
        self.connect("size-allocate", self.on_size_allocate)

        # Connect the "clicked" signal of the "Firewall Configuration" button to update the "Options" column
        self.button1.connect("clicked", self.on_firewall_configuration_clicked)

    def on_size_allocate(self, widget, allocation):
        # Calculate and set the sizes of the columns based on the window's size
        total_width = allocation.width
        column1_width = total_width * 0.25  # 25% of the window width
        column2_width = total_width * 0.30  # 30% of the window width
        column3_width = total_width * 0.45  # 45% of the window width

        self.column1.set_size_request(column1_width, -1)
        self.column2.set_size_request(column2_width, -1)
        self.column3.set_size_request(column3_width, -1)

    def on_firewall_configuration_clicked(self, widget):
        # Clear the existing content of the "Options" column
        for child in self.box2.get_children():
            self.box2.remove(child)

        # Create labels and toggle switches for the firewall configuration options
        enable_firewall_label = Gtk.Label(label="Enable Firewall")
        allow_incoming_label = Gtk.Label(label="Allow Incoming")
        allow_outgoing_label = Gtk.Label(label="Allow Outgoing")
        allow_ssh_label = Gtk.Label(label="Allow SSH")

        # Create a Grid to organize the option names and toggle switches
        grid = Gtk.Grid()
        grid.set_column_homogeneous(True)  # Make columns have equal width

        # Create a column for option names (80%)
        name_column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        name_column.pack_start(enable_firewall_label, False, False, 5)
        name_column.pack_start(allow_incoming_label, False, False, 5)
        name_column.pack_start(allow_outgoing_label, False, False, 5)
        name_column.pack_start(allow_ssh_label, False, False, 5)

        # Create a column for toggle switches (20%)
        switch_column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        enable_firewall_toggle = Gtk.Switch()
        allow_incoming_toggle = Gtk.Switch()
        allow_outgoing_toggle = Gtk.Switch()
        allow_ssh_toggle = Gtk.Switch()

        # Reduce the height and width of the toggle switches by 25%
        toggle_size_reduction = 0.75  # 25% reduction
        toggle_width = int(enable_firewall_toggle.get_size_request()[0] * toggle_size_reduction)
        toggle_height = int(enable_firewall_toggle.get_size_request()[1] * toggle_size_reduction)

        enable_firewall_toggle.set_size_request(toggle_width, toggle_height)
        allow_incoming_toggle.set_size_request(toggle_width, toggle_height)
        allow_outgoing_toggle.set_size_request(toggle_width, toggle_height)
        allow_ssh_toggle.set_size_request(toggle_width, toggle_height)

        switch_column.pack_start(enable_firewall_toggle, False, False, 5)
        switch_column.pack_start(allow_incoming_toggle, False, False, 5)
        switch_column.pack_start(allow_outgoing_toggle, False, False, 5)
        switch_column.pack_start(allow_ssh_toggle, False, False, 5)

        # Set padding for the Grid
        grid.set_column_spacing(5)

        # Set the width proportions for the columns within the grid
        grid.attach(name_column, 0, 0, 8, 1)  # Name column takes 8 parts (80%)
        grid.attach(switch_column, 8, 0, 2, 1)  # Switch column takes 2 parts (20%)

        # Create a "Save" button
        save_button = Gtk.Button(label="Save")
        save_button.set_margin_top(10)

        # Add the Grid and the "Save" button to the "Options" column
        self.box2.pack_start(grid, False, False, 5)
        self.box2.pack_start(save_button, False, False, 5)

        # Show all the newly added elements
        self.box2.show_all()

if __name__ == "__main__":
    app = MyApplication()
    app.show_all()
    Gtk.main()
