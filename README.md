# Neural-Style-Transfer-Keras
Quick introduction to neural style transfert using Keras with TensorFlow in backend.

For each iteration, a picture is saved. It is recommended to create a new directory and put each picture in it. We can then create a video from this sequence of pictures. 

The python script  image2video.py combines the sequence of .png file into a video. It is recommended to add leading zero beforehand.
To do so, we can use a bash command. rename is used here (if not installed, sudo apt install rename)

# to rename all .png files and add  leading zero (1->01)
rename -e 's/\d+/sprintf("%03d",$&)/e' -- *.png

# to create a new directory, move all files in it and zip this directory
!mkdir Result
!bash -c 'mv my_result_at_iteration_.{0..599}.png /content/Result
!zip -r /content/file.zip /content/Result

In the folder
