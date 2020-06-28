package main;

public class CollapseDuplicates_main {

	public static void main(String[] args) {
		CollapseDuplicates collapseDuplicates = new CollapseDuplicates();
		
		String result = collapseDuplicates.fix("abbbcaaa");
		
		System.out.println(result);
	}
}
