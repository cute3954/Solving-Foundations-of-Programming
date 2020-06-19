package main;

import java.util.HashMap;
import java.util.Map;

/*
 * https://codingbat.com/prob/p152303
 * 
 * Given an array of strings, return a Map<String, Integer> containing a key for every different string in the array, always with the value 0. For example the string "hello" makes the pair "hello":0. We'll do more complicated counting later, but for this problem the value is simply 0.
 * 
 * word0(["a", "b", "a", "b"]) → {"a": 0, "b": 0}
 * word0(["a", "b", "a", "c", "b"]) → {"a": 0, "b": 0, "c": 0}
 * word0(["c", "b", "a"]) → {"a": 0, "b": 0, "c": 0}
 * 
 * */
public class Word0 {
	public Map<String, Integer> changeTo0(String[] strings) {
		Map<String, Integer> result = new HashMap<String, Integer>();
		for (String str : strings) {
			result.put(str, 0);
		}
		return result;
	}
}
