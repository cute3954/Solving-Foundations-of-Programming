package main;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * https://codingbat.com/prob/p238573
 * 
 * Write a function that replaces the words in `raw` with the words 
 * in `code_words` such that the first occurrence of each word 
 * in `raw` is assigned the first unassigned word in `code_words`.
 * 
 * encoder(["a"], ["1", "2", "3", "4"]) → ["1"]
 * encoder(["a", "b"], ["1", "2", "3", "4"]) → ["1", "2"]
 * encoder(["a", "b", "a"], ["1", "2", "3", "4"]) → ["1", "2", "1"]
 * */
public class Encoder {
	public List<String> replaceWords(String[] raw, String[] code_words) {
		Map<String, String> strEncoder = new HashMap<String, String>();
		strEncoder.put("a", code_words[0]);
		strEncoder.put("b", code_words[1]);
		strEncoder.put("c", code_words[2]);
		strEncoder.put("d", code_words[3]);
		
		List<String> result = new ArrayList<String>();
		for (int i = 0; i < raw.length; i++) {
			result.add(strEncoder.get(raw[i]));
		}
		return result;
	}
}
