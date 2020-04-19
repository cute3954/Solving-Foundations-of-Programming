package main;

/*
 *  参照：　https://github.com/mirandaio/codingbat/blob/master/java/array-3/maxSpan.java
*/
public class MaxSpan_modified {

	public static void main(String[] args) {
		int[] nums = {1, 4, 2, 1, 4, 4, 4};
		int result = maxSpan(nums);
		System.out.println(result);
	}
	
	public static int maxSpan(int[] nums) {
		int max = 0;
		for (int i = 0; i < nums.length; i++) {
			// 配列の先頭要素は０から順に番号が割り当てられるため、1を引く
			int j = nums.length - 1;
			// nums[i]とnums[j]が一致するまで繰り返し処理
			while (nums[i] != nums[j]) {
				j--;
			}
			int span = j - i + 1;
			if (span > max) {
				max = span;
			}
		}
		return max;
	}
}
