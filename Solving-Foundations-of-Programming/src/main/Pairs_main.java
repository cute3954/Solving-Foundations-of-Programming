package main;

import java.util.Map;

public class Pairs_main {

	public static void main(String[] args) {

		Pairs pairs = new Pairs();
		
		String[] strings = {"man", "moon", "good", "night", "choichoi"};
		Map<String, String> result = pairs.makePairs(strings);
		
		System.out.println(result);
	}
}
