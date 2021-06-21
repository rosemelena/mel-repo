//This program is a game of Hotter or Colder, this will pring who ill win between jack or jill

import java.util.*;

public class HotterColder{

	public static void main (String[] args){

		//initialize var and assigning random number to jill
		int in_it = 101;
		Random rndm = new Random();
		int jill = rndm.nextInt(in_it);

		System.out.printf("\nJill's number is: %d\n\nGuess\t| Action\n", jill);

		//initialize var for guessing
		int prevGuess = 0, numGuess = 0, minLeft = 0, maxRight = 100,  jack = ((minLeft + maxRight)/2);

		while (jack != jill){ //this will continue looping until jack and jill are equal

			if (jack > jill){ //if jack is greater than jill, this will set maxRight or the max number to jack minus 1. this will be use for next guessing until found
				maxRight = jack - 1;

			} else if (jack < jill){ //if jack is less than jill, this will set minLeft or the min number to jack plus 1
				minLeft = jack + 1;
			}

			numGuess += 1; //will iterate each loop


			//CONDITIONS IN FINDING JACK

			//I use abs because it is possible that the answer will be both negative and I will only need the positive
			if (numGuess == 1){ //First run will always print same and will become the first basis for next guess
				System.out.printf("%d\t| Same\n", jack);

			} else if (Math.abs(prevGuess - jill) > Math.abs(jack - jill)){ //Hotter if the diff of prev and jill is GREATER than the diff of jack and jill
				System.out.printf("%d\t| Hotter\n", jack);

			} else if (Math.abs(prevGuess - jill) < Math.abs(jack - jill)){ //Colder if the diff of prev and jill is LESS than the diff of jack and jill
				System.out.printf("%d\t| Colder\n", jack);

			} else {
				System.out.printf("%d\t| Same\n", jack); //Else same
			}
			prevGuess = jack; //will set jack as previous guess or basis
			jack = ((minLeft + maxRight)/2);//since jack became the prevGuess, Jack will be set to new formula whether it's minLeft or maxRight (depends on guess)
		}
		numGuess += 1; //since the guess is correct, we put another iteration because the other one is inside the loop
		System.out.printf("%d\t| CORRECT\n", jack);
		System.out.printf("\nNumber of guesses: %d\n", numGuess);
	}
}