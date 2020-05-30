package main;

/*
 * https://codingbat.com/prob/p294185
 * Write a simple interpreter which understands "+", "-", and "*" operations. 
 * Apply the operations in order using command/arg pairs starting with the initial value of `value`. 
 * If you encounter an unknown command, return -1.
 * 
 * interpret(1, ["+"], [1]) → 2
 * interpret(4, ["-"], [2]) → 2
 * interpret(1, ["+", "*"], [1, 3]) → 6
 * 
 * */
public class Interpret {
	public int cal(int value, String[] commands, int[] args_int) {
		for (int i = 0; i < commands.length; i++) {
			switch (commands[i]) {
				case "+":
					value += args_int[i];
					break;
				case "-":
					value -= args_int[i];
					break;
				case "*":
					value *= args_int[i];
					break;
				default:
					return -1;
			}	
		}
		return value;
	}
}
