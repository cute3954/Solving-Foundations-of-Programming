package main;

import java.util.HashMap;
import java.util.Map;

/*
 * https://codingbat.com/prob/p126332
 * 
 * Given an array of non-empty strings, create and return a Map<String, String> as follows: 
 * for each string add its first character as a key with its last character as the value.
 * 
 * pairs(["code", "bug"]) → {"b": "g", "c": "e"}
 * pairs(["man", "moon", "main"]) → {"m": "n"}
 * pairs(["man", "moon", "good", "night"]) → {"g": "d", "m": "n", "n": "t"}
 * */
public class Pairs {
	public Map<String, String> makePairs(String[] strings) {
		Map<String, String> result = new HashMap<String, String>();
		for (String str : strings) {
			String firstStr = str.substring(0, 1);
			String lastStr = str.substring(str.length() - 1);
			result.put(firstStr, lastStr);
		}
		return result;
	}
}
