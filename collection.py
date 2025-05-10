# Misael Rivera - Perez
# 5/10/2025
# This program will list 4 different authors and their year of death

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print("%s died on %s" % (author, date))

input("Press ENTER to Exit") # This makes sure the program doesn't close until Enter key is pressed