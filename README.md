# Cowrie Honeypot Auto Installer
This repository contains a Python script that automates the installation of the Cowrie Honeypot on Debian/Ubuntu-based systems.
It installs all necessary dependencies, sets up a dedicated user, clones the official Cowrie repository, creates a Python virtual environment, and configures Cowrie for quick startup.

# Features 
One-command Cowrie installation

Automatic dependency setup

Creates a secure, dedicated cowrie user

Sets up a Python virtual environment and installs required packages

Prepares Cowrie configuration for immediate use

# After installing

To start and check the status of cowrie run the following
sudo su - cowrie
cd cowrie
bin/cowrie start
bin/cowrie status

# Need Help?

If you get stuck, are confused, or want to explore more advanced features, please visit the official Cowrie documentation:
https://docs.cowrie.org/en/latest/README.html

# Disclaimer

I did not create nor do I own Cowrie. This script simply automates the installation process to help others deploy it more easily.
All credit for the Cowrie project goes to the official maintainers.
Visit the official GitHub repo at https://github.com/cowrie/cowrie for source code and contribution details.
