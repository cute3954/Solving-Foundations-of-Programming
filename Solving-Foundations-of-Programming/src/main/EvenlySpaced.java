package main;

import java.util.Arrays;

/*
 * https://codingbat.com/prob/p198700
 * 
 * 
 * Given three ints, a b c, one of them is small, one is medium and one is large. 
 * Return true if the three values are evenly spaced, so the difference between small 
 * and medium is the same as the difference between medium and large.
 * 
 * evenlySpaced(2, 4, 6) → true
 * evenlySpaced(4, 6, 2) → true
 * evenlySpaced(4, 6, 3) → false
 * */
public class EvenlySpaced {
	public boolean calc(int a, int b, int c) {
		boolean result = false;
		int[] intArr = {a, b, c};
		Arrays.sort(intArr);
		
		result = intArr[1] - intArr[0] == intArr[2] - intArr[1] ? true : false;
		
		return result;
	}
}
