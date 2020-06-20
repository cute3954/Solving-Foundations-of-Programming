package main;

import java.util.HashMap;
import java.util.Map;

/*
 * https://codingbat.com/prob/p117630
 * 
 * The classic word-count algorithm: given an array of strings, 
 * return a Map<String, Integer> with a key for each different string, 
 * with the value the number of times that string appears in the array.
 * 
 * wordCount(["a", "b", "a", "c", "b"]) → {"a": 2, "b": 2, "c": 1}
 * wordCount(["c", "b", "a"]) → {"a": 1, "b": 1, "c": 1}
 * wordCount(["c", "c", "c", "c"]) → {"c": 4}
 * */
public class WordCount {
	public Map<String, Integer> countWords(String[] strings) {
		Map<String, Integer> result = new HashMap<String, Integer>();
		for (String str : strings) {
			if (result.containsKey(str)) {
				result.put(str, result.get(str) + 1);
			} else {
				result.put(str, 1);
			}
		}
		return result;
	}
}
