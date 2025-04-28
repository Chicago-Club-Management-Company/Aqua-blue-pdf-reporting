# Use Ubuntu 20.04 (Focal) to have access to libssl1.1.
FROM ubuntu:20.04

# Disable interactive prompts during package installation.
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install prerequisites needed for wkhtmltopdf.
RUN apt-get update && apt-get install -y \
    wget \
    libssl1.1 \
    libjpeg-turbo8 \
    libxrender1 \
    xfonts-base \
    xfonts-75dpi \
    fontconfig \
    libxext6 \
  && rm -rf /var/lib/apt/lists/*

# Download and install wkhtmltopdf 0.12.6 by using the focal package.
# (Make sure the URL below is correct; check the official releases page)
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb
RUN dpkg -i wkhtmltox_0.12.6-1.focal_amd64.deb
RUN rm wkhtmltox_0.12.6-1.focal_amd64.deb

# Set the working directory. When mounting your repository,
# this is where your HTML files and output PDFs will reside.
WORKDIR /data

# By default, print the installed version (override this command when running).
CMD ["wkhtmltopdf", "--version"]
