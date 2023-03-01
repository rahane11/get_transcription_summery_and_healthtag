import os
import requests
import json

#define required variable which required to access api
access_token = "eyJ4NXQiOiJZV0poTVdaa1l6WXhZekpqTVRWbE9EUXdOREF5WkdObVpqZ3pNRE5pWmpaa05qa3lNalprWVEiLCJraWQiOiJabVkzWkRneU5qQmlaREJqTXpNNVltWmtaVGRqTldZNVpqZGpaamswT0dKbU9UTXlPR1ExTmprMU16TTJPVFE1TnprMk5UZGpZV1ZpTURJNE1qRTJOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJhZG1pbiIsImF1dCI6IkFQUExJQ0FUSU9OIiwiYXVkIjoiWWZERHZzX0RmUmphZVliQVZpZ2RTeUhnOHQwYSIsIm5iZiI6MTY3NzE0ODg2MCwiYXpwIjoiWWZERHZzX0RmUmphZVliQVZpZ2RTeUhnOHQwYSIsInNjb3BlIjoiZGVmYXVsdCIsImlzcyI6Imh0dHBzOlwvXC8xMy45MC4yNDIuNzA6OTQ0M1wvb2F1dGgyXC90b2tlbiIsImV4cCI6OTIyMzM3MjAzNjg1NDc3NSwiaWF0IjoxNjc3MTQ4ODYwLCJqdGkiOiI1OWExMDA5ZS00YjY5LTQyZjctOGVlYy1hY2MxYjAwNTEzZDIifQ.Rv4cocGnSmgBZDRMh8aIl4XLQno0jqELpnCE7vqVXLz3UMP3r_fWjMiZ90B3qxWAVtd5ubk1R6OMfZEPw6DoHp5c53hr9zN01KPu6A7ua3Lxeps77Y3mQJ5Nw11dtFyi3IIhIP1wDX3oU7cHSpedSLpiRtGJrJQX13uuyvetEh3YrVlO0O92Jucfl41dQe2J6oy43FgLEv7EH8eykLsC35p3Os_P5fndjtSkjSp_dq_PA0ZEJlG6ZS9Dlmy_78zueAvPWjZ_tuVNUjoveBYedkVRqeepfZ_xf54a0gcMbYLHKUR35Sqnm8cb6WxjDwXMinXlhZQWBE8Ccx_ziOJjCw"
url_for_transcript_api = "http://127.0.0.1:8000/whisper"
url_for_textsummerize_api = "http://52.188.68.191:5008/summerize"

url_for_healthtag = "https://auto-tagger.azurewebsites.net/api/healthtag"


text = '''Oh, hello. Hi. You look lovely today and you're not wearing a mask so I would presume Sam is not beside you. That's true. That's what I call to tell you. I think he's going to show. He didn't call me back either time I left message as and the office hadn't seen him for a while. I don't know what to do with him. Um, probably. We need to probably send him, you know, I sent you that release of information. Yeah. Can we send it by certified mail to show that he received it? Yeah, I can see if they can do that in the office. And I will write you a letter that says on my letter head on that you can include with it. Okay. You've not followed up and I'll sort of outline what's happened and the importance of being treated. And we need to talk and unfortunately there is a state health department guideline and I don't know what their time frame is. But if he's off meds much longer, they're not going to do anything for him. Yeah. And he's not going to see Dr. George. I mean, she's not going to treat him. So, yeah, she's kind of done. Treat him until I sign up on him. Right. Yeah. If I can't get to take the meds, then I'm sort of out of luck. So, yeah. I don't know. He's just, he marches to his own beat and he's pretty red neck. And I mean, the message on his phone is like, it's a Sam. Lock and load. Leave me a message. I'm like. Really? Lovely. Yeah. So, I mean, and I know he probably has PTSD and stuff from being in the war and everything. But I would think you hurt that you would want to be treated. I would. And my bad is he doesn't understand the difference between this time and the last time he was on Humero. Yeah. He does. That this is just a whole bunch of rigamarald and one more layer. And yeah, probably I'm out to make money off of him. Yeah, you probably are. Yeah. They forget to bill like for a year at a time at free state for me. Yeah. That'll be my retirement. I tell them I'm looking forward to it. Yeah. Yeah. So, what I will do is I think actually I can, I think I can do on that PDF form. I think I can fill in the blanks. Okay. So, let me try to fill in the blanks and then I will email them to you. Okay. So, I'll fill out that form as much as I can and and I will write a cover letter explaining this is what we've done. This is what we need to do. Please call us at your earliest convenience. So, I can see you. You know, as I'm going to sign it's less likely that we'll be able to do anything to help. Okay. Sounds good. Sorry. You know, it's been one of those days. So you wouldn't hear my exciting day so far. Yeah. Oh, I happened to your dog. Well, it's just so I had one aunt die and I went to her funeral last week. I had another aunt die of COVID. I'm going to her funeral in Michigan tomorrow. I'm sorry. My brother is supposed to watch my dogs, but she has to go somewhere out of town. So the person who always watches our dogs, her sister lined it up in the ICU yesterday. So she can't watch our dogs. And it turns out me of all people, the one who preaches vaccines day and night. I forgot to get my dog vaccinated. So he couldn't go to the kettle. So I took him in this morning to get him vaccinated. Which makes life even more exciting last night when we are opening the garage to put my husband's car in the garage because mine is in the shop. Our garage door broke. Oh, God. Off the hinges. So I can't get in or out of the garage. So this morning I locked myself out of the car twice and out of the house twice. Oh. Lovely. Yeah. You've had a good day. Good. Good. I'm looking forward to the third things I can say I'm done. Yeah. Really. I know. I know. All right. Anything else we need to do with any of our other patients? No, Dr. George. You don't want to see Barnett. I need to talk to him. I'm going to call him and see if he said his. Um. Aspiration again because I haven't gotten any reports. You know, and I haven't heard from the health department. They were supposed to call me last Thursday about that. Okay. Okay. Let me know and. What else. So do you have any idea of what a key word or a buzzword would be for Sam to help him. No, I mean, when he first started, he was fine. But it's just like he's just put up all the breaks and he's just done with it all. Okay. And I mean, I know that he has said. I mean, he just doesn't understand it. The office is pretty sure that he goes to. Then he didn't understand why because he got he married before from that other doctor. Who wasn't associated with free state and this is just yeah, he just doesn't get it. Why? And I'm like, well, and I said to them, I said, well, I guess he can search for another dermatologist to give it to him, but nobody at free state's going to. Right. So he's just kind of stuck. I said, Dr. George won't give it. I know Dr. I'm usually why I won't get it. He's got to do this treatment. So. Well, I will. I will. All right. That's okay. I'll just try to explain in the letter. Maybe that I understand that you had the American another rheumatologist previously. And it's probably hard to understand what's different this time. Yeah. And I mean, would he always, I mean, this is my ignorance on T be gold, but would he always, I mean, if that rheumatologist did a T be gold, would it have been positive back then or could it just have? I mean, he may have developed it now. So he may have been negative before. Okay. And now be positive. Okay. He should have a record with the state health department if he had a positive one before. Right. Depending on who's reporting it. Yeah, he should be. This I think who he went to was in Joplin, Missouri. Who knows what they did. What if they reported it in Missouri? Yeah, I don't know. You know, just so happens, I used to work in Missouri. I hope it doesn't find a call them and see if he had a positive one back then. Okay. And I don't remember. I don't think the doctor that was in Joplin is practicing there anymore. And I can't. I don't even remember who it was. But I think he went to Joplin. I may be totally wrong. Well, I'll call Missouri the Missouri State Health Department. Okay. I didn't see if they have any record. They've been really good. I had the syphilis patient with them that they got to love me for. So I'll call the TV department, see what I can find. And then I will get a letter to you sometime today. Okay. I'll get it out later today. Well, either later today or it'll be the first of the week because I'm not going to be here Thursday and Friday because. My girlfriend's an eye or having a garage sale. My favorite thing to do in life. You are a much braver person or you have crazier girlfriends than I do. Yeah. When I go friends talk about that, honestly, I just hand them more wide and say, let's pick a book to read instead. Yeah. I know. I just got too much a gent to get rid of. And my daughter has a ton of stuff. And that's nice. She was like, we ran out of stickers to mark her boyfriend and her stuff. And so we've gone through 600. And I went, okay. Well, we're going to get some more. We're only at some more stickers. So I finished marking. I said, well, you have a whole box that was at my house that was not marked and the sack. But I can mark him Friday while we're not busy probably. She was like, okay, just have to bring everything in, which I'm sure she's going to go. That's my step and you have your initials on it. Yeah. Well, it's been stored in my house. So I'm going to put my initials on it. Exactly. You should get some benefit. Yeah. So my split it with her. There you go. All right. Well, I will try to get this. I'll call Missouri and I'll try to get this information as soon as I can. Okay. My dog first. Okay. All right. Well, I'm sorry about your aunt. Thank you. I appreciate it. You take care. It's always a pleasure to work with you. Thanks. I do need to tell you, I am retiring. Oh, you're the first provider I've told. My last day is going to be December 17th. November, time June, January 1st. So yeah, I'll take a vacation time. Well, and I'm totally calling Colleen's not very happy and they haven't hired. So hopefully I'll get the hire and I'll get the person trained because Colleen's like you have to train now. Because we haven't and godly. I'm any amount of patients and stuff. But you know, I was hired for 20 hours and I'm working like 37 and I really want more time. And I'm talking about a retired period. So I and I love the job. That's just not it. I mean, I would continue, but I just want more time. So I'm expecting another grandchild. So another grand send. So in March. So all of the new need time to go and enjoy the yes. We dedicated enough of your time to the rest of the world. Sometimes we have to take care of ourselves. Right. Right. I will miss working with you. And I want to thank you. Thank you. I'm sure we'll have more patients before I leave. There you go. I will get hopefully well. Darren straightened out and hopefully getting back to work and everything. So I hope so. Yeah. All right. Well, you take care. All right. You too. Bye bye. Bye bye.
'''
payload_for_transcript = '''{
    "filepath":"",
    "ftype": "mp3",
    "filesource": "gdrive",
    "saveinDB": "no",
    "wso2_username":"admin"
}'''

payload_for_textsum = {
  "wso2_username":"admin",
  "text":text,
  "filesource": "text",
  "source_lang": "English",
  "saveinDB": "no"
}

def call_transcript_api(payload):
    headers = {'Content-Type': 'application/json'} #, 'Authorization': 'Bearer '+ access_token}
    try:
        payload = json.loads(payload)
    except Exception as e:
        print(e)
    response= requests.post(url=url_for_transcript_api, json=payload,headers=headers)
    return response.json()

def call_textsummerize_api(payload):
    headers = {'Content-Type': 'text/plain'}#, 'Authorization': 'Bearer '+ access_token}
    # try:
    #     payload = json.loads(payload)
    # except Exception as e:
    #     print(e)
    response= requests.post(url=url_for_textsummerize_api, json=payload,headers=headers)
    return response.json()

def call_healthtag_api(payload):
    headers = {'Content-Type': 'application/json'} #, 'Authorization': 'Bearer '+ access_token}
    try:
        payload = json.loads(payload)
    except Exception as e:
        print(e)
    response= requests.post(url=url_for_healthtag, json=payload,headers=headers)
    return response.json() 
    

if __name__=="__main__":
    # print(call_transcript_api(payload_for_transcript))
    print(call_textsummerize_api(payload_for_textsum))