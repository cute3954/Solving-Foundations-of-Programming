package main;


/*
 * https://codingbat.com/prob/p158767
 * Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.
 * 
 * canBalance([1, 1, 1, 2, 1]) → true
 * canBalance([2, 1, 1, 2, 1]) → false
 * canBalance([10, 10]) → true
 * 
 * */
public class CanBalance {
	
	public boolean canBalance(int[] nums) {
		
		int total = 0;
		int rightsum = 0;
		int leftsum = 0;
		boolean result = false;
		
		for (int i = 0; i < nums.length; i++) {
			total += nums[i];
		}
		
		// 配列が要素を１つしか持っていない場合は比較対象がないため、必ずfalseになる。
		// 従って、判定を行わない。
		if (nums.length > 1) {
			for (int i = 0; i < nums.length; i++) {
				leftsum += nums[i];
				if (leftsum == total / 2) break; 
			}
			
			rightsum = total - leftsum;
			if (leftsum == rightsum) result = true;
		}		
		
		return result; 
	}

}
