# PG Finder

PG Finder is a web application designed to help users find Paying Guest (PG) accommodations, roommates, tiffin services, and local events. Built with Flask, Bootstrap, and SQLite, it provides a user-friendly interface for searching and listing PGs and related services.

## Features
- Browse PG listings
- Find and connect with roommates
- Discover tiffin (meal) services
- View and post local events
- Responsive design with Bootstrap

## Project Structure
```
projecthehai1026/
├── app.py                # Main Flask application
├── models/               # Database models
│   └── models.py
├── static/               # Static files (CSS, images)
│   ├── css/
│   │   └── style.css
│   └── images/
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── listings.html
│   ├── roommates.html
│   ├── tiffin.html
│   ├── events.html
│   └── details.html
├── instance/
│   └── site.db           # SQLite database
├── requirements.txt      # Python dependencies
├── seed_data.py          # Script to seed the database
├── test_flask.py         # Test file
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pgfinder.git
   cd pgfinder
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - The SQLite database (`site.db`) is included in the `instance/` folder. If you need to reset or seed the database, run:
     ```bash
     python seed_data.py
     ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. 