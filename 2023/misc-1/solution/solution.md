The easiest way do depixelize an image is to use Depix. For the tool to work the user has to know what text editor and what algorithm were used. The editor can be guessed to be notepad.exe and the pixelizer has to be Gimp because of the image metadata.
The whole image can't be depixelized at once, you have to cut it into smaller pieces (usually lines, but special characters aren't included in the default training data so you have to cut off the pixelized $ from the menu prices to be able to get the numbers.)
Based on the examples on the Depix GitHub, you can create the command using the knowledge above and reconstruct the program:

depix -p .\cut.png -s .\Depix-main\images\searchimages\debruinseq_notepad_Windows10_closeAndSpaced.png -o depixelized.png --averagetype linear

The original image is of a 'Drive-In Window' program. By finding this out quickly you can drastically reduce the amount of depixelization you have to do. Afterwards you can run the reconstructed program in an interpreter and it will print out the flag.