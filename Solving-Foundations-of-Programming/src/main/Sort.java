package main;

import java.util.Arrays;

/*
 * https://codingbat.com/prob/p262890
 * Return an array that contains the sorted values from the input array with duplicates removed.
 * 
 * sort([]) → []
 * sort([1]) → [1]
 * sort([1, 1]) → [1]
 * */
public class Sort {
	public int[] sortInt(int[] a) {
		// Arrays.streamメソッドでIntStreamが取得できる
		// distinct()で重複を除いた要素から構成されるストリームを得る
		// toArray()メソッドでint型の配列を取得
		int[] result = Arrays.stream(a).distinct().toArray();
		return result;
	}
}
