

def create_yt_video(title,description):
	my_dictionary={"title": title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return my_dictionary

def like(dictionary):
	if "likes" in dictionary:
		dictionary["likes"]+=1
	return dictionary

def dislike(dictionary):
	if "dislikes" in dictionary:
		dictionary["dislikes"]+=1
	return dictionary

def add_comment(yt_video,username,comment_text):
	yt_video["comments"]["username"]=username
	yt_video["comments"]["comment_text"]=comment_text



video=create_yt_video("funny video","funny description")
print(video)
add_comment(video,"Munir","amazing")
print(video)


