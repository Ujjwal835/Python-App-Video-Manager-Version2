import sqlite3

# connecting a database
conn=sqlite3.connect('youtube_videos.db')

cursor=conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print("*"*70)
    for row in cursor.fetchall():
        print(row)
    print("*"*70)
def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES (?,?)",(name,time))
    conn.commit()
    print("***** Video Added Successfully *****")
def update_video(video_id):
    cursor.execute("SELECT id FROM videos WHERE id=?", (video_id,))
    result = cursor.fetchone()
    if result:
        new_name=input("Enter The Video Name: ")
        new_time=input("Enter The Video Time: ")
        cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
        conn.commit()
        print("***** Details Updated Successfully *****")
    else:
        print("Error: Video ID not found. Please provide a valid video ID.")
def delete_video(video_id):
    cursor.execute("SELECT id FROM videos WHERE id=?", (video_id,))
    result = cursor.fetchone()
    if result:
        cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
        conn.commit()
        print("***** Video Deleted Successfully *****")
    else:
        print("Error: Video ID not found. Please provide a valid video ID.")
def main():
    while True:
        print("\n\t\t Youtube Manager App with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice=input("Enter Your Choice : ")
        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter The Video Name: ")
            time=input("Enter The Video Time: ")
            add_video(name,time)
        elif choice=='3':
            video_id=input("Enter The Video ID to Update: ")
            
            update_video(video_id)
        elif choice=='4':
            video_id=input("Enter The Video ID to Delete: ")
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid Choice !!!")

    # closing the db connection so that the database dont get corrupt
    conn.close()

if __name__=="__main__":
    main()
