package main;

public class Interpret_main {

	public static void main(String[] args) {
		Interpret inter = new Interpret();
		int value = 1;
		String[] commands = {"+", "*"}; 
		int[] args_int = {1, 3};
		int result = inter.cal(value, commands, args_int);
		System.out.println(result);
	}
}
