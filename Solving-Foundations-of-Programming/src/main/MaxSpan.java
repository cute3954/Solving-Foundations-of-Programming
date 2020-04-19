package main;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/*
 *  参照： https://codingbat.com/prob/p189576
 *  Consider the leftmost and rightmost appearances of some value in an array. We'll say that the "span" is the number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found in the given array. (Efficiency is not a priority.)
 *  
 *  maxSpan([1, 2, 1, 1, 3]) → 4
 *  maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
 *  maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6
*/
public class MaxSpan {

	public static void main(String[] args) {
		// Arrays.asList():　引数で指定した配列をリストとして返す
		List<Integer>nums = Arrays.asList(1, 4, 2, 1, 4, 4, 4);
		int result = maxSpan(nums);
		System.out.println(result);
	}
	
	public static int maxSpan(List<Integer> nums) {
		// Listに格納されている数値をキー、数値の数をバリューとして保存する
		// Collectors.groupingBy：　Listをグルーピングし、Key-ListのMap型データを取得できる（SQLであればGROUP BYみたいなもの…？）
		// Collectors.counting:　要素の数
		Map<Object, Long> count_of_nums = nums.stream().collect(Collectors.groupingBy(x -> x, Collectors.counting()));  
        int max_key = 0;
		int max_value = 0;
		// 数が一番多いデータだけ、キーとバリューを変数に格納する
		for (Map.Entry<Object, Long> num : count_of_nums.entrySet()) {
            if (num.getValue() > max_value) {
            	max_key = (int) num.getKey();
            	// long型の引数をintで返す。
            	max_value = Math.toIntExact(num.getValue());
            }
        }
		
		int result = 0;
		int max_value_dummy = 0;
		
		for (int i = 0; i < nums.size(); i++) {
			if (result == 0) {
				if (nums.get(i) == max_key && max_value_dummy == 0) {
					result++;
					max_value_dummy++;
				}
			} else {	
				if (max_value_dummy < max_value) {
					result++;
				}
				if (nums.get(i) == max_key) {
					max_value_dummy++;
				}	
			}
		}
		
		return result;
		
	}
}
