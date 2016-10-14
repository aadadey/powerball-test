# powerball-test

This work completes the Powerball project required to submit a Python Developer application to Greenphire.

As some of the requirements were unclear, they were interpreted as such:

1) Allow an undetermined number of employees to enter powerball numbers
2) Restrict the first five numbers to be a unique set with each value between 1 and 69.
3) Restrict the final number to be a value between 1 and 26 (but can be a repeat of any of the first five)
4) Once the user is done entering employee powerball numbers (via a Y/N question), calculate the winning number:
  a) For each position (1 through 6), find the most common number among all the entries (in that SPECIFIC position)
  b) If there is a tie for most common, randomly choose from all entries in that position
  
Based on the interpreted requirements above, the sample output given is actually invalid (see below)
but I have made sure the logic in my code reflects the requirements and not the sample.


Sample output below (incorrect because winning numbers 5 and 5 (55 and 63) do not appear in neither of the drawings)
----------------------------------------------
Wade Wilson 15 26 33 60 34 powerball: 16 Frank Castle 15 26 34 56 61 powerball: 16

Powerball winning number:

15 26 34 55 63  powerball: 16
