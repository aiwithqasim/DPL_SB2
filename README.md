# Intro
In many situations you may find yourself having duplicates files on your disk and but when it comes to tracking and checking them manually it can tedious.

## Here is a solution
Instead of tracking throughout your disk to see if there is a duplicate, you can automate the process using coding, by writing a program to recursively track through the disk and remove all the found duplicates and that's what this article is about.

## But How do we do it?
If we were to read the whole file and then compare it to the rest of the files recursively through the given directory it will take a very long time, then how do we do it
The answer is hashing, with hashing we can generate a given string of letters and numbers which acts as the identity of a given file and if we find any other file with the same identity we gonna delete it.

We would be using hashlib library in python for the said purpose. There's a variety of hashing algorithms out there such as:
- md5
- sha1
- sha224, sha256, sha384 and sha512 etc.

Lets install this python library to remove the Duplicate file in the existing Working directory by <em>"pip install DPL_SB2"</em>

### Contribution Guideline:
Feel free to open a PR if you feel like something needs to be added or you want to suggest something then your commit message should be in given format: **added to -->resource_name-->section_name**
