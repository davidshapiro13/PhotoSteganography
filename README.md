# Image Steganography
### Created by David Shapiro
#### May 2024

###### NOTE: Only compatable with PNG files.

##### To run, type the following into the terminal:
    python3 FinalProject.py
##### An example image is provided. It is titled *original.png*

##### Capabilities
This program will take in an image path and a text message from either a file or the console and it will use Least Significant Bit Steganography to hide the message in the image.

It will also do the inverse operation and decode a message hidden in an image.

##### If I Had More Time:
To expand this project, I would like to add the ability to code and decode messages in JPEG and other lossy formats. This would require learning about Discrete Cosine Transforms which is beyond my current abilities and thus, I didn't have enough time to explore it in this project. I would also like to actually implement encoding and decoding for other media such as sounds, videos and networks.

In doing so, I would also like to learn more about different steganography techniques and how those techniques can be detected.

##### Challenges Faced:

I had a relatively straight-forward time implementing the least significant bit (LSB) algorithm but I did run into trouble when I learned it didn't work for JPEGs. It took some researching before I learned that you can't use LSB on lossy files. Then I tried to learn how to use steganography for lossy images but the math involved was too complex for my current abilities and amount of time.

I also had challenges finding sources that were at my level and were relevant for my project. Overall though, I perserved, learned a lot and had fun coding this project.

##### Coding Sources

*Python Imaging Library (PIL)*
https://www.geeksforgeeks.org/how-to-manipulate-the-pixel-values-of-an-image-using-python/

*Steganography Basics*
https://www.youtube.com/watch?v=TWEXCYQKyDc

Googling basic python things I didn't know how to do (bit operations for example)