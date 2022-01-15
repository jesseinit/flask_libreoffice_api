# LibreOffice REST API

This project is a Stateless REST API that exposes an endpoint for document conversion using the LibreOffice CLI.

# Motivation

The motivation for this project was from the issues experienced from another service I was using at work for the same purpose, it had a large memory footprint on our clusters as a result of some zombie processes cause memory leakages.

# Getting Started

1. Ensure you have docker running and enough resources(atleast 2GB RAM) allocated to it.
2. Build image with `docker build -t libreoffice_rest .`
3. Start container with `docker run --name libreoffice_rest --rm -p 3000:3000 libreoffice_rest`

# Accessing Endpoints

There are three endpoint exposed on the project and they are as follows

- GET `/health` - Returns a message on how so up we are..lol
- GET `/` - Returns a greeting message..hehe
- POST `/forms/libreoffice/convert` - Takes a multipart form request and returns the converted file.

  Example Request

  ```curl
  curl --location --request POST 'http://0.0.0.0:3000/forms/libreoffice/convert' --form 'files=@"/Users/jesseinit/Downloads/DesignProcessWorkshopbySlidesgo.pptx"'
  ```

## Todo

Feel free to open an issue or a PR for any of the todos below or other improvements.

- [ ] Support Non-root user
- [ ] Support Other document types conversion
- [ ] Reduce docker image size
- [ ] Miscellaneous Gunicorn configuration fine-tunning
