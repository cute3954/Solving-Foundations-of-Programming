package main;

import java.util.Map;

public class WordLen_main {

	public static void main(String[] args) {

		WordLen wordLen = new WordLen();
		
		String[] strings = {"a", "bb", "a", "bb"};
		Map<String, Integer> result = wordLen.insertStrLen(strings);
		
		System.out.println(result);
	}
}
