package main;

import java.util.Map;

public class WordCount_main {

	public static void main(String[] args) {

		WordCount wordCnt = new WordCount();
		
		String[] strings = {"a", "b", "a", "c", "b"};
		Map<String, Integer> result = wordCnt.countWords(strings);
		
		System.out.println(result);
	}
}
