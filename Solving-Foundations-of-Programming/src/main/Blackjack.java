package main;

/*
 * https://codingbat.com/prob/p117019
 * 
 * Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. 
 * Return 0 if they both go over.
 * 
 * blackjack(19, 21) → 21
 * blackjack(21, 19) → 21
 * blackjack(19, 22) → 19
 * */
public class Blackjack {
	public int play(int a, int b) {
		int result = 0;
		if (a > 21 && b > 21) {
			return result;
		} else {
			if (a >= b) {
				result = a <= 21 ? a : b;
			} else if (a < b) {
				result = b <= 21 ? b : a;
			}
		}
		return result;
	}
}
