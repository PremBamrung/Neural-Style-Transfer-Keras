# Neural-Style-Transfer-Keras
Quick introduction to neural style transfert using Keras with TensorFlow in backend.

For each iteration, a picture is saved. It is recommended to create a new directory and put each picture in it. We can then create a video from this sequence of pictures. 

The python script  image2video.py combines the sequence of .png file into a video. It is recommended to add leading zero beforehand.
To do so, we can use a bash command. rename is used here (if not installed, sudo apt install rename)

## To rename all .png files and add  leading zero (1->01)
rename -e 's/\d+/sprintf("%03d",$&)/e' -- *.png

or use the rename_leading_zero.py script

## To create a new directory, move all files in it and zip this directory
!mkdir Result

!bash -c 'mv my_result_at_iteration_.{0..599}.png /content/Result

!zip -r /content/file.zip /content/Result


## To run the neural style transfer 
python3 neural_style_transfer.py path_to_your_base_image.jpg path_to_your_reference.jpg prefix_for_results

With the provided exemple, it would look like this in a Google Colba notebook, with Shiba.jpg and Starry_night.jpg uploaded:

python3 neural_style_transfer.py content/Shiba.jpg content/Starry_night.jpg content/my_result --iter 600

Optional parameters in the neural_style_transfer.py script.

