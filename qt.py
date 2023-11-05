import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QCheckBox, QTextEdit, QLabel, QVBoxLayout, QInputDialog, QSplitter
import subprocess
from PyQt5 import QtWidgets

class UbuntuHardeningApp(QMainWindow):
    def __init__(self, sudo_password):
        super().__init__()
        self.sudo_password = sudo_password

        self.setWindowTitle("Ubuntu Hardening App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.splitter = QSplitter(self.central_widget)
        self.splitter.setGeometry(10, 10, 780, 580)

        self.menu_frame = QWidget(self.splitter)
        self.menu_frame.setStyleSheet("background-color: #f2f2f2; border: 1px solid #dcdcdc; border-radius: 15px;")

        self.output_frame = QTextEdit(self.splitter)
        self.output_frame.setStyleSheet("background-color: black; color: blue; border: 1px solid #dcdcdc; border-radius: 15px;")

        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self.menu_frame)

        ufw_label = QLabel("UFW Configuration", self.menu_frame)
        ufw_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #0078d4; background-color: #eaeaea; border-top-left-radius: 15px; border-top-right-radius: 15px;")

        text_color = "#0078d4"
        style = f"background-color: #f2f2f2; color: {text_color}; padding: 10px;"

        ufw_toggle = QCheckBox("Enable UFW", self.menu_frame)
        ufw_toggle.setChecked(False)  # Set "Enable UFW" to unchecked by default
        incoming_toggle = QCheckBox("Allow Incoming", self.menu_frame)
        outgoing_toggle = QCheckBox("Allow Outgoing", self.menu_frame)
        ssh_toggle = QCheckBox("Allow SSH", self.menu_frame)
        apply_button = QPushButton("Apply Rules", self.menu_frame)
        apply_button.setStyleSheet("background-color: #808080; color: white; padding: 10px; border: none; border-radius: 5px;")
        apply_button.setEnabled(False)  # Disable by default

        update_label = QLabel("System Updates", self.menu_frame)
        update_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #0078d4; background-color: #eaeaea; border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;")
        update_button = QPushButton("Update", self.menu_frame)
        upgrade_button = QPushButton("Upgrade", self.menu_frame)

        for label in [ufw_label, update_label]:
            label.setStyleSheet(style)

        for item in [ufw_toggle, incoming_toggle, outgoing_toggle, ssh_toggle, update_button, upgrade_button]:
            item.setStyleSheet(style)
            item.installEventFilter(self)  # Install an event filter to handle hover events

        layout.addWidget(ufw_label)
        layout.addWidget(ufw_toggle)
        layout.addWidget(incoming_toggle)
        layout.addWidget(outgoing_toggle)
        layout.addWidget(ssh_toggle)
        layout.addWidget(apply_button)
        layout.addWidget(update_label)
        layout.addWidget(update_button)
        layout.addWidget(upgrade_button)

        ufw_toggle.stateChanged.connect(self.toggle_ufw)
        apply_button.clicked.connect(self.configure_ufw_rules)
        update_button.clicked.connect(self.run_update)
        upgrade_button.clicked.connect(self.run_upgrade)

        # Set object names for the checkboxes
        incoming_toggle.setObjectName("AllowIncoming")
        outgoing_toggle.setObjectName("AllowOutgoing")
        ssh_toggle.setObjectName("AllowSSH")

        self.ufw_toggle = ufw_toggle
        self.apply_button = apply_button

    def eventFilter(self, source, event):
        # Handle hover events to change the background color
        if event.type() == event.Enter:
            source.setStyleSheet("background-color: #d3d3d3; color: #0078d4; padding: 10px;")
        elif event.type() == event.Leave:
            source.setStyleSheet("background-color: #f2f2f2; color: #0078d4; padding: 10px;")

        return super().eventFilter(source, event)

    def toggle_ufw(self, state):
        ufw_status = state
        command = "sudo ufw enable" if ufw_status else "sudo ufw disable"
        self.run_command_with_sudo(command)
        # Enable the "Apply Rules" button when the "Enable UFW" toggle is checked
        self.apply_button.setEnabled(ufw_status)
        if ufw_status:
            self.apply_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px;")
        else:
            self.apply_button.setStyleSheet("background-color: #808080; color: white; padding: 10px; border: none; border-radius: 5px;")

    def configure_ufw_rules(self):
        rules = []

        # Find checkboxes by objectName
        incoming_checkbox = self.menu_frame.findChild(QCheckBox, "AllowIncoming")
        outgoing_checkbox = self.menu_frame.findChild(QCheckBox, "AllowOutgoing")
        ssh_checkbox = self.menu_frame.findChild(QCheckBox, "AllowSSH")

        if incoming_checkbox.isChecked():
            rules.append("sudo ufw default allow incoming")
        else:
            rules.append("sudo ufw default deny incoming")

        if outgoing_checkbox.isChecked():
            rules.append("sudo ufw default allow outgoing")
        else:
            rules.append("sudo ufw default deny outgoing")

        if ssh_checkbox.isChecked():
            rules.append("sudo ufw allow ssh")
        else:
            rules.append("sudo ufw delete allow ssh")

        for rule in rules:
            self.run_command_with_sudo(rule)

    def run_command_with_sudo(self, command):
        try:
            command = f'echo {self.sudo_password} | sudo -S {command}'
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            stdout, stderr = process.communicate()

            if process.returncode == 0:
                self.output_frame.append(stdout)
                QtWidgets.QMessageBox.information(self, "Success", f"Command executed successfully: {command}")
            else:
                self.output_frame.append(stderr)
                QtWidgets.QMessageBox.critical(self, "Error", f"Error executing command: {command}")

        except subprocess.CalledProcessError as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error executing command: {e.stderr}")

    def run_update(self):
        self.run_command_with_sudo("sudo apt update")

    def run_upgrade(self):
        self.run_command_with_sudo("sudo apt upgrade -y")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sudo_password, _ = QInputDialog.getText(None, "Sudo Password", "Please enter your sudo password:", QtWidgets.QLineEdit.Password)
    if sudo_password:
        hardening_app = UbuntuHardeningApp(sudo_password)
        hardening_app.show()
        sys.exit(app.exec_())
