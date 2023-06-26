## mySite - Dynamic Personal Website

mySite is a dynamic personal website project that aims to showcase information about you, your projects, and provide an introduction to your online presence. This project is built using Django, a high-level Python web framework, which provides a robust and scalable foundation for web application development.

## Features
About Me: Displays information about you, including a brief bio, skills, and interests.
Projects: Showcases your notable projects, including descriptions, images, and links.
Blog: Allows you to write and publish blog posts about various topics.
Contact: Provides a means for visitors to get in touch with you via a contact form.

## Installation

Clone the repository:
shell
git clone https://github.com/your-username/mySite.git
Change into the project directory:
shell
cd mySite
Create and activate a virtual environment (optional, but recommended):
shell
python -m venv env
source env/bin/activate
Install the project dependencies:
shell
pip install -r requirements.txt
Apply the database migrations:
shell
python manage.py migrate
Start the development server:
shell
python manage.py runserver
Open your web browser and visit http://localhost:8000 to see the website in action.

## Configuration

Customize the content:
Update the information in the templates located in the personal/templates/personal/ directory to reflect your own bio, skills, project details, etc.
Add your own project images to the personal/static/personal/images/ directory.
Modify the CSS styles in the personal/static/personal/css/ directory to customize the website's appearance.
Configure email settings:
If you plan to use the contact form, set up your email backend configuration in the settings.py file.
Deploy to a production environment:
Update the DEBUG setting in the settings.py file to False.
Configure a production-ready web server, such as Apache or Nginx, to serve the application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit an issue or a pull request.

## Contact

For any inquiries or questions, feel free to contact me at CameronGunn012@gmail.com.

