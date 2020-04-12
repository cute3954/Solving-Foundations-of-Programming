package main;

/*
 * 参照：　https://codingbat.com/prob/p117334
 * Given a non-empty string like "Code" return a string like "CCoCodCode".
 * 
 * stringSplosion("Code") → "CCoCodCode"
 * stringSplosion("abc") → "aababc"
 * stringSplosion("ab") → "aab"
*/
public class stringSplosion {

	public static void main(String[] args) {
		String word = "Code";
		String newWord = stringSplosion(word);
		System.out.println(newWord);

	}
	
	public static String stringSplosion(String str) {
	  // strArrayに1文字多い配列を作る
	  String[] strArray = new String[str.length()];
	  // 変数strの長さ分回す
	  for (int i = 0; i < str.length(); i++) {
	    // charAt(): 文字列からn番目の文字を抜き出す。
	    // valueOf(): 引数に指定した値をString型の文字列としてｈ返す。
	    // strの先頭から1文字ずつString型にして取り出す。
	    strArray[i] = String.valueOf(str.charAt(i));
	  }
	  // 新しい文字列を格納する変数
	  String createNewWord = "";
	  //　配列の長さ
	  for (int i = 0; i <= strArray.length; i++) {
	    for (int j = 0; j < i; j++) {
	      createNewWord += strArray[j];
	    }
	  }
	  return createNewWord;
	}
}
