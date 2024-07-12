#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine
# lib/debug.py

if __name__ == "__main__":
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    article1 = author1.add_article(magazine1, "The Future of AI")
    article2 = author2.add_article(magazine1, "Advancements in Robotics")
    article3 = author1.add_article(magazine2, "Healthy Living Tips")
    article4 = author1.add_article(magazine1, "AI and Healthcare")
    article5 = author2.add_article(magazine1, "AI in Everyday Life")

    import ipdb; ipdb.set_trace()

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
