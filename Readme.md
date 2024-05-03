# YouTube Manager Application with SQLite

This Python application allows users to manage their YouTube videos using an SQLite database. Users can perform CRUD (Create, Read, Update, Delete) operations on their videos through a simple command-line interface.

# Features 

1. List Videos: Display all videos stored in the database.
2. Add Videos: Add new videos to the database by providing the name and time.
3. Update Videos: Modify the details of existing videos by providing the video ID, new name, and new time.
4. Delete Videos: Remove videos from the database by specifying the video ID.
5. Error Handling: Provides feedback to users for invalid inputs or non-existent video IDs.

## Requirements

- Python 3.x
- SQLite3

## Setup

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. No additional installations are required, as SQLite is included with Python.

## Installation

1. Clone the repository:
   > > git clone https://github.com/Ujjwal835/Python-App-Video-Manager-Version2
2. Navigate to the project directory:
   > > cd Python-App-Video-Manager-Version2
3. Install dependencies (SQLite3 is included in Python standard library).


## Usage

1. Run the `youtube_manager_db.py` file using Python.
2. Follow the prompts to perform various operations:
   - List Videos: View all videos in the database.
   - Add Videos: Add a new video to the database.
   - Update Videos: Update the details of an existing video.
   - Delete Videos: Delete a video from the database.
   - Exit App: Terminate the application.

## Notes

- Videos are stored in an SQLite database named `youtube_videos.db`.
- Each video has an auto-incrementing ID, a name, and a time field.
- Video details can be updated by providing the video ID.
- Videos can be deleted by providing the video ID.

## Contributors

- Ujjwal Jindal- ujjwaljindal835@gmail.com

Feel free to contribute to this project by forking the repository and submitting pull requests with improvements or additional features.
