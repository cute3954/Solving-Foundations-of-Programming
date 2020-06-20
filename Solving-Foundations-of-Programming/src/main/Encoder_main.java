package main;

import java.util.List;

public class Encoder_main {

	public static void main(String[] args) {

		Encoder encoder = new Encoder();
		
		String[] raw = {"a"};
		String[] code_words = {"1", "2", "3", "4"};
		
		List<String> result = encoder.replaceWords(raw, code_words);
		
		System.out.println(result);
	}
}
