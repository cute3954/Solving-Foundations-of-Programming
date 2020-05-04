package main;

public class CanBalance_main {
	
	public static void main(String[] args) {
		int[] nums = {1, 1, 1, 2, 1};
		CanBalance canBal = new CanBalance();
		boolean result = canBal.canBalance(nums);
		System.out.println(result);
	}
	
}
