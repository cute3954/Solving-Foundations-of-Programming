package main;

/*
 * https://codingbat.com/prob/p256268
 * 
 * Fix this duplicate collapsing code: 
 * public String collapseDuplicates(String a) { int i = 0; String result = ""; 
 * while (i < a.length()) { char ch = a.charAt(i); result += ch; 
 * while (a.charAt(i+1) == ch) { i++; } i++; } return result; }
 * 
 * collapseDuplicates("a") → "a"
 * collapseDuplicates("aa") → "a"
 * collapseDuplicates("abc") → "abc"
 * */
public class CollapseDuplicates {
	public String fix(String a) {
		int i = 0; 
		String result = ""; 
		
		while (i < a.length()) { 
			char ch = a.charAt(i); 
			if (result == "" || result.charAt(result.length() - 1) != ch) {
				result += ch; 
			}
		    i++;      
		} 
		return result;		
	}
}
