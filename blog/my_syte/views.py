from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "post_name" : "mount-hiking",
        "image" : "mount.jpg",
        "author" : "mahdi",
        "date" : date(2022,10,11),
        "title" : "Mountain hiking",
        "expert" :"Hiking is a long distance walk along a specific trail, most commonly across country. Some hikes can be challenging and last for days including camping, but others can be a long day walk at a steady pace. However, mountain climbing is a challenging sport in which people climb steep rocky slopes to reach the top",
        "content" : """A mountain is an elevated portion of the Earth's crust, generally with steep sides that show significant exposed bedrock. Although definitions vary, a mountain may differ from a plateau in having a limited summit area, and is usually higher than a hill, typically rising at least 300 metres (980 ft) above the surrounding land. A few mountains are isolated summits, but most occur in mountain ranges.[1]

Mountains are formed through tectonic forces, erosion, or volcanism,[1] which act on time scales of up to tens of millions of years.[2] Once mountain building ceases, mountains are slowly leveled through the action of weathering, through slumping and other forms of mass wasting, as well as through erosion by rivers and glaciers.[3]

High elevations on mountains produce colder climates than at sea level at similar latitude. These colder climates strongly affect the ecosystems of mountains: different elevations have different plants and animals. Because of the less hospitable terrain and climate, mountains tend to be used less for agriculture and more for resource extraction, such as mining and logging, along with recreation, such as mountain climbing and skiing.

The highest mountain on Earth is Mount Everest in the Himalayas of Asia, whose summit is 8,850 m (29,035 ft) above mean sea level. The highest known mountain on any planet in the Solar System is Olympus Mons on Mars at 21,171 m (69,459 ft).
"""

    },
]
def get_date(post):
    return post['date']
def home_page(request):
    latest_posts = sorted(all_posts, key=get_date)[-3:]
    return render(request, 'my_syte/home_page.html', {'posts' : latest_posts})

def posts(request):
    return render(request, 'my_syte/all_posts.html', {"posts" : all_posts})

def post_ditails(request, post_name):
    post = next(post for post in all_posts if post['post_name'] == post_name)
    return render(request, 'my_syte/post_detail.html', {'post': post})