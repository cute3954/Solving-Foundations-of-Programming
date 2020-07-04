package main;

public class MakeBricks_main {

	public static void main(String[] args) {

		MakeBricks makeBricks = new MakeBricks();
		
		boolean result = makeBricks.make(22, 2, 33);
		
		System.out.println(result);
	}
}
