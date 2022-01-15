# LibreOffice REST API

This project is a Stateless REST API that exposes an endpoint for document conversion using the LibreOffice CLI.

# Motivation

The motivation for this project was from the issues experienced from another service I was using at work for the same purpose, it had a large memory footprint on our clusters as a result of some zombie processes thereby leading to memory leakages.

Before Implementation
![image](https://user-images.githubusercontent.com/13919080/149616920-c5c04f57-1efb-4f1d-843f-5d4a1caa08e2.png)

After Implementation
![Screen Shot 2022-01-15 at 9 47 37 AM](https://user-images.githubusercontent.com/13919080/149616946-c6fc843c-af1c-48b8-adf0-fadd22ebd50f.png)

😇


# Getting Started

1. Ensure you have docker running and enough resources(atleast 2GB RAM) allocated to it.
2. Build image with `docker build -t libreoffice_rest .`
3. Start container with `docker run --name libreoffice_rest --rm -p 3000:3000 libreoffice_rest`

# Accessing Endpoints

There are three endpoint exposed on the project and they are as follows

- GET `/health` - Returns a message on how so uppp we are..lol
- GET `/` - Returns a greeting message..hehe
- POST `/forms/libreoffice/convert` - Takes a multipart form request and returns the converted file.

  Example Request

  ```curl
  curl --location --request POST 'http://0.0.0.0:3000/forms/libreoffice/convert' --form 'files=@"/Users/jesseinit/Downloads/DesignProcessWorkshopbySlidesgo.pptx"'
  ```

## Todo

Feel free to open an issue or a PR for any of the todos below or other improvements.

- [ ] Implement non-root user in the docker image
- [ ] Support other document type conversion
- [ ] Reduce docker image size
- [ ] Optimise how the subprocess is called
- [ ] Add logging and increased granularity
- [ ] Miscellaneous Gunicorn configuration fine-tunning
