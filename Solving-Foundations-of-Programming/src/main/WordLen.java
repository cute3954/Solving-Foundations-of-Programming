package main;

import java.util.HashMap;
import java.util.Map;

/*
 * http://codingbat.com/prob/p125327
 * Given an array of strings, return a Map<String, Integer> containing a key for every different string in the array, and the value is that string's length.
 * 
 * wordLen(["a", "bb", "a", "bb"]) → {"bb": 2, "a": 1}
 * wordLen(["this", "and", "that", "and"]) → {"that": 4, "and": 3, "this": 4}
 * wordLen(["code", "code", "code", "bug"]) → {"code": 4, "bug": 3}
 * 
 * */
public class WordLen {
	public Map<String, Integer> insertStrLen(String[] strings) {
		Map<String, Integer> result = new HashMap<String, Integer>();
		for (String str : strings) {
			result.put(str, str.length());
		}
		return result;
	}
}
