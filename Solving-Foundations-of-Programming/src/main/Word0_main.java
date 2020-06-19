package main;

import java.util.Map;

public class Word0_main {

	public static void main(String[] args) {
		Word0 word0 = new Word0();
		
		String[] strings = {"a", "b", "a", "b"};
		Map<String, Integer> result = word0.changeTo0(strings);
		
		System.out.println(result);
	}
}
