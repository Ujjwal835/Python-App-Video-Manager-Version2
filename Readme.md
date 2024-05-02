Description

This Python application allows users to manage YouTube video records using a SQLite database backend. Users can perform basic CRUD (Create, Read, Update, Delete) operations on video records, including listing all videos, adding new videos, updating existing video details, and deleting videos.

Features

List Videos: Display all videos stored in the database.
Add Videos: Add new videos to the database by providing the name and time.
Update Videos: Modify the details of existing videos by providing the video ID, new name, and new time.
Delete Videos: Remove videos from the database by specifying the video ID.
Error Handling: Provides feedback to users for invalid inputs or non-existent video IDs.

Requirements

Python 3.x
SQLite3

Installation

1. Clone the repository:
   > > git clone https://github.com/Ujjwal835/Python-App-Video-Manager-Version2
2. Navigate to the project directory:
   > > cd Python-App-Video-Manager-Version2
3. Install dependencies (SQLite3 is included in Python standard library).

Usage

1. Run the application:

   > > python youtube_video_manager.py

2. Follow the on-screen instructions to perform desired operations:
   > > Choose from the available options to list videos, add videos, update videos, delete videos, or exit the application.
   > > Provide necessary inputs when prompted.

Example:

        Youtube Manager App with DB

1. List Videos
2. Add Videos
3. Update Videos
4. Delete Videos
5. Exit App
   Enter Your Choice : 1

---

(1, 'Video 1', '10:30')
(2, 'Video 2', '15:45')

---

Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your proposed changes.
