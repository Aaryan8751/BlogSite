from django.shortcuts import render
from datetime import date

all_posts=[
    {
        'slug':'hike-in-the-mountains',
        'image':'mountains.jpg',
        'author':'Ryan',
        'date':date(2021,7,21),
        'title':'Mountain Hiking',
        'excerpt':'''There's nothing like the views you get when hiking in the mountains! And I wasn't even
            prepared for what happened whlist I was enjoying the view!''',
        'content':'''
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Similique qui possimus eligendi iusto, nisi dolore iste perspiciatis repudiandae, excepturi asperiores, tempore animi sequi itaque hic delectus sit minima architecto! Ea.

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Similique qui possimus eligendi iusto, nisi dolore iste perspiciatis repudiandae, excepturi asperiores, tempore animi sequi itaque hic delectus sit minima architecto! Ea.

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Similique qui possimus eligendi iusto, nisi dolore iste perspiciatis repudiandae, excepturi asperiores, tempore animi sequi itaque hic delectus sit minima architecto! Ea.
        '''
    },
     {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Ryan",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Similique qui possimus eligendi iusto, nisi dolore iste perspiciatis repudiandae, excepturi asperiores, tempore animi sequi itaque hic delectus sit minima architecto! Ea.

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Similique qui possimus eligendi iusto, nisi dolore iste perspiciatis repudiandae, excepturi asperiores, tempore animi sequi itaque hic delectus sit minima architecto! Ea.

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Similique qui possimus eligendi iusto, nisi dolore iste perspiciatis repudiandae, excepturi asperiores, tempore animi sequi itaque hic delectus sit minima architecto! Ea.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Ryan",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
         Lorem ipsum dolor sit amet consectetur, adipisicing elit. Similique qui possimus eligendi iusto, nisi dolore iste perspiciatis repudiandae, excepturi asperiores, tempore animi sequi itaque hic delectus sit minima architecto! Ea.

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Similique qui possimus eligendi iusto, nisi dolore iste perspiciatis repudiandae, excepturi asperiores, tempore animi sequi itaque hic delectus sit minima architecto! Ea.

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Similique qui possimus eligendi iusto, nisi dolore iste perspiciatis repudiandae, excepturi asperiores, tempore animi sequi itaque hic delectus sit minima architecto! Ea.
        """
    }
]
def get_date(post):
    return post['date']

# Create your views here

def starting_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    context={
        "posts":latest_posts
    }
    return render(request, 'blog/index.html',context)
def posts(request):
    context={
        "all_posts":all_posts
    }
    return render(request,'blog/all-posts.html',context)

def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post["slug"]==slug)
    context={
        "post":identified_post
    }
    return render(request,'blog/post-detail.html',context)
