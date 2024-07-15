def create_youtube_video(title, description):
    youtube_video = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}
    }
    return youtube_video

def like(youtube_video):
	if "like" in youtube_video:
		youtube_video["like"] +=1
	return youtube_video
def dislike(youtube_video):
	if "dislikes" in youtube_video:
		    youtube_video["dislikes"] += 1
	return youtube_video

def add_comment(youtube_video,username,comment_text):
	youtube_video["comments"][username]=comment_text
	return youtube_video



new_youtube= create_youtube_video("0OP 101 with Loai!", "This tutorial helps you successfully review most of the material learned so far in Y1 Summer and Yearlong, so we can start the Y2 Summer super strong and elevate you to a whole new level in CS by the end of the summer!!!")
new_youtube_= add_comment(new_youtube, "Loai", "YO000 first video ya'11! Fame, here we come")
new_youtube = add_comment(new_youtube, "Lyel", "Thanks! Been looking for something like this for so long.")
for _ in range(495):
     new_youtube = like(new_youtube)
for _ in range(123):
     new_youtube = dislike(new_youtube)
new_youtube = dislike(new_youtube)
print(f"Title: {new_youtube['title']}")
print(f"Description: {new_youtube['description']}")
print(f"{new_youtube['likes']} people liked this :)")
print(f"{new_youtube['dislikes']} people disliked this :(")
print("\nComments:")
for username, comment in new_youtube['comments'].items():
    print(f"{username}: {comment}")